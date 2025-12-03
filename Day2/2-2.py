import sys
import math

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = open(filename).read().split(',')

count = 0
for item in data:
    nums = item.split('-')
    print(nums)
    place = 10 ** math.ceil(len(nums[0]) / 2)
    checks = set()
    for i in range(int(nums[0]) // place, int(nums[1]) // place + 1):
        for j in range(len(str(i))):
            substring = str(i)[:j+1]
            length = len(substring)
            if (len(nums[0]) % length == 0):
                len0 = (len(nums[0]) // len(substring))
                checks.add(int(substring * len0))
            if (len(nums[1]) % length == 0):
                len1 = (len(nums[1]) // len(substring))
                checks.add(int(substring * len1))
    for check in checks:
        if check >= int(nums[0]) and check <= int(nums[1]):
            count += check
print(count)