import math
import numpy
import datetime
import matplotlib.pyplot as plt
import sys
import astropy.io.fits as pyfits
import os
import glob





# Command line argument is the following:
# bias.fits dark.fits flat.fits (for each color) image_Color_*.fits

# * represents a wildcard and tells it to open all files named image_Color_...

# In command line, you put python filename.py bias.fits dark.fits ...
# If fits files in file put file/ before .fits in command line

# sys.argv prints the arguments from the command line
# print sys.argv
# the first term, sys.argv[0] is the filename





# Define our arguments

bias = pyfits.open("Transit/Transit_Data/Prompt5_mbias_304745.fits")
dark = pyfits.open("Transit/Transit_Data/Prompt5_mdark_0080_304751.fits")
flat = pyfits.open("Transit/Transit_Data/Prompt5_mflat_Green_305440.fits")

#bias = sys.argv[1]
#dark = sys.argv[2]
#flat = sys.argv[3]
# print bias

# Since our color images have varying file names we need to introduce glob
# The glob command allows Windows to look for varying filenames

#image_list = glob.glob(sys.argv[-1])
image_list = glob.glob('Transit/Transit_Data/wasp_77ab_hw5_1175421_Green_*.fits')
# print image_list

# From fits files we can load the data using pyfits.open[0].data

bias_data = (bias)[0].data
dark_data = (dark)[0].data
flat_data = (flat)[0].data

#bias_data = pyfits.open(bias)[0].data
#dark_data = pyfits.open(dark)[0].data
#flat_data = pyfits.open(flat)[0].data
# print flat_data





# Need to know exposures of bias, dark, and flat images

bias_header = (bias)[0].header
dark_header = (dark)[0].header
flat_header = (flat)[0].header

#bias_header = pyfits.open(bias)[0].header
#dark_header = pyfits.open(dark)[0].header
#flat_header = pyfits.open(flat)[0].header
# print flat_header
# print "Bias Exposure:", bias_header["EXPOSURE"]
# print "Dark Exposure:", dark_header["EXPOSURE"]
# print "Flat Exposure:", flat_header["EXPOSURE"]





# Before we calibrate the color images we first normalize the flats
# Our flats already have the bias and dark subtracted out
# To normalize we divide the flat data by the mean
# We also correct the exposure time of the flats
#originally had numpy.mean
flat_mean = numpy.average(flat_data)
normalized_flat = (flat_data / flat_mean)
# print normalized_flat





# For each color image we need to calibrate the files
# Then we need to feed the calibrated files into an array
# To create an empty array/list

aperture=numpy.zeros((200,200),numpy.float32)
background_aperture=numpy.zeros((200,200),numpy.float32)
reference_aperture_first=numpy.zeros((200,200),numpy.float32)
reference_background_aperture_first=numpy.zeros((200,200),numpy.float32)
reference_aperture_second=numpy.zeros((200,200),numpy.float32)
reference_background_aperture_second=numpy.zeros((200,200),numpy.float32)
radius = 6.0

transit_brightness = []
transit_time = []
reference_transit_brightness_first = []
reference_transit_brightness_second = []
# array = numpy.array((10,1024,1024))

j = 0

for file in image_list:
    j += 1
    # print file
    image_data = pyfits.open(file)[0].data
    # print image_data

    if j > 368:
        image_data = numpy.rot90(image_data,2)

    image_header = pyfits.open(file)[0].header
    image_time = image_header["TIME-OBS"].split(":")
    time_seconds = float(image_time[0])*3600.0 + float(image_time[1])*60.0 + float(image_time[2])
    #print time_seconds
    transit_time.append(time_seconds)
    # print transit_time

    # Calibrate each fits file

    # First subtract bias
    calibrate1 = image_data - bias_data
    # print calibrate1

    # Second scale dark exposure to match fits exposure and subtract
    calibrate2 = calibrate1 - dark_data * 60.0/80.0
    # print calibrate2

    # Third take our calibrated image and divide by normalized flat
    calibrated_images = calibrate2 / normalized_flat
    # print calibrated_images

    transit_array = calibrated_images[485:685,340:540]
    reference_array_first = calibrated_images[485:685,40:240]
    reference_array_second = calibrated_images[135:335,0:200]

    for x in range(0,200):
        for y in range (0,200):
            maximum_per_image = numpy.amax(transit_array)
            ymax,xmax = numpy.unravel_index(transit_array.argmax(),transit_array.shape)
            if (x-xmax)**2 + (y-ymax)**2 < (3.0*radius)**2:
                background_aperture[y,x] = 1

            if (x-xmax)**2 + (y-ymax)**2 < (3.0*radius-2.0)**2:
                background_aperture[y,x] = 0

            if (x-xmax)**2 + (y-ymax)**2 < (radius)**2:
                aperture[y,x] = 1

    for x in range(0,200):
        for y in range (0,200):
            maximum_per_image = numpy.amax(reference_array_first)
            ymax,xmax = numpy.unravel_index(reference_array_first.argmax(),reference_array_first.shape)
            if (x-xmax)**2 + (y-ymax)**2 < (3.0*2.0)**2:
                reference_background_aperture_first[y,x] = 1

            if (x-xmax)**2 + (y-ymax)**2 < (3.0*2.0-2.0)**2:
                reference_background_aperture_first[y,x] = 0

            if (x-xmax)**2 + (y-ymax)**2 < (2.0)**2:
                reference_aperture_first[y,x] = 1

    for x in range(0,200):
        for y in range (0,200):
            maximum_per_image = numpy.amax(reference_array_second)
            ymax,xmax = numpy.unravel_index(reference_array_second.argmax(),reference_array_second.shape)
            if (x-xmax)**2 + (y-ymax)**2 < (3.0*2.0)**2:
                reference_background_aperture_second[y,x] = 1

            if (x-xmax)**2 + (y-ymax)**2 < (3.0*2.0-2.0)**2:
                reference_background_aperture_second[y,x] = 0

            if (x-xmax)**2 + (y-ymax)**2 < (2.0)**2:
                reference_aperture_second[y,x] = 1

    
    
    
    background = transit_array * background_aperture

    background_light = numpy.sum(background)
    # Want number of pixels in background annulus
    background_pixels = (math.pi)*(3.0*radius)**2 - (math.pi)*(3.0*radius-2.0)**2
    # Background light per pixel
    background_per_pixel = background_light / background_pixels
    # Background light in Source
    background_source = background_per_pixel * (math.pi)*(radius)**2
    # print background_per_pixel

    image = (transit_array - background_per_pixel) * aperture

    
   
    reference_background_first = reference_array_first * reference_background_aperture_first

    # Total light in background
    reference_background_light_first = numpy.sum(reference_background_first)
    reference_background_pixels_first = (math.pi)*(3.0*2.0)**2 - (math.pi)*(3.0*2.0-2.0)**2
    reference_background_per_pixel_first = reference_background_light_first / reference_background_pixels_first
    reference_background_source_first = reference_background_per_pixel_first * (math.pi)*(2.0)**2

    reference_first = (reference_array_first - reference_background_per_pixel_first) * reference_aperture_first


    reference_background_second = reference_array_second * reference_background_aperture_second

    # Total light in background
    reference_background_light_second = numpy.sum(reference_background_second)
    reference_background_pixels_second = (math.pi)*(3.0*2.0)**2 - (math.pi)*(3.0*2.0-2.0)**2
    reference_background_per_pixel_second = reference_background_light_second / reference_background_pixels_second
    reference_background_source_second = reference_background_per_pixel_second * (math.pi)*(2.0)**2

    reference_second = (reference_array_second - reference_background_per_pixel_second) * reference_aperture_second

    
    # Total light in image
    image_brightness = numpy.sum(image)
    reference_brightness_first = numpy.sum(reference_first)
    reference_brightness_second = numpy.sum(reference_second)
    
    transit_brightness.append(image_brightness)
    reference_transit_brightness_first.append(reference_brightness_first)
    reference_transit_brightness_second.append(reference_brightness_second)

    combined_image = image + background
    combined_reference_first = reference_first + reference_background_first
    combined_reference_second = reference_second + reference_background_second



# To calibrate images I need the median of the reference star's brightness
reference_median_first = numpy.median(reference_transit_brightness_first)
reference_median_second = numpy.median(reference_transit_brightness_second)

# Calibration
calibration_per_image = (((reference_transit_brightness_first - reference_median_first) / reference_median_first))               

#+ ((reference_transit_brightness_second - reference_median_second) / reference_median_second))/2 

calibrated_transit_brightness = transit_brightness * (1-calibration_per_image)
    


#print transit_brightness

plt.scatter(transit_time,transit_brightness)
plt.xlabel("Time (seconds)")
plt.ylabel("Transit Brightness UnCalibrated")
plt.title("UnCalibrated Transit Brightness Over Time")
plt.show()

plt.scatter(transit_time, reference_transit_brightness_first)
plt.xlabel("Time (seconds)")
plt.ylabel("Reference Brightness")
plt.title("First Reference Brightness Over Time")
plt.show()

plt.scatter(transit_time, reference_transit_brightness_second)
plt.xlabel("Time (seconds)")
plt.ylabel("Reference Brightness")
plt.title("Second Reference Brightness Over Time")
plt.show()

plt.scatter(transit_time, calibrated_transit_brightness)
plt.xlabel("Time (seconds)")
plt.ylabel("Calibrated Brightness")
plt.title("Calibrated Brightness Over Time")
plt.show()







# To bin the images we need to only select number of images that can be easily divisible
calibrated_transit_brightness_selected = calibrated_transit_brightness[0:600]
transit_time_selected = transit_time[0:600]

calibrated_transit_brightness_selected = numpy.array(calibrated_transit_brightness_selected)
binned_calibrated_transit_brightness_selected = calibrated_transit_brightness_selected.reshape(120,-1)
binned_calibrated_transit_brightness = binned_calibrated_transit_brightness_selected.mean(axis=1)

plt.scatter(transit_time_selected[0::5], binned_calibrated_transit_brightness)
plt.xlabel("Time (seconds)")
plt.ylabel("Calibrated Brightness")
plt.title("Binned Calibrated Brightness Over Time")
plt.show()



   
# print image_stack
pyfits.PrimaryHDU(calibrated_images).writeto("Transit after calibration.fits",overwrite = True)

pyfits.PrimaryHDU(combined_image).writeto("Aperture.fits",overwrite = True)
