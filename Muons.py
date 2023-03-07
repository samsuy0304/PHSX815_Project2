#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import math

from Generator import Decay

Tests= Decay()

boo = False
while boo == False:
    n, p, l = Tests.Time()
    print(len(n),len(p))
    hist, bins = np.histogram(l,50)

    # Calculate the bin width
    bin_width = bins[1] - bins[0]

    # Calculate the midpoint of each bin
    bin_midpoints = bins[:-1] + bin_width / 2

    # Calculate the weighted mean of the l
    mean = np.sum(hist * bin_midpoints) / np.sum(hist)
    
    print("Estimated rate parameter:", mean)
    if mean > 2.4e-6:
        break
    Tests.Update_Probability()
    
    plt.show()
