# PythonCode
Various Python Code Examples


The following are codes developed for an astronomical data analysis class
Within each python program are notes detailing most steps in the analysis


Python program name:     celestial_navigation.py

Program function:     Plots the altitude of a target star over 24 hours as observed from a particular observing site on a particular date

Program command line arguments:    
          
          celestial_navigation.py year month day obs_long obs_lat target_ra target_dec

where obs_long is the observing longitude, obs_lat is the observing latitude, target_ra is the target's Right Ascension, target_dec is the target's declination

Example:     Plot titled "SOAR Altitude Graph" is the output of this program using the following command line arguments

             celestial_navigation.py 2015 09 01 273.0 32.0 4:00:00 12:00:00

          
          

Python program name:     celestial_navigation_list.py

Program function:     Plots the altitude of multiple targets over 24 hours as observed from a particular observing site on particular date

Program command line arguments:     
          
          celestial_navigation.py year month day obs_long obs_lat

where obs_long is the observing longitude, obs_lat is the observing latitude

This program reads in multiple targets Right Ascensions and Declinations from a file titled "Target_Altitudes.txt"

Example:     Plot titled "SOAR Altitude Graph Multiple Targets" is the output of this program using the following command line arguments

             celestial_navigation_list.py 2015 09 01 273.0 32.0
There are also multiple tables outside the graph which label which times a given target is above an airmass of 2.0
          
          
          

