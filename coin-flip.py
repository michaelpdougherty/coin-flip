#!/usr/bin/env python3.6
#
# Usage: ./coin-flip.py [flips]
#
# This program graphs with matplotlib the relationship between the number
# of coin flips and the distance of percentage of heads from 50%.
# Prints total time elapsed.
#
# Created by Michael Dougherty
#
# Inspired by John Fish

from datetime import timedelta as td
import matplotlib.pyplot as plt
from random import random
from sys import argv
from time import time

# Set default number of flips
DEFAULT = 10000

# Get flips
if len(argv) == 2:
    flips = int(argv[1]) if argv[1].isdigit() else DEFAULT
else:
    flips = input(f"Flips (default {DEFAULT}): ")
    flips = int(flips) if flips.isdigit() else DEFAULT

# Record starting time
startTime = time()

# Initialize lists
nArray = list()
percentDiff = list()

# Initialize heads
heads = 0

# Flip coins and record distance of percentage of heads from 50%
for flip in range(1, flips + 1):
    # "Flip coins"
    if random() >= 0.5:
        heads += 1

    # Get percentage of heads
    percentHeads = (heads * 100) / flip

    # Append x and y values to lists
    nArray.append(flip)
    percentDiff.append(abs(50 - percentHeads))

# Print total time
elapsedTime = str(td(seconds=round(time() - startTime, 10)))[5:]
print(f"{elapsedTime} seconds elapsed")

# Create plot
plot = plt.plot(nArray, percentDiff)

# Add labels
plt.xlabel("Number of Flips")
plt.ylabel("Distance of percentage of heads from 50% (%)")
plt.title("Accuracy of a 50/50 Chance as Number of Trials Increases")

# Show plot
plt.show()
