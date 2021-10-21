import numpy as np
import matplotlib.pyplot as plt
from  astropy.time import Time

z = np.linspace(0, 90, 10**4)
alt = 90 - z
X = 1 / np.sin(np.radians(alt + 244 / (165 + 47 * alt**1.1)))
label = 'Plane-Parallel approx.'
plt.plot(z, 1 / np.cos(np.radians(z)), label = label, lw = 7, ls = 'dotted')
plt.xlabel('Zenith Angle (deg)')
plt.ylabel('Airmass')
plt.ylim(0, 10)
plt.legend()
#plt.show()

#date must be of the form "year-month-day hour:minute:seconds"

def airmass_calc (ra, dec, date, lat, long):
    #base everything around noon local time
    #meridian moves 360 degrees per year, and is 0 on vernal equinox
    #base everything on vernal equinox 2021
    #all time will be kept in hours
    vernal_equinox = Time("2021-03-20 12:00:00") #when the meridian has 0 RA
    date = Time(date)
    deltaTime = date - vernal_equinox
    delta_ra = deltaTime.value * 24/365
    print(delta_ra)
    '''
    hour_angle = hour_angle(ra, dec, date)
    airmass = 1 / (np.sin(lat) * np.sin(dec) +
        np.cos(lat) * np.cos(dec) * np.cos(hour_angle))
    lst = hour_angle + ra
    #get an array of lst values and corresponding airmasses, then plot them
    #against each other
    return airmass
    '''

ra = 5.22
dec = 22.2
lat = 33.3
long = -116.8
date = "2021-10-23 00:00:00"

airmass_calc(ra, dec, date, lat, long)

def hour_angle(ra, dec, date):
    return
