import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.loadtxt(filename, dtype=str).transpose()
data = np.flip(data, axis=1)
count = 0
for row in data:
    if row[0] == '+':
        count += np.array([int(x) for x in row[1:]]).sum()
    elif row[0] == '*':
        count += np.array([int(x) for x in row[1:]]).prod()
print(count)