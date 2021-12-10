import numpy as np
import matplotlib.pyplot as plt
from  astropy.time import Time
#all dates and times are GMST


#date must be of the form "year-month-day hour:minute:seconds"
def airmass_calc (ra, dec, date, utc, lat, long):        
    #base everything around noon local time
    #meridian moves 360 degrees per year, and is 0 on vernal equinox
    #base everything on vernal equinox 2021
    #all time will be kept in hours
    autumnal_equinox = Time("2021-09-22 00:00:00") 
    #when the RA on the meridian matches the time of day
    date = Time(date)
    deltaTime = date - autumnal_equinox #deltaTime.value will be in days
    lst = float(deltaTime.value) * 24 * (360 / 365) / 365
    #account for the movement of Earth through its orbit
    lst = lst + float((deltaTime.value - int(deltaTime.value)) * 24)  
    #account for Earth's rotation about the spin axis
    if utc:
        lst += long * 24 / 360 #adjust for location 
    lst %= 24 
    hour_angle = lst - ra #adjust for star position
    hour_angle %= 24
    #calculate airmass
    partone = np.sin(np.deg2rad(lat)) * np.sin(np.deg2rad(dec))
    parttwo = np.cos(np.deg2rad(lat)) * np.cos(np.deg2rad(dec))
    parttwo *= np.cos(hour_angle * np.pi / 12)
    airmass = 1 / (partone + parttwo)
    zenith_angle = np.arccos(1 / airmass) * 180 / np.pi 
    return (airmass, hour_angle)