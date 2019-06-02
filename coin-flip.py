#!/usr/bin/env python3.6

# This program graphs the relationship between the difference in percentages
# of heads and tails and the number of coin flips as it increases from
# one to a user-inputted number
#
# Created by Michael Dougherty
#
# Inspired by John Fish :)

from random import random
from time import time
from datetime import timedelta as td
import matplotlib.pyplot as plt

# Set maximum number of flips to calculate
maxFlips = int(input("Max Flips: "))

# Record starting time
startTime = time()

# Initialize lists
nArray = list()
percentDiff = list()

# Flip coins 1 up to maxFlips times and record difference in percentages
for flips in range(1, maxFlips + 1):
    heads = 0
    tails = 0
    for i in range(0, flips + 1):
        if random() >= 0.5:
            heads += 1
        else:
            tails += 1
    percentHeads = (heads * 100) / flips
    percentTails = (tails * 100) / flips

    nArray.append(flips)
    percentDiff.append(abs(percentHeads - percentTails))

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
