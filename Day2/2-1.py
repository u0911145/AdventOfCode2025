import sys
import math

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = open(filename).read().split(',')

count = 0
for item in data:
    nums = item.split('-')
    place = 10 ** math.ceil(len(nums[0]) / 2)
    for i in range(int(nums[0]) // place, int(nums[1]) // place + 1):
        num = int(str(i) * 2)
        if num >= int(nums[0]) and num <= int(nums[1]):
            count += num
print(count)