import math
import numpy
import datetime
import matplotlib.pyplot as plt
import sys
import astropy.io.fits as pyfits
import os
import glob





# Event List
event_list = pyfits.open('XRay/acisf10137N002_evt2.fits')[1].data
print(pyfits.open('XRay/acisf12075N003_evt2.fits')[0].header)
# print event_list

# X coordinates of event
x_data = event_list['x']
# print x_data

# Y coordinates of event
y_data = event_list['y']
# print y_data





# Need to round the pixel coordinates and make image smaller by factor of 4
x_fourth_data = x_data/4
# print x_fourth_data

x_rounded_data = [round(elem) for elem in x_fourth_data]
# print x_rounded_data[0]


y_fourth_data = y_data/4
# print y_fourth_data

y_rounded_data = [round(elem) for elem in y_fourth_data]
# print y_rounded_data[0]

# print y_rounded_data[0],x_rounded_data[0]





#print len(y_rounded_data)
#print len(x_rounded_data)


  


# Size of image
image_y_size = int(max(y_rounded_data))
# print image_y_size

image_x_size = int(max(x_rounded_data))
# print image_x_size


# Make blank image
image = numpy.zeros((image_x_size+1,image_y_size+1))

for i in range(0,len(x_rounded_data)):
    # print i
    x_location = int(x_rounded_data[i])
    # print x_location
    y_location = int(y_rounded_data[i])
    # print y_location
    image[x_location][y_location] = image[x_location][y_location] + 1
    print(image[x_location][y_location])





pyfits.PrimaryHDU(image).writeto("XRay/10135_obs_all_events.fits",overwrite = True)





# Event List
event_list = pyfits.open('XRay/acisf10135N003_evt2.fits')[1].data
# print event_list

# X coordinates of event
x_data = event_list['x']
# print x_data

# Y coordinates of event
y_data = event_list['y']
# print y_data





# Need to round the pixel coordinates and make image smaller by factor of 4
x_fourth_data = x_data/4
# print x_fourth_data

x_rounded_data = [round(elem) for elem in x_fourth_data]
# print x_rounded_data[0]


y_fourth_data = y_data/4
# print y_fourth_data

y_rounded_data = [round(elem) for elem in y_fourth_data]
# print y_rounded_data[0]

# print y_rounded_data[0],x_rounded_data[0]





#print len(y_rounded_data)
#print len(x_rounded_data)


    


# Size of image
image_y_size = int(max(y_rounded_data))
# print image_y_size

image_x_size = int(max(x_rounded_data))
# print image_x_size


# Make blank image
image = numpy.zeros((image_x_size+1,image_y_size+1))

for i in range(0,len(x_rounded_data)):
    # print i
    x_location = int(x_rounded_data[i])
    # print x_location
    y_location = int(y_rounded_data[i])
    # print y_location

    if (event_list["GRADE"][i] == 0) | (event_list["GRADE"][i] == 2) | (event_list["GRADE"][i] == 4) | (event_list["GRADE"][i] == 6):
        if numpy.sum(event_list["STATUS"][i]) == 0:
            image[x_location][y_location] = image[x_location][y_location] + 1
            print(image[x_location][y_location])





pyfits.PrimaryHDU(image).writeto("XRay/10135_obs_status_grade.fits",overwrite = True)





# Event List
event_list = pyfits.open('XRay/acisf10135N003_evt2.fits')[1].data
# print event_list

# X coordinates of event
x_data = event_list['x']
# print x_data

# Y coordinates of event
y_data = event_list['y']
# print y_data





# Need to round the pixel coordinates and make image smaller by factor of 4
x_fourth_data = x_data/4
# print x_fourth_data

x_rounded_data = [round(elem) for elem in x_fourth_data]
# print x_rounded_data[0]


y_fourth_data = y_data/4
# print y_fourth_data

y_rounded_data = [round(elem) for elem in y_fourth_data]
# print y_rounded_data[0]

# print y_rounded_data[0],x_rounded_data[0]





#print len(y_rounded_data)
#print len(x_rounded_data)


    


# Size of image
image_y_size = int(max(y_rounded_data))
# print image_y_size

image_x_size = int(max(x_rounded_data))
# print image_x_size


# Make blank image
image = numpy.zeros((image_x_size+1,image_y_size+1))

for i in range(0,len(x_rounded_data)):
    # print i
    x_location = int(x_rounded_data[i])
    # print x_location
    y_location = int(y_rounded_data[i])
    # print y_location

    if (event_list["GRADE"][i] == 0) | (event_list["GRADE"][i] == 2) | (event_list["GRADE"][i] == 4) | (event_list["GRADE"][i] == 6):
        if numpy.sum(event_list["STATUS"][i]) == 0:
            if event_list["energy"][i] > 1200:
                image[x_location][y_location] = image[x_location][y_location] + 1
                print(image[x_location][y_location])





pyfits.PrimaryHDU(image).writeto("XRay/10135_obs_status_grade_energy.fits",overwrite = True)





# Event List
event_list = pyfits.open('XRay/acisf12075N003_evt2.fits')[1].data
# print event_list

# X coordinates of event
x_data = event_list['x']
# print x_data

# Y coordinates of event
y_data = event_list['y']
# print y_data





# Need to round the pixel coordinates and make image smaller by factor of 4
x_fourth_data = x_data/4
# print x_fourth_data

x_rounded_data = [round(elem) for elem in x_fourth_data]
# print x_rounded_data[0]


y_fourth_data = y_data/4
# print y_fourth_data

y_rounded_data = [round(elem) for elem in y_fourth_data]
# print y_rounded_data[0]

# print y_rounded_data[0],x_rounded_data[0]





#print len(y_rounded_data)
#print len(x_rounded_data)


    


# Size of image
image_y_size = int(max(y_rounded_data))
# print image_y_size

image_x_size = int(max(x_rounded_data))
# print image_x_size


# Make blank image
image = numpy.zeros((image_x_size+2,image_y_size+2))

for i in range(0,len(x_rounded_data)):
    # print i
    x_location = int(x_rounded_data[i])
    # print x_location
    y_location = int(y_rounded_data[i])
    # print y_location

    if (event_list["GRADE"][i] == 0) | (event_list["GRADE"][i] == 2) | (event_list["GRADE"][i] == 4) | (event_list["GRADE"][i] == 6):
        if numpy.sum(event_list["STATUS"][i]) == 0:
            if event_list["energy"][i] > 1200:
                image[x_location][y_location] = ((image[x_location][y_location] + 1)+image[x_location+1][y_location] + image[x_location][y_location+1] + image[x_location-1][y_location] + image[x_location][y_location-1])/5
                print(image[x_location][y_location])





pyfits.PrimaryHDU(image).writeto("XRay/12075_obs_status_grade_energy_blurred.fits",overwrite = True)






first_obs = pyfits.open("XRay/10135_obs_status_grade_energy_blurred.fits")[0].data
second_obs = pyfits.open("XRay/10136_obs_status_grade_energy_blurred.fits")[0].data
third_obs = pyfits.open("XRay/10137_obs_status_grade_energy_blurred.fits")[0].data
fourth_obs = pyfits.open("XRay/10138_obs_status_grade_energy_blurred.fits")[0].data
fifth_obs = pyfits.open("XRay/10139_obs_status_grade_energy_blurred.fits")[0].data
sixth_obs = pyfits.open("XRay/12073_obs_status_grade_energy_blurred.fits")[0].data
seventh_obs = pyfits.open("XRay/12074_obs_status_grade_energy_blurred.fits")[0].data
eighth_obs = pyfits.open("XRay/12075_obs_status_grade_energy_blurred.fits")[0].data

# Align observations to first observation
y_align,x_align = numpy.unravel_index(first_obs.argmax(),first_obs.shape)

y_second,x_second = numpy.unravel_index(second_obs.argmax(),second_obs.shape)
y_third,x_third = numpy.unravel_index(third_obs.argmax(),third_obs.shape)
y_fourth,x_fourth = numpy.unravel_index(fourth_obs.argmax(),fourth_obs.shape)
y_fifth,x_fifth = numpy.unravel_index(fifth_obs.argmax(),fifth_obs.shape)
y_sixth,x_sixth = numpy.unravel_index(sixth_obs.argmax(),sixth_obs.shape)
y_seventh,x_seventh = numpy.unravel_index(seventh_obs.argmax(),seventh_obs.shape)
y_eighth,x_eighth = numpy.unravel_index(eighth_obs.argmax(),eighth_obs.shape)

x_second_aligned = numpy.roll(second_obs,x_align-x_second,axis=1)
x_third_aligned = numpy.roll(third_obs,x_align-x_third,axis=1)
x_fourth_aligned = numpy.roll(fourth_obs,x_align-x_fourth,axis=1)
x_fifth_aligned = numpy.roll(fifth_obs,x_align-x_fifth,axis=1)
x_sixth_aligned = numpy.roll(sixth_obs,x_align-x_sixth,axis=1)
x_seventh_aligned = numpy.roll(seventh_obs,x_align-x_seventh,axis=1)
x_eighth_aligned = numpy.roll(eighth_obs,x_align-x_eighth,axis=1)

second_aligned = numpy.roll(x_second_aligned,y_align-y_second,axis=0)
third_aligned = numpy.roll(x_third_aligned,y_align-y_third,axis=0)
fourth_aligned = numpy.roll(x_fourth_aligned,y_align-y_fourth,axis=0)
fifth_aligned = numpy.roll(x_fifth_aligned,y_align-y_fifth,axis=0)
sixth_aligned = numpy.roll(x_sixth_aligned,y_align-y_sixth,axis=0)
seventh_aligned = numpy.roll(x_seventh_aligned,y_align-y_seventh,axis=0)
eighth_aligned = numpy.roll(x_eighth_aligned,y_align-y_eighth,axis=0)

pyfits.PrimaryHDU(second_aligned).writeto("XRay/10136_aligned.fits", overwrite = True)
pyfits.PrimaryHDU(third_aligned).writeto("XRay/10137_aligned.fits", overwrite = True)
pyfits.PrimaryHDU(fourth_aligned).writeto("XRay/10138_aligned.fits", overwrite = True)
pyfits.PrimaryHDU(fifth_aligned).writeto("XRay/10139_aligned.fits", overwrite = True)
pyfits.PrimaryHDU(sixth_aligned).writeto("XRay/12073_aligned.fits", overwrite = True)
pyfits.PrimaryHDU(seventh_aligned).writeto("XRay/12074_aligned.fits", overwrite = True)
pyfits.PrimaryHDU(eighth_aligned).writeto("XRay/12075_aligned.fits", overwrite = True)



        

event_list = pyfits.open('XRay/acisf10135N003_evt2.fits')[1].data
energy_event = []

# X coordinates of event
x_data = event_list['x']
# print x_data

# Y coordinates of event
y_data = event_list['y']
# print y_data

x_rounded_data = [round(elem) for elem in x_data]
# print x_rounded_data[0]

y_rounded_data = [round(elem) for elem in y_data]
# print y_rounded_data[0]


# Energy of event photons
energy = event_list['energy']
# print energy[0]



pulsar_energy = []
for i in range(0,len(x_rounded_data)):
    # print i
    x_location = x_rounded_data[i]
    # print x_location
    y_location = y_rounded_data[i]
    # print y_location

    if x_data[i] > 3900:
        if x_data[i] < 3920:
            if y_data[i] > 4215:
                if y_data[i] < 4235:
                    print(energy[i])
                    pulsar_energy.append(energy[i])



jet_energy = []
for i in range(0,len(x_rounded_data)):
    # print i
    x_location = x_rounded_data[i]
    # print x_location
    y_location = y_rounded_data[i]
    # print y_location

    if x_data[i] > 4050:
        if x_data[i] < 4070:
            if y_data[i] > 4310:
                if y_data[i] < 4330:
                    print(energy[i])
                    jet_energy.append(energy[i])


plt.hist(pulsar_energy, bins=10)
plt.xlabel("Energy")
plt.ylabel("Count")
plt.title("Pulsar Energy")
plt.show()

plt.hist(jet_energy, bins=10)
plt.xlabel("Energy")
plt.ylabel("Count")
plt.title("Jet Energy")
plt.show()






# Event List
event_list = pyfits.open('XRay/acisf14458N002_evt2.fits')[1].data
# print event_list

# X coordinates of event
x_data = event_list['x']
# print x_data

# Y coordinates of event
y_data = event_list['y']
# print y_data





# Need to round the pixel coordinates and make image smaller by factor of 4
x_fourth_data = x_data/4
# print x_fourth_data

x_rounded_data = [round(elem) for elem in x_fourth_data]
# print x_rounded_data[0]


y_fourth_data = y_data/4
# print y_fourth_data

y_rounded_data = [round(elem) for elem in y_fourth_data]
# print y_rounded_data[0]

# print y_rounded_data[0],x_rounded_data[0]





#print len(y_rounded_data)
#print len(x_rounded_data)


    


# Size of image
image_y_size = int(max(y_rounded_data))
# print image_y_size

image_x_size = int(max(x_rounded_data))
# print image_x_size


# Make blank image
image = numpy.zeros((image_x_size+2,image_y_size+2),dtype=numpy.float32)

for i in range(0,len(x_rounded_data)):
    # print i
    x_location = int(x_rounded_data[i])
    # print x_location
    y_location = int(y_rounded_data[i])
    # print y_location

    if (event_list["GRADE"][i] == 0) | (event_list["GRADE"][i] == 2) | (event_list["GRADE"][i] == 4) | (event_list["GRADE"][i] == 6):
        if numpy.sum(event_list["STATUS"][i]) == 0:
            if event_list["energy"][i] > 1200:
                image[x_location][y_location] = ((image[x_location][y_location] + 1)+image[x_location+1][y_location] + image[x_location][y_location+1] + image[x_location-1][y_location] + image[x_location][y_location-1])/5
                print(image[x_location][y_location])





pyfits.PrimaryHDU(image).writeto("Crab_Pulsar_obs_status_grade_energy_blurred.fits",overwrite = True)







