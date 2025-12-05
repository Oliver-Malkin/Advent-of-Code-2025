ingredients = []
ranges = []
flag = True
total = 0

with open("Day 5/input.txt", "r") as file:
    for line in file:
        if line.rstrip() == "":
            flag = False
        elif flag:
            temp = line.rstrip().split('-')
            ranges.append([int(temp[0]), int(temp[1])])
        else:
            ingredients.append(int(line.rstrip()))

ranges = sorted(ranges, key=lambda x: x[0])
new_ranges = [ranges[0]] # First one in the list
ranges.pop(0)

for range_ in ranges: # Current ranges
    flag = True
    for j, new_range in enumerate(new_ranges): # New ranges

        if range_[0] in range(new_range[0], new_range[1]+1) and range_[1] > new_range[1]:
            new_ranges[j][1] = range_[1]
            flag = False
        
        elif range_[1] in range(new_range[0], new_range[1]+1) and range_[0] < new_range[0]:
            new_ranges[j][0] = range_[0]
            flag = False

        elif range_[0] in range(new_range[0], new_range[1]+1) and range_[1] in range(new_range[0], new_range[1]+1):
            flag = False # Range already in another range so ignore it

    if flag:
        new_ranges.append(range_)

for i in new_ranges:
    total += i[1]-i[0]+1

print(total)