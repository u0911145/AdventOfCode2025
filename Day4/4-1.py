import sys
import numpy as np
from scipy.signal import convolve2d

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = open(filename).read().splitlines()

grid = np.array([[1 if x == "@" else 0 for x in line] for line in data])
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

convolved = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
convolved = convolved[grid > 0]

print((convolved < 4).sum())