import math
import numpy
import datetime
import matplotlib.pyplot as plt
import sys
import astropy.io.fits as pyfits
import os
import glob





# Command line argument is the following:
# diameter (m), exposure (min), throughput, airmass, magnitude, pixel scale (arcsec), number of pixels, % light pixels

# In command line, you put python filename.py diameter, exposure ...

# sys.argv prints the arguments from the command line
# print sys.argv

# the first term, sys.argv[0] is the filename
# print sys.argv[1]





# Define our variables as the float of the sys.argv to make numbers

diameter_meters = float(sys.argv[1])
exposure_minutes = float(sys.argv[2])
throughput = float(sys.argv[3])
airmass = float(sys.argv[4])
magnitude_source = float(sys.argv[5])
pixel_scale = float(sys.argv[6])
pixel_area = float(sys.argv[7])
pixel_fraction = float(sys.argv[8])

quantum_efficiency = float(sys.argv[9])
dark_current = float(sys.argv[10])
readout_noise = float(sys.argv[11])




# Area of telescope in cm
telescope_area = (math.pi) * ((diameter_meters*100.0/2.0)**2.0)
print ("Telescope Area", telescope_area)


# Exposure in seconds
exposure_seconds = exposure_minutes * 60.0
print ("Exposure seconds", exposure_seconds)


# Extinction (in magnitudes) due to airmass
extinction = .2 * airmass
print ("Extinction", extinction)


# Corrected magnitude due to extinction
magnitude = magnitude_source + extinction
print ("Corrected Magnitude", magnitude)


# Number of Photons for Magnitude 0 Star
photons_magnitude_0 = 1000.0*exposure_seconds*880.0*telescope_area
print ("Mag 0 Photons", photons_magnitude_0)


# Number of Photons for Source Star
number_photons = photons_magnitude_0 * (10**(-magnitude/2.5))
print ("Source Photons", number_photons)

print ("Source Photons per pixel", number_photons/pixel_area)


# Signal
signal = number_photons * throughput * pixel_fraction
print ("Signal", signal)





# Background Photons
background_photons = throughput*(photons_magnitude_0 * (10**(-21.9/2.5)))*(pixel_scale ** 2.0)*pixel_area
print ("Background Photons", background_photons)


# Noise
noise = (signal + background_photons)**(.5)
print ("Noise", noise)





# Signal to Noise Ratio
print ("Signal / Noise", signal/noise)





# Updated Signal
updated_signal = signal * quantum_efficiency
print ("Updated Signal", updated_signal)


# Updated Noise
updated_noise = (updated_signal + quantum_efficiency*background_photons + pixel_area*(dark_current*exposure_seconds)+pixel_area*(readout_noise**2.0))**(.5)
print ("Updated Noise", updated_noise)





# Updated Signal to Noise Ratio
print ("Updated Signal / Noise", updated_signal/updated_noise)



