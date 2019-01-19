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
# If fits files in file put ngc7793/ before .fits in command line

# sys.argv prints the arguments from the command line
# print sys.argv
# the first term, sys.argv[0] is the filename





# Define our arguments

bias = sys.argv[1]
dark = sys.argv[2]
flat = sys.argv[3]
# print bias

# Since our color images have varying file names we need to introduce glob
# The glob command allows Windows to look for varying filenames

image_list = glob.glob(sys.argv[-1])
# print image_list

# From fits files we can load the data using pyfits.open[0].data

bias_data = pyfits.open(bias)[0].data
dark_data = pyfits.open(dark)[0].data
flat_data = pyfits.open(flat)[0].data
# print flat_data





# Need to know exposures of bias, dark, and flat images

bias_header = pyfits.open(bias)[0].header
dark_header = pyfits.open(dark)[0].header
flat_header = pyfits.open(flat)[0].header
# print flat_header
# print "Bias Exposure:", bias_header["EXPOSURE"]
# print "Dark Exposure:", dark_header["EXPOSURE"]
# print "Flat Exposure:", flat_header["EXPOSURE"]





# Before we calibrate the color images we first normalize the flats
# Our flats already have the bias and dark subtracted out
# To normalize we divide the flat data by the mean
# We also correct the exposure time of the flats

flat_mean = numpy.mean(flat_data)
normalized_flat = (flat_data / flat_mean)
# print normalized_flat





# For each color image we need to calibrate the files
# Then we need to feed the calibrated files into an array
# To create an empty array/list

image_stack = []
# array = numpy.array((10,1024,1024))

for file in image_list:
    # print file
    image_data = pyfits.open(file)[0].data
    # print image_data

    # Calibrate each fits file

    # First subtract bias
    calibrate1 = image_data - bias_data
    # print calibrate1

    # Second scale dark exposure to match fits exposure and subtract
    calibrate2 = calibrate1 - dark_data * 60.0/80.0
    # print calibrate2

    # Third take our calibrated image and divide by normalized flat
    calibrated_images = calibrate2 #/ normalized_flat
    # print calibrated_images

    # We need to append our images to the empty array    
    image_stack.append(calibrated_images)
    
# print image_stack





# Take the mean/median of the stack to get one array per color
# Take the mean/median along the depth of the array = axis=0

avg = numpy.mean(image_stack,axis=0)
# print avg
median = numpy.median(image_stack,axis=0)
# print median





# Finally we want to write out avg/median to a file
# overwrite says that it's okay to overwrite a file that already exists

pyfits.PrimaryHDU(avg).writeto("ngc7793_blue_avg.fits", overwrite = True)
pyfits.PrimaryHDU(median).writeto("ngc7793_blue_median.fits", overwrite = True)





# ALIGNING
# I want to find the maximum point for one group of color images and align them automatically
# I chose to align my images to my green averaged stack

single_file = pyfits.open("ngc7793_blue_avg.fits")
align_image_data = single_file[0].data


# AUTO-ALIGNING
# The align coordinates are the coordinates for the max pixel for my green averaged frames
y_align,x_align = numpy.unravel_index(align_image_data.argmax(),align_image_data.shape)
# print x_align
# print y_align
# print align_image_data[y_align,x_align]


# We can find the initial coordinates for the max pixel for the other two color averaged frames
y,x = numpy.unravel_index(avg.argmax(),avg.shape)
# print x
# print y


# Auto shift to align the maximum pixels
avg_x = numpy.roll(avg,x_align-x,axis=1)
avg_aligned = numpy.roll(avg_x,y_align-y,axis=0)
# print avg_x
# print avg_y





# MANUAL ALIGNING
# For the sample data I manually determined how much I needed to shift my images
# From ds9 I found the number of pixels I needed to shift my images
# axis=1 is the x axis and axis=0 is the y axis

# Shift red
   #avg_redx = numpy.roll(avg,2,axis=1)
# print avg_redx
   #avg_red_aligned = numpy.roll(avg_redx,14,axis=0)
# print avg_redy

# Shift blue
# avg_bluex = numpy.roll(avg,-13,axis=1)
# avg_blue_aligned = numpy.roll(avg_bluex,-2,axis=0)





# Finally we want to write out avg aligned to a file
# overwrite says that it's okay to overwrite a file that already exists

pyfits.PrimaryHDU(avg_aligned).writeto("ngc7793_blue_auto_aligned_avg.fits", overwrite = True)
