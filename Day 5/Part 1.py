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

for i in ingredients:
    for j in ranges:
        if i in range(j[0], j[1]+1):
            total += 1
            break

print(total)