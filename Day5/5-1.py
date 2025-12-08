import sys

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = open(filename).read().split("\n\n")
ranges = [[int(x) for x in line.split("-")] for line in data[0].splitlines()]

count = 0
for num in data[1].splitlines():
    num = int(num)
    for r in ranges:
        if num >= r[0] and num <= r[1]:
            count += 1
            break
print(count)