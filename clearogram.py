from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
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

print(data)

#mass, prot, ross, stov, mag1, mag2 = 