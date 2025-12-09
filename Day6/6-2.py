import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.append(np.array([[r[0], ''.join(r[1:])] for r in np.roll(np.genfromtxt(filename, dtype=str, delimiter=1).transpose(), shift=1, axis=1)]), [[' ', ' ']], axis=0)
opindices = np.concatenate(np.where(np.logical_or(~np.char.isspace(data[:, 0]), np.char.isspace(data[:, 1])))).reshape((-1, 2))

count = 0
for set in opindices:
    nums = np.array([int(x) for x in data[set[0]:set[1], 1]])
    count += nums.sum() if data[set[0], 0] == '+' else nums.prod()
print(count)