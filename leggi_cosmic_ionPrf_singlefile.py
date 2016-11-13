# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:34:09 2016

@author: nazario tartaglione
Read ionospheric data from COSMIC
"""

import netCDF4 as nc
import numpy as np
import os
#import glob, string
from peakdetect import peakdet
#from salishsea_tools import nc_tools

   
    
work_dir = '/media/nazario/SAMSUNG/COSMIC'
myfile=os.path.join(work_dir,'cosmic2013_ionPrf/ionPrf/2009.001/ionPrf_C003.2009.001.02.20.G18_2013.3520_nc')
yourpath=os.path.join(work_dir,'cosmic2013_ionPrf/')


#extract the variables

fh = nc.Dataset(myfile, mode='r')
YY=fh.year
MM=fh.month
DD=fh.day
hh=fh.hour
mm=fh.minute
ss=fh.second
lons = fh.variables['GEO_lon'][:]
lats = fh.variables['GEO_lat'][:]
alt  = fh.variables['MSL_alt'][:]
tec  = fh.variables['TEC_cal'][:]
elden= fh.variables['ELEC_dens'][:]

#find max and min values

import operator
min_index, min_value = min(enumerate(elden), key=operator.itemgetter(1))
max_index, max_value = max(enumerate(elden), key=operator.itemgetter(1))
print(max_value,max_index,alt[max_index])
fh.close()

#plot data

import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
# Plot profiles ***********************************************
# in different ways
fig1 =plt.figure()

ax1 = fig1.add_subplot(111)
ax1.plot(tec,alt,'o-')
 
# Draw x label
ax1.set_xlabel('TEC (TECU)')
ax1.xaxis.set_label_position('top') # this moves the label to the top
ax1.xaxis.set_ticks_position('top') # this moves the ticks to the top
#ax1.xaxis.tick_top() # ANOTHER way to move the ticks to the top
 
# Draw y label
ax1.set_ylabel('Altitude (km)')
#ax1.set_ylim(ax1.get_ylim()[::-1]) #this reverses the yaxis (i.e. deep at the bottom)
#another way to reverse the yaxis
#ax = plt.gca()
#ax.invert_yaxis()

plt.show()

#Two panels in one figure
fig, ax1 = plt.subplots()

ax1.plot(alt,tec, 'b')
ax1.set_xlabel('Altitude (km)')
ax1.xaxis.set_label_position('bottom') # this moves the label to the top/bottom
ax1.xaxis.set_ticks_position('bottom') # this moves the ticks to the top/bottom
#ax1.xaxis.tick_top() # ANOTHER way to move the ticks to the top
 
# Draw y label
ax1.set_ylabel('TEC (TECU)')
for tl in ax1.get_yticklabels():
    tl.set_color('b')


ax2 = ax1.twinx()

ax2.plot(alt,elden, 'r.')
ax2.set_ylabel('electronic density', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.show()



#if we want to have altitude on y axis

fig, ax1 = plt.subplots()

ax1.plot(tec,alt, 'b')
ax1.set_xlabel('TEC (TECU)')
#ax1.xaxis.set_label_position('bottom') # this moves the label to the top/bottom
#ax1.xaxis.set_ticks_position('bottom') # this moves the ticks to the top
#ax1.xaxis.tick_top() # ANOTHER way to move the ticks to the top
for tl in ax1.get_xticklabels():
    tl.set_color('b')
# Draw y label
ax1.set_ylabel('Altitude')



ax2 = ax1.twiny()

ax2.plot(elden/10000,alt, 'r.')
ax2.set_xlabel('electronic density $cm^{-3} \cdot 10^{-4}$', color='r')

for tl in ax2.get_xticklabels():
    tl.set_color('r')
plt.show()


#where the observation is located
# Get some parameters for the Stereographic Projection
#lon_0 = lons.mean()
#lat_0 = lats.mean()
#
#m = Basemap(width=5000000,height=3500000,
#            resolution='l',projection='stere',\
#            lat_ts=40,lat_0=lat_0,lon_0=lon_0)




#Find local maxima - Use peakdetect.py

maxtab, mintab = peakdet(elden,10)
fig1=plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(elden)
ax1.scatter(np.array(maxtab)[:,0], np.array(maxtab)[:,1], color='blue')
ax1.scatter(np.array(mintab)[:,0], np.array(mintab)[:,1], color='red')
plt.show()
