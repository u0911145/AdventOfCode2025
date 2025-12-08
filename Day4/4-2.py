import sys
import numpy as np
from scipy.signal import convolve2d

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = open(filename).read().splitlines()

grid = np.array([[1 if x == "@" else 0 for x in line] for line in data])
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

count = 0
moved = 99
while moved > 0:
    convolved = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
    convolved[grid < 1] = 99

    moved = (convolved < 4).sum()
    count += moved

    grid[convolved < 4] = 0
print(count)