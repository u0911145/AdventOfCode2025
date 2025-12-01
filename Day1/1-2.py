import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.loadtxt(filename, dtype=str)

count = 50
pswd = 0
for item in data:
    dir = -1 if item[0] == 'L' else 1
    num = int(item[1:])
    pswd += ((dir * count) % 100 + num) // 100
    count = (count + dir * num) % 100
print(pswd)