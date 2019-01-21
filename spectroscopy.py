import math
import numpy
import datetime
import matplotlib.pyplot as plt
import sys
import astropy.io.fits as pyfits
import os
import glob




# Command line argument is the following:
# bias_*.fits image_Spectroscopy_*.fits

# * represents a wildcard and tells it to open all files named image_Spectroscopy_...

# In command line, you put python filename.py bias.fits ...
# If fits files in file put file/ before .fits in command line

# sys.argv prints the arguments from the command line
# print sys.argv
# the first term, sys.argv[0] is the filename





# Since our bias/spectrum have varying file names we need to introduce glob
# The glob command allows Windows to look for varying filenames

# Define our arguments
bias_list = glob.glob(sys.argv[1])
# print bias

wavelength_calibration = sys.argv[2]
wavelength_data = pyfits.open(wavelength_calibration)[0].data
# print wavelength_calibration

image_list = glob.glob(sys.argv[-1])
# print image_list





# First we need to median combine the bias files
# From fits files we can load the data using pyfits.open[0].data

bias_stack = []

for file in bias_list:
    bias_data = pyfits.open(file)[0].data
    # print bias_data

    # We need to append our images to the empty array    
    bias_stack.append(bias_data)


# Take the mean/median of the stack to get one array per color
# Take the mean/median along the depth of the array = axis=0

bias_median = numpy.median(bias_stack,axis=0)
# print bias_median





# Calibrate spectrum with biases

image_stack = []

for file in image_list:
    image_data = pyfits.open(file)[0].data
    # print image_data

    # Subtract the median bias
    calibrated = image_data - bias_median
    # print calibrated

    # We need to append our images to the empty array
    image_stack.append(calibrated)


# Take the mean/median of the stack to get one array per color
# Take the mean/median along the depth of the array = axis=0

calibrated_median = numpy.median(image_stack,axis=0)
print(calibrated_median.shape)
# print calibrated_median
# print calibrated_median[0]
# print calibrated_median[520,1354]

# pyfits.PrimaryHDU(calibrated_median).writeto("Median_Spectrum.fits", clobber = True)





spectrum = calibrated_median[ range(513,524), ]
# print spectrum


#max_x = numpy.arange(1500)
max_x = range(1,1501)
max_y = []
#print max_x

for n in range(0,1500):
    # print n
    # print spectrum.max(axis=0)[n]

    max_position = spectrum.argmax(axis=0)[n] + 513.0
    # print max_position

    max_y.append(max_position)


# print max_x
# print max_y

plt.scatter(max_x,max_y)
# plt.show


coeffs = numpy.polyfit(max_x,max_y,3)
# print coeffs

fit_function = numpy.poly1d(coeffs)
max_y = fit_function(max_x)
plt.plot(max_x,max_y)
plt.xlabel("X Position")
plt.ylabel("Max Y Position")
plt.title("Measured Positions of Max Light with Polynomial")
plt.show()





background = calibrated_median[ range(913,924), ]
# print background


background_max_x = numpy.arange(1500)
# background_max_x = range(1,1501)
background_max_y = []
#print background_max_x

for n in range(0,1500):
    # print n
    # print background.max(axis=0)[n]

    background_max_position = background.argmax(axis=0)[n] + 913.0
    # print background_max_position

    background_max_y.append(background_max_position)


# print background_max_x
# print background_max_y

plt.scatter(background_max_x,background_max_y)
# plt.show


background_coeffs = numpy.polyfit(background_max_x,background_max_y,3)
# print background_coeffs

fit_function = numpy.poly1d(background_coeffs)
background_max_y = fit_function(background_max_x)
plt.plot(background_max_x,background_max_y)
plt.xlabel("Background X Position")
plt.ylabel("Background Max Y Position")
plt.title("Measured Positions of Max Background Light with Polynomial")
plt.show()




x_values = numpy.arange(1500)
# print x_values
spectrum = []

# print calibrated_median[max_y[0]]
# print calibrated_median[max_y[0] - 2.0]

for n in range(0,1500):
    spectrum_alone = calibrated_median[int(max_y[n] - 2.0),n] + calibrated_median[int(max_y[n] - 1.0),n] + calibrated_median[int(max_y[n]),n] + calibrated_median[int(max_y[n] + 1.0),n] + calibrated_median[int(max_y[n] + 2.0),n]
    # print spectrum_total

    spectrum.append(spectrum_alone)
  

plt.plot(x_values,spectrum)
plt.xlabel("X Pixel Value")
plt.ylabel("Total Light")
plt.title("Light in Spectrum w/o Background Calibration")
plt.show()





x_values = numpy.arange(1500)
# print x_values
spectrum_minus_background = []

# print calibrated_median[max_y[0]]
# print calibrated_median[max_y[0] - 2.0]

for n in range(0,1500):
    spectrum_total = calibrated_median[int(max_y[n] - 2.0),n] + calibrated_median[int(max_y[n] - 1.0),n] + calibrated_median[int(max_y[n]),n] + calibrated_median[int(max_y[n] + 1.0),n] + calibrated_median[int(max_y[n] + 2.0),n] - calibrated_median[int(background_max_y[n] - 2.0),n] - calibrated_median[int(background_max_y[n] - 1.0),n] - calibrated_median[int(background_max_y[n]),n] - calibrated_median[int(background_max_y[n] + 1.0),n] - calibrated_median[int(background_max_y[n] + 2.0),n]
    # print spectrum_total

    spectrum_minus_background.append(spectrum_total)
    

plt.plot(x_values,spectrum_minus_background)
plt.xlabel("X Pixel Value")
plt.ylabel("Total Light")
plt.title("Light in Spectrum w/ Background Calibration")
plt.show()





wavelength_spectrum = wavelength_data[ range(513,524), ]
# print wavelength_spectrum


wavelength_max_x = numpy.arange(1500)
wavelength_max_y = []
#print wavelength_max_x

for n in range(0,1500):
    # print n
    # print wavelength_spectrum.max(axis=0)[n]

    wavelength_max_position = wavelength_spectrum.argmax(axis=0)[n] + 513.0
    # print max_position

    wavelength_max_y.append(wavelength_max_position)


# print max_x
# print max_y

plt.plot(wavelength_max_x,wavelength_max_y)
# plt.show()


# coeffs = numpy.polyfit(max_x,max_y,3)
# print coeffs

# fit_function = numpy.poly1d(coeffs)
wavelength_max_y = fit_function(wavelength_max_x)
# plt.plot(wavelength_max_x,wavelength_max_y)
# plt.xlabel("X Position")
# plt.ylabel("Max Y Position")
# plt.title("Wavelength Calibration with Polynomial")
# plt.show()





x_values = numpy.arange(1500)
# print x_values
wavelength_spectrum = []


for n in range(0,1500):
    wavelength_spectrum_total = wavelength_data[int(wavelength_max_y[n] - 2.0),n] + wavelength_data[int(wavelength_max_y[n] - 1.0),n] + wavelength_data[int(wavelength_max_y[n]),n] + wavelength_data[int(wavelength_max_y[n] + 1.0),n] + wavelength_data[int(wavelength_max_y[n] + 2.0),n]
    # print wavelength_spectrum_total

    #wavelength_spectrum_log = math.log10(wavelength_spectrum_total)

    wavelength_spectrum.append(wavelength_spectrum_total)
    

plt.plot(x_values,wavelength_spectrum)
#plt.yscale('log')
plt.xlabel("X Pixel Value")
plt.ylabel("Total Light")
plt.title("Wavelength Spectrum")
plt.show()


# Need the location of max peak
#peak_wavelength_spectrum = max(wavelength_spectrum)
#print peak_wavelength_spectrum
#peak_wavelength_spectrum_location = wavelength_spectrum.index(peak_wavelength_spectrum)
#print peak_wavelength_spectrum_location




# Need to fit polynomial to wavelength spectrum
wavelength_x = [172.6,726.7,881.9,894.5,1489.8]
wavelength = [435.83,546.07,576.9,579.06,696.54]

wavelength_coeffs = numpy.polyfit(wavelength_x, wavelength, 2)
wavelength_fit_function = numpy.poly1d(wavelength_coeffs)

x_to_wavelength = wavelength_fit_function(x_values)



plt.plot(x_to_wavelength,spectrum_minus_background)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.title("Final Spectrum")
plt.show()


# Need the location of max peak to see how much it shifts by
peak_spectrum = max(spectrum_minus_background)
print(peak_spectrum)
peak_spectrum_location = wavelength_fit_function(spectrum_minus_background.index(peak_spectrum))
print(peak_spectrum_location)


# Redshift
redshift = (peak_spectrum_location - 656.281)/656.281
print(redshift)


def redshift(spectrum_minus_background):
    peak_spectrum = max(spectrum_minus_background)
    peak_spectrum_location = wavelength_fit_function(spectrum_minus_background.index(peak_spectrum))
    return (peak_spectrum_location - 656.281)/656.281

print("Redshift", redshift(spectrum_minus_background))

peak_spectrum_location = 670.052
peak_spectrum_error = 1.0    


redshifts = []

for trials in range(0,1000000):
    test_peak_location = numpy.random.normal(peak_spectrum_location,peak_spectrum_error)
    test_redshift = (test_peak_location - 656.281)/656.281
    
    redshifts.append(test_redshift)

n, bins, patches = plt.hist(redshifts, 50, normed=1)
plt.xlabel("Redshift")
plt.ylabel("Prob.")
plt.title("Redshift Error")
plt.show()













# To find the rotation curve of the galaxy I need to pull the spectrum from various places

spectrum_two = calibrated_median[ range(200,211), ]
# print spectrum


#max_x = numpy.arange(1500)
two_x = range(1,1501)
two_y = []
#print max_x

for n in range(0,1500):
    # print n
    # print spectrum.max(axis=0)[n]

    two_position = spectrum_two.argmax(axis=0)[n] + 200.0
    # print max_position

    two_y.append(two_position)


# print max_x
# print max_y

#plt.scatter(two_x,two_y)
# plt.show


two_coeffs = numpy.polyfit(two_x,two_y,3)
# print coeffs

fit_function = numpy.poly1d(two_coeffs)
two_y = fit_function(two_x)
#plt.plot(two_x,two_y)
#plt.xlabel("X Position")
#plt.ylabel("Max Y Position")
#plt.title("Measured Positions of Max Light with Polynomial")
#plt.show()



x_values = numpy.arange(1500)
# print x_values
spectrum_twohundred = []

# print calibrated_median[max_y[0]]
# print calibrated_median[max_y[0] - 2.0]

for n in range(0,1500):
    spectrum_two = calibrated_median[int(two_y[n] - 2.0),n] + calibrated_median[int(two_y[n] - 1.0),n] + calibrated_median[int(two_y[n]),n] + calibrated_median[int(two_y[n] + 1.0),n] + calibrated_median[int(two_y[n] + 2.0),n]
    # print spectrum_total

    spectrum_twohundred.append(spectrum_two)
  

plt.plot(x_values,spectrum_twohundred)
plt.xlabel("X Pixel Value")
plt.ylabel("Total Light")
plt.title("Light in Spectrum w/o Background Calibration")
plt.show()

peak_spectrum = max(spectrum_twohundred)
#print spectrum_twohundred[1355]
peak_spectrum_location = wavelength_fit_function(spectrum_twohundred.index(peak_spectrum))
#peak_spectrum_location = wavelength_fit_function(spectrum_twohundred[1355])

print(peak_spectrum_location)

plt.plot(x_to_wavelength,spectrum_twohundred)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.title("200 Slice Final Spectrum")
plt.show()






spectrum_four = calibrated_median[ range(400,411), ]
# print spectrum


#max_x = numpy.arange(1500)
four_x = range(1,1501)
four_y = []
#print max_x

for n in range(0,1500):
    # print n
    # print spectrum.max(axis=0)[n]

    four_position = spectrum_four.argmax(axis=0)[n] + 400.0
    # print max_position

    four_y.append(four_position)


# print max_x
# print max_y

#plt.scatter(four_x,four_y)
# plt.show


four_coeffs = numpy.polyfit(four_x,four_y,3)
# print coeffs

fit_function = numpy.poly1d(four_coeffs)
four_y = fit_function(four_x)
#plt.plot(six_x,six_y)
#plt.xlabel("X Position")
#plt.ylabel("Max Y Position")
#plt.title("Measured Positions of Max Light with Polynomial")
#plt.show()



x_values = numpy.arange(1500)
# print x_values
spectrum_fourhundred = []

# print calibrated_median[max_y[0]]
# print calibrated_median[max_y[0] - 2.0]

for n in range(0,1500):
    spectrum_four = calibrated_median[int(four_y[n] - 2.0),n] + calibrated_median[int(four_y[n] - 1.0),n] + calibrated_median[int(four_y[n]),n] + calibrated_median[int(four_y[n] + 1.0),n] + calibrated_median[int(four_y[n] + 2.0),n]
    # print spectrum_total

    spectrum_fourhundred.append(spectrum_four)
  

plt.plot(x_values,spectrum_fourhundred)
plt.xlabel("X Pixel Value")
plt.ylabel("Total Light")
plt.title("Light in Spectrum w/o Background Calibration")
plt.show()

peak_spectrum = max(spectrum_fourhundred)
#print spectrum_fourhundred[1355]
peak_spectrum_location = wavelength_fit_function(spectrum_fourhundred.index(peak_spectrum))
#peak_spectrum_location = wavelength_fit_function(spectrum_twohundred[1355])

print(peak_spectrum_location)

plt.plot(x_to_wavelength,spectrum_fourhundred)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.title("400 Slice Final Spectrum")
plt.show()















spectrum_six = calibrated_median[ range(600,611), ]
# print spectrum


#max_x = numpy.arange(1500)
six_x = range(1,1501)
six_y = []
#print max_x

for n in range(0,1500):
    # print n
    # print spectrum.max(axis=0)[n]

    six_position = spectrum_six.argmax(axis=0)[n] + 600.0
    # print max_position

    six_y.append(six_position)


# print max_x
# print max_y

#plt.scatter(six_x,six_y)
# plt.show


six_coeffs = numpy.polyfit(six_x,six_y,3)
# print coeffs

fit_function = numpy.poly1d(six_coeffs)
six_y = fit_function(six_x)
#plt.plot(six_x,six_y)
#plt.xlabel("X Position")
#plt.ylabel("Max Y Position")
#plt.title("Measured Positions of Max Light with Polynomial")
#plt.show()



x_values = numpy.arange(1500)
# print x_values
spectrum_sixhundred = []

# print calibrated_median[max_y[0]]
# print calibrated_median[max_y[0] - 2.0]

for n in range(0,1500):
    spectrum_six = calibrated_median[int(six_y[n] - 2.0),n] + calibrated_median[int(six_y[n] - 1.0),n] + calibrated_median[int(six_y[n]),n] + calibrated_median[int(six_y[n] + 1.0),n] + calibrated_median[int(six_y[n] + 2.0),n]
    # print spectrum_total

    spectrum_sixhundred.append(spectrum_six)
  

plt.plot(x_values,spectrum_sixhundred)
plt.xlabel("X Pixel Value")
plt.ylabel("Total Light")
plt.title("Light in Spectrum w/o Background Calibration")
plt.show()

peak_spectrum = max(spectrum_sixhundred)
#print spectrum_sixhundred[1355]
peak_spectrum_location = wavelength_fit_function(spectrum_sixhundred.index(peak_spectrum))
#peak_spectrum_location = wavelength_fit_function(spectrum_twohundred[1355])

print(peak_spectrum_location)

plt.plot(x_to_wavelength,spectrum_sixhundred)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.title("600 Slice Final Spectrum")
plt.show()


