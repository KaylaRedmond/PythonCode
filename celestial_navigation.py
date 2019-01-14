import math
import numpy
import datetime
import matplotlib.pyplot as plt
import sys





# Command line argument is the following:
# year, month, day, obs_long, obs_lat, target_ra, target_dec

# In command line, you put python filename.py year month day ...

# sys.argv prints the arguments from the command line
# print sys.argv
# the first term, sys.argv[0] is the filename
# print sys.argv[1]

# Float function makes number as floating number with decimal points
# Floating number includes decimal so 1 is 1.0





# Define our variables as the float of the sys.argv to make numbers

year = float(sys.argv[1])
month = float(sys.argv[2])
day = float(sys.argv[3])
obs_long = float(sys.argv[4])
obs_lat = float(sys.argv[5])
target_ra = (sys.argv[6])
target_dec = (sys.argv[7])

# RA and Dec are HH:MM:SS and DD:MM:SS then we need to split into components

target_ra_split = target_ra.split(":")
target_dec_split = target_dec.split(":")
# print target_ra.split(":")
# print target_ra_split[0]





# Calculate Julian date from given: year, month, day
# int command gives us the integer of a number with no decimal points

JD = 367.0*year - int(7.0*(year+int((month+9.0)/12.0))/4.0) + int(275.0*month/9.0) + day + 1721013.5

# print "Julian Date", JD





# From Julian Date compute the Greenwich Sidereal Time

d = JD - 2451545.0
T = d/36525.0
GMST = 24110.54841 + 8640184.81266*T+ 0.093104*T**2.0 - 0.0000062*T**3.0

# print "Greenwich Sidereal Time", GMST(year,month,day), "seconds"

# GMST is in units of seconds, convert to hours, minutes, and seconds

GST_hours = int((GMST/86400.0 - int(GMST/86400.0))*24.0)
GST_minutes = int(((GMST/86400.0 - int(GMST/86400.0))*24.0 - GST_hours)*60.0)
GST_seconds = (((GMST/86400.0 - int(GMST/86400.0))*24.0 - GST_hours)*60.0 - GST_minutes)*60.0

# print "Greenwich Sidereal Time", GST_hours,":", GST_minutes, ":", GST_seconds





# Convert Observing Longitude to hours, minutes, and seconds

long_hours = int(obs_long/15.0)
long_minutes = int(((obs_long/15.0) - long_hours)*60.0)
long_seconds = ((obs_long/15.0) - long_hours)*60.0 - long_minutes

# print "Longitude", long_hours, "hours", long_minutes, "minutes", long_seconds, "seconds"





# Calculate Local Sidereal Time by adding Longitude to GST

LST_hours = GST_hours + long_hours
LST_minutes = GST_minutes + long_minutes
LST_seconds = GST_seconds + long_seconds

# print "LST", LST_hours,":",LST_minutes,":",LST_seconds





# Calculate Hour Angle by subtracting RA from LST

HA_hours = LST_hours - float(target_ra_split[0])
HA_minutes = LST_minutes - float(target_ra_split[1])
HA_seconds = LST_seconds - float(target_ra_split[2])

# print "HA", HA_hours,":",HA_minutes,":",HA_seconds





# Convert Hour Angle to degrees

HA_deg = HA_hours*15.0 + HA_minutes/4.0 + HA_seconds/240.0

# print "HA Degrees", HA_deg





# Convert Target Declination to degrees

target_dec_deg = float(target_dec_split[0]) + float(target_dec_split[1])/60.0 + float(target_dec_split[2])/3600.0

# print "Target Declination Degrees", target_dec_deg





# Calculate Altitude

altitude = math.asin(math.sin(math.radians(target_dec_deg))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg))*math.cos(math.radians(obs_lat))*math.cos(math.radians(HA_deg))) * 57.2957795

# print "Altitude Degrees", altitude





# Over 24 hours the Hour Angle = LST - RA changes
# LST changes by 360-.985647 degrees = 359.014 degrees
# RA changes by 3.94 minutes = .985 degrees due to sidereal time effects
# Hour Angle changes by a total of 358.029 degrees
# linspace constructs a list of the hour angles over 24 hours

HA_hour = numpy.linspace(HA_deg, HA_deg + 358.029, 25)

# print "Varying HA", HA_hour





# Vary Altitude over 24 Hours
# [] makes an empty list for the varying altitude
# numpy.nditer iterates through altitude for each of the hours in HA_hour
# append adds each altitude for each hour to the empty list

altitude_hour = []
for hour in numpy.nditer(HA_hour):
    altitude = math.asin(math.sin(math.radians(target_dec_deg))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg))*math.cos(math.radians(obs_lat))*math.cos(math.radians(hour))) * 57.2957795
    altitude_hour.append(altitude)

# print "Varying Altitude", altitude_hour





# Plot Hour vs. Altitude

hour = numpy.linspace(0,24,25)
plt.plot(hour,altitude_hour)
plt.xlabel("Hour")
plt.ylabel("Altitude")
plt.title("SOAR Telescope w/ Star RA 4:00:00 Dec 12:00:00")
plt.show()


