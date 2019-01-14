import math
import numpy
import datetime
import matplotlib.pyplot as plt
import sys
from tabulate import tabulate





# Command line argument is the following:
# year, month, day, obs_long, obs_lat

# In command line, you put python filename.py year month day ...

# sys.argv prints the arguments from the command line
# print sys.argv
# the first term, sys.argv[0] is the filename
# print sys.argv[1]

# Float function makes number as floating number with decimal points
# Floating number includes decimal so 1 is 1.0





# Input text file of stars
# open the textfile and read each line, and we strip an split each component

li = [i.strip().split() for i in open("Target_Altitudes.txt").readlines()]

# print li
# print li[2][1]





# Define our variables as the float of the sys.argv to make numbers

year = float(sys.argv[1])
month = float(sys.argv[2])
day = float(sys.argv[3])
obs_long = float(sys.argv[4])
obs_lat = float(sys.argv[5])

target_ra_1 = li[0][1]
target_dec_1 = li[0][2]
target_ra_2 = li[1][1]
target_dec_2 = li[1][2]
target_ra_3 = li[2][1]
target_dec_3 = li[2][2]
target_ra_4 = li[3][1]
target_dec_4 = li[3][2]
target_ra_5 = li[4][1]
target_dec_5 = li[4][2]

# RA and Dec are HH:MM:SS and DD:MM:SS then we need to split into components

target_ra_split_1 = target_ra_1.split(":")
target_dec_split_1 = target_dec_1.split(":")
target_ra_split_2 = target_ra_2.split(":")
target_dec_split_2 = target_dec_2.split(":")
target_ra_split_3 = target_ra_3.split(":")
target_dec_split_3 = target_dec_3.split(":")
target_ra_split_4 = target_ra_4.split(":")
target_dec_split_4 = target_dec_4.split(":")
target_ra_split_5 = target_ra_5.split(":")
target_dec_split_5 = target_dec_5.split(":")
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

HA_hours_1 = LST_hours - float(target_ra_split_1[0])
HA_minutes_1 = LST_minutes - float(target_ra_split_1[1])
HA_seconds_1 = LST_seconds - float(target_ra_split_1[2])
HA_hours_2 = LST_hours - float(target_ra_split_2[0])
HA_minutes_2 = LST_minutes - float(target_ra_split_2[1])
HA_seconds_2 = LST_seconds - float(target_ra_split_2[2])
HA_hours_3 = LST_hours - float(target_ra_split_3[0])
HA_minutes_3 = LST_minutes - float(target_ra_split_3[1])
HA_seconds_3 = LST_seconds - float(target_ra_split_3[2])
HA_hours_4 = LST_hours - float(target_ra_split_4[0])
HA_minutes_4 = LST_minutes - float(target_ra_split_4[1])
HA_seconds_4 = LST_seconds - float(target_ra_split_4[2])
HA_hours_5 = LST_hours - float(target_ra_split_5[0])
HA_minutes_5 = LST_minutes - float(target_ra_split_5[1])
HA_seconds_5 = LST_seconds - float(target_ra_split_5[2])

# print "HA 1", HA_hours_1,":",HA_minutes_1,":",HA_seconds_1





# Convert Hour Angle to degrees

HA_deg_1 = HA_hours_1*15.0 + HA_minutes_1/4.0 + HA_seconds_1/240.0
HA_deg_2 = HA_hours_2*15.0 + HA_minutes_2/4.0 + HA_seconds_2/240.0
HA_deg_3 = HA_hours_3*15.0 + HA_minutes_3/4.0 + HA_seconds_3/240.0
HA_deg_4 = HA_hours_4*15.0 + HA_minutes_4/4.0 + HA_seconds_4/240.0
HA_deg_5 = HA_hours_5*15.0 + HA_minutes_5/4.0 + HA_seconds_5/240.0

# print "HA 1 Degrees", HA_deg_1





# Convert Target Declination to degrees

target_dec_deg_1 = float(target_dec_split_1[0]) + float(target_dec_split_1[1])/60.0 + float(target_dec_split_1[2])/3600.0
target_dec_deg_2 = float(target_dec_split_2[0]) + float(target_dec_split_2[1])/60.0 + float(target_dec_split_2[2])/3600.0
target_dec_deg_3 = float(target_dec_split_3[0]) + float(target_dec_split_3[1])/60.0 + float(target_dec_split_3[2])/3600.0
target_dec_deg_4 = float(target_dec_split_4[0]) + float(target_dec_split_4[1])/60.0 + float(target_dec_split_4[2])/3600.0
target_dec_deg_5 = float(target_dec_split_5[0]) + float(target_dec_split_5[1])/60.0 + float(target_dec_split_5[2])/3600.0

# print "Target 1 Declination Degrees", target_dec_deg_1





# Calculate Altitude

altitude_1 = math.asin(math.sin(math.radians(target_dec_deg_1))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_1))*math.cos(math.radians(obs_lat))*math.cos(math.radians(HA_deg_1))) * 57.2957795
altitude_2 = math.asin(math.sin(math.radians(target_dec_deg_2))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_2))*math.cos(math.radians(obs_lat))*math.cos(math.radians(HA_deg_2))) * 57.2957795
altitude_3 = math.asin(math.sin(math.radians(target_dec_deg_3))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_3))*math.cos(math.radians(obs_lat))*math.cos(math.radians(HA_deg_3))) * 57.2957795
altitude_4 = math.asin(math.sin(math.radians(target_dec_deg_4))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_4))*math.cos(math.radians(obs_lat))*math.cos(math.radians(HA_deg_4))) * 57.2957795
altitude_5 = math.asin(math.sin(math.radians(target_dec_deg_5))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_5))*math.cos(math.radians(obs_lat))*math.cos(math.radians(HA_deg_5))) * 57.2957795

# print "Altitude 1 Degrees", altitude_1





# Over 24 hours the Hour Angle = LST - RA changes
# LST changes by 360-.985647 degrees = 359.014 degrees
# RA changes by 3.94 minutes = .985 degrees due to sidereal time effects
# Hour Angle changes by a total of 358.029 degrees
# linspace constructs a list of the hour angles over 24 hours

HA_hour_1 = numpy.linspace(HA_deg_1, HA_deg_1 + 358.029, 25)
HA_hour_2 = numpy.linspace(HA_deg_2, HA_deg_2 + 358.029, 25)
HA_hour_3 = numpy.linspace(HA_deg_3, HA_deg_3 + 358.029, 25)
HA_hour_4 = numpy.linspace(HA_deg_4, HA_deg_4 + 358.029, 25)
HA_hour_5 = numpy.linspace(HA_deg_5, HA_deg_5 + 358.029, 25)

# print "Varying HA 1", HA_hour_1





# Vary Altitude over 24 Hours
# [] makes an empty list for the varying altitude
# numpy.nditer iterates through altitude for each of the hours in HA_hour
# append adds each altitude for each hour to the empty list

altitude_hour_1 = []
for hour in numpy.nditer(HA_hour_1):
    altitude_1 = math.asin(math.sin(math.radians(target_dec_deg_1))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_1))*math.cos(math.radians(obs_lat))*math.cos(math.radians(hour))) * 57.2957795
    altitude_hour_1.append(altitude_1)

# print "Altitude Target 1 over Hours", altitude_hour_1

altitude_hour_2 = []
for hour in numpy.nditer(HA_hour_2):
    altitude_2 = math.asin(math.sin(math.radians(target_dec_deg_2))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_2))*math.cos(math.radians(obs_lat))*math.cos(math.radians(hour))) * 57.2957795
    altitude_hour_2.append(altitude_2)


altitude_hour_3 = []
for hour in numpy.nditer(HA_hour_3):
    altitude_3 = math.asin(math.sin(math.radians(target_dec_deg_3))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_3))*math.cos(math.radians(obs_lat))*math.cos(math.radians(hour))) * 57.2957795
    altitude_hour_3.append(altitude_3)


altitude_hour_4 = []
for hour in numpy.nditer(HA_hour_4):
    altitude_4 = math.asin(math.sin(math.radians(target_dec_deg_4))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_4))*math.cos(math.radians(obs_lat))*math.cos(math.radians(hour))) * 57.2957795
    altitude_hour_4.append(altitude_4)


altitude_hour_5 = []
for hour in numpy.nditer(HA_hour_5):
    altitude_5 = math.asin(math.sin(math.radians(target_dec_deg_5))*math.sin(math.radians(obs_lat)) + math.cos(math.radians(target_dec_deg_5))*math.cos(math.radians(obs_lat))*math.cos(math.radians(hour))) * 57.2957795
    altitude_hour_5.append(altitude_5)





# Zenith Angle is 90 degrees - altitude

zenith_angle_1 = numpy.zeros(25) + 90.0 - altitude_hour_1
zenith_angle_2 = numpy.zeros(25) + 90.0 - altitude_hour_2
zenith_angle_3 = numpy.zeros(25) + 90.0 - altitude_hour_3
zenith_angle_4 = numpy.zeros(25) + 90.0 - altitude_hour_4
zenith_angle_5 = numpy.zeros(25) + 90.0 - altitude_hour_5

# print "Varying Zenith Angle 1", zenith_angle_1





# Calculate Airmass

airmass_1 = numpy.array([abs(1/math.cos(math.radians(a))) for a in zenith_angle_1])
airmass_2 = numpy.array([abs(1/math.cos(math.radians(a))) for a in zenith_angle_2])
airmass_3 = numpy.array([abs(1/math.cos(math.radians(a))) for a in zenith_angle_3])
airmass_4 = numpy.array([abs(1/math.cos(math.radians(a))) for a in zenith_angle_4])
airmass_5 = numpy.array([abs(1/math.cos(math.radians(a))) for a in zenith_angle_5])

# print "Airmass Target1", airmass_1
# print "Airmass Target2", airmass_2
# print "Airmass Target3", airmass_3
# print "Airmass Target4", airmass_4
# print "Airmass Target5", airmass_5

table_target2 = [["Target2", "airmass"],[0,4.78],[1,4.31],[2,3.67],[3,3.06],[4,2.55],[5,2.16],[18,2.27],[19,2.69],[20,3.24],[21,3.87],[22,4.48],[23,4.86],[24,4.82]]
# print tabulate(table_target2)

table_target4 = [["Target4","airmass"],[0,20.47],[1,73.38],[2,11.31],[3,5.87],[4,3.93],[5,2.99],[6,2.47],[7,2.17],[8,2.00],[11,2.05],[12,2.25],[13,2.62],[14,3.24],[15,4.42],[16,7.00],[17,15.98],[18,115.55],[19,15.13],[20,9.44],[21,7.98],[22,8.12],[23,10.05],[24,17.87]]
# print tabulate(table_target4)

table_target5 = [["Target5","airmass"],[6,2.12],[7,2.24],[8,2.28],[9,2.25],[10,2.15]]
# print tabulate(table_target5)





# Plot Hour vs. Altitude

hour = numpy.linspace(0,24,25)
plt.plot(hour,altitude_hour_1)
plt.plot(hour,altitude_hour_2)
plt.plot(hour,altitude_hour_3)
plt.plot(hour,altitude_hour_4)
plt.plot(hour,altitude_hour_5)
plt.text(-12,-0,tabulate(table_target2),fontsize=8)
plt.text(-20,-80,tabulate(table_target4),fontsize=8)
plt.text(-12,-80,tabulate(table_target5),fontsize=8)


plt.xlabel("Hour")
plt.ylabel("Altitude")
plt.title("SOAR Telescope")
plt.legend(["Target1","Target2","Target3","Target4","Target5"],loc="upper left")
plt.subplots_adjust(left=0.4)
plt.show()


