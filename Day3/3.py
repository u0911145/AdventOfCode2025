import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
digits = int(sys.argv[2]) if len(sys.argv) > 2 else 2
data = open(filename).read().splitlines()

count = 0
for line in data:
    nums = np.array([int(x) for x in line])
    startind = 0
    for i in reversed(range(digits)):
        maxind = startind + nums[startind:len(nums)-i].argmax()
        count += nums[maxind] * 10 ** i
        startind = maxind + 1
print(count)