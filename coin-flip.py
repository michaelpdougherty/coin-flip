#!/usr/bin/env python3.6

# Flips coin flips number of times
# and prints percentages of each heads and tails

from random import random
from time import time
from datetime import timedelta

flips = int(input("Flips: "))

startTime = time()

heads = 0
tails = 0

for i in range(0,flips):
    if random() >= 0.5:
        heads += 1
    else:
        tails += 1

elapsedTime = str(timedelta(seconds=round(time() - startTime, 10)))[5:]

print(f"Flipped {flips} coins in {elapsedTime} seconds")

print(f"Heads: {round((heads / flips)*100, 2)}%")
print(f"Tails: {round((tails / flips)*100, 2)}%")
