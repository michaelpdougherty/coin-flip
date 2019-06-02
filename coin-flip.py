#!/usr/bin/env python3.6
#
# Usage: ./coin-flip.py [flips]
#
# This program graphs with matplotlib the relationship between the number
# of coin flips and the difference in percentage of heads and tails.
# Prints total time elapsed.
#
# Created by Michael Dougherty
#
# Inspired by John Fish :)

from datetime import timedelta as td
import matplotlib.pyplot as plt
from random import random
from sys import argv
from time import time

# If argv[1] given, set maximum number of flips to calculate
if len(argv) > 1 and argv[1].isdigit():
    flips = int(argv[1])

# Else, prompt user
else:
    flips = int(input("Flips: "))

# Record starting time
startTime = time()

# Initialize lists
nArray = list()
percentDiff = list()

# Initialize heads
heads = 0

# Flip coins and record difference in heads and tails each time
for flip in range(2, flips + 2):
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
plt.ylabel("Percentage Difference")
plt.title("Accuracy of a 50/50 Chance as Number of Trials Increases")

# Show plot
plt.show()
