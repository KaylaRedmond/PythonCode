import math
import numpy
import datetime
import matplotlib.pyplot as plt
import sys
import astropy.io.fits as pyfits
import os
import glob





# Fits files contain multiple frames of a single image
hd73871 = pyfits.open("HD73871.fits")
# print hip19849

# Number of frames is the length of the fits file
# print len(hip19849)

# first image is the zeroth item
first_image = hd73871[0].data #.shape gives you length
print (hd73871[0].header)
# print first_image

# second image is the first item
second_image = hd73871[1].data
# print second_image

# You can add the frames together
# print first_image + second_image





# Create open array then append the data from each frame to the array

frame_stack = []

for i in range(len(hd73871)):
    fits_frames = hd73871[i].data
    frame_stack.append(fits_frames)

    # print frame_stack





# Add the frames together

added_frames = numpy.sum(frame_stack,axis=0)
# print added_frames

pyfits.PrimaryHDU(added_frames).writeto("hd73871_added_frames.fits", overwrite = True)





# Find the brightest pixel for the added frames
y_max,x_max = numpy.unravel_index(added_frames.argmax(),added_frames.shape)
print (added_frames[y_max,x_max])

# Find total light for all frames
total_pixels = numpy.sum(added_frames)
print (total_pixels)

# Strehl ratio for the added frames
strehl_ratio = (added_frames[y_max,x_max] / total_pixels)/.015
print (strehl_ratio)





strehl_array = []

# Strehl ratio for each frame
for i in range(len(hd73871)):
    fits_frames = hd73871[i].data

    maximum_per_image = numpy.amax(fits_frames)
    # print maximum_per_image

    total_pixels_per_frame = numpy.sum(fits_frames)
    # print total_pixels_per_frame
    
    strehl_ratio_per_image = (maximum_per_image / total_pixels_per_frame)/.015
    # print strehl_ratio_per_image

    strehl_array.append(strehl_ratio_per_image)


# Create histogram of all the Strehl ratios
plt.hist(strehl_array, bins=10)
plt.xlabel("Strehl Ratio")
plt.ylabel("Count")
plt.title("HD73871")
plt.show()





# Measure the brightest pixel and automatically align them

# Align them to one image
align_image_data = hd73871[0].data
y_align,x_align = numpy.unravel_index(align_image_data.argmax(),align_image_data.shape)
# print x_align
# print y_align
# print align_image_data[y_align,x_align]





brightest_pixel = []

for i in range(len(hd73871)):
    fits_frames = hd73871[i].data

    # Maximum per frame
    maximum_per_image = numpy.amax(fits_frames)

    # Axis are switched in ds9
    # Initial coordinates for max pixel for each frame
    y_max,x_max = numpy.unravel_index(fits_frames.argmax(),fits_frames.shape)
    # print x_max
    # print y_max
    # print fits_frames[y_max,x_max]

    # Roll each image so the max pixel coordinates to the 'aligned' max pixel
    frame_data_aligned_x = numpy.roll(fits_frames,int(x_align-x_max),axis=1)
    frame_data_aligned_total = numpy.roll(frame_data_aligned_x,int(y_align-y_max),axis=0)
    # print frame_data_aligned_total    

    # Check that all of the frames have the same coordinates for max pixel
    y_aligned,x_aligned = numpy.unravel_index(frame_data_aligned_total.argmax(),frame_data_aligned_total.shape)
    # print x_aligned
    # print y_aligned
    # print frame_data_aligned_total[y_aligned,x_aligned]

    brightest_pixel.append(frame_data_aligned_total)





added_brightest_pixel_frames = numpy.sum(brightest_pixel,axis=0)

pyfits.PrimaryHDU(added_brightest_pixel_frames).writeto("hd73871_aligned_added_frames.fits", overwrite = True)





# Find the brightest pixel for the aligned added frames
y_max,x_max = numpy.unravel_index(added_brightest_pixel_frames.argmax(),added_brightest_pixel_frames.shape)
print (added_brightest_pixel_frames[y_max,x_max])

# Find total light
total_pixels = numpy.sum(added_brightest_pixel_frames)
print (total_pixels)

# Strehl ratio for aligned added frames
strehl_ratio = (added_brightest_pixel_frames[y_max,x_max] / total_pixels)/.015
print (strehl_ratio)





# Keeping top 5% of Strehl ratio

strehl_array = []


for i in range(len(hd73871)):
    fits_frames = hd73871[i].data

    maximum_per_image = numpy.amax(fits_frames)
    # print maximum_per_image

    total_pixels_per_frame = numpy.sum(fits_frames)
    # print total_pixels_per_frame
    
    strehl_ratio_per_image = (maximum_per_image / total_pixels_per_frame)/.015
    # print strehl_ratio_per_image
    
    strehl_array.append(strehl_ratio_per_image) 

# print strehl_array

# Take strehl array and find the 95th percentile

strehl_95th = numpy.percentile(strehl_array,95)
print ("Strehl 95th percentile", strehl_95th)





# Make new strehl array that includes only top 5%
top_strehl_array = []

for i in range(len(hd73871)):
    fits_frames = hd73871[i].data

    # Maximum per frame
    maximum_per_image = numpy.amax(fits_frames)

    # Axis are switched in ds9
    # Initial coordinates for max pixel for each frame
    y_max,x_max = numpy.unravel_index(fits_frames.argmax(),fits_frames.shape)
    # print x_max
    # print y_max
    # print fits_frames[y_max,x_max]

    # Roll each image so the max pixel coordinates to the 'aligned' max pixel
    frame_data_aligned_x = numpy.roll(fits_frames,int(x_align-x_max),axis=1)
    frame_data_aligned_total = numpy.roll(frame_data_aligned_x,int(y_align-y_max),axis=0)
    # print frame_data_aligned_total    

    # Check that all of the frames have the same coordinates for max pixel
    y_aligned,x_aligned = numpy.unravel_index(frame_data_aligned_total.argmax(),frame_data_aligned_total.shape)
    # print x_aligned
    # print y_aligned
    # print frame_data_aligned_total[y_aligned,x_aligned]

    total_pixels_per_frame = numpy.sum(fits_frames)
    # print total_pixels_per_frame
    
    strehl_ratio_per_image = (maximum_per_image / total_pixels_per_frame)/.015
    # print strehl_ratio_per_image

    if strehl_ratio_per_image > strehl_95th:
        # print strehl_ratio_per_image
        
        # Then append the data for the top 5% into array
        top_strehl_array.append(frame_data_aligned_total)

# print top_strehl_array

top_percent_added_brightest_pixel_frames = numpy.sum(top_strehl_array,axis=0)

pyfits.PrimaryHDU(top_percent_added_brightest_pixel_frames).writeto("hd73871_top_5%_aligned_added_frames.fits", overwrite = True)





# Find the brightest pixel for the aligned added frames
y_max,x_max = numpy.unravel_index(top_percent_added_brightest_pixel_frames.argmax(),top_percent_added_brightest_pixel_frames.shape)
print (top_percent_added_brightest_pixel_frames[y_max,x_max])

# Find total light
total_pixels = numpy.sum(top_percent_added_brightest_pixel_frames)
print (total_pixels)

# Strehl ratio for aligned added frames
strehl_ratio = (top_percent_added_brightest_pixel_frames[y_max,x_max] / total_pixels)/.015
print (strehl_ratio)






#strehl_array = []

# Strehl ratio for each frame
#for i in range(len(hd73871)):
#    fits_frames = hd73871[i].data

#    maximum_per_image = numpy.amax(fits_frames)
    # print maximum_per_image

#    total_pixels_per_frame = numpy.sum(fits_frames)
    # print total_pixels_per_frame
    
#    strehl_ratio_per_image = (maximum_per_image / total_pixels_per_frame)/.015
    # print strehl_ratio_per_image

#average_strehl_ratio = numpy.average(strehl_ratio_per_image)
#print ("Average Strehl", average_strehl_ratio)


# Strehl ratio for each frame
#for i in range(len(hd73871)):
#    fits_frames = hd73871[i].data
   
#    maximum_per_image = numpy.amax(fits_frames)
    # print maximum_per_image

#    total_pixels_per_frame = numpy.sum(fits_frames)
    # print total_pixels_per_frame
    
#    strehl_ratio_per_image = (maximum_per_image / total_pixels_per_frame)/.015
    # print strehl_ratio_per_image

#    strehl = strehl_ratio_per_image - strehl_ratio_per_image

#    subtract = strehl_ratio_per_image - average_strehl_ratio
    #print subtract

    




