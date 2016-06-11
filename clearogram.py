from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from matplotlib.patches import Ellipse
import matplotlib.patches as patches
import numpy.random as rnd
#from astropy.table import Table
"""
De-confusifying the Confusogram
Cool Stars 19 Hack Day
by Meredith Rawls and friends
"""

# Read in confusogram data
# Plot it
# Plot it better

#infile = 'confusogram_data.txt'
infile = 'summary-toupies-v3-send.dat'

data = ascii.read(infile, format='commented_header')
#print(data)

#ells = [Ellipse(xy=rnd.rand(2)*10, width=rnd.rand(), height=rnd.rand(), angle=rnd.rand()*360)
#        for i in range(50)]

fig1 = plt.figure()
plt.plot(data['P_rot'], data['M'], ls='None', marker='o', markersize=10)
ax1 = fig1.add_subplot(111)
plt.xlabel(r'$P_{\textrm{rot}}$ (d)')
plt.ylabel(r'Mass ($M_{\odot}$)')

myellipse = Ellipse(xy=(0.5, 0.5), width=0.1, height=0.2)

#ax1.add_patch(myellipse)

plt.show()


