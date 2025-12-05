import numpy as np

with open("Day 4/input.txt") as file:
    data = [list(line.rstrip()) for line in file]

data = np.pad(np.array(data), [(1, 1), (1, 1)], mode='constant')
total = 0

def findRolls(x: int, y: int) -> int:
    count = 0
    if data[y-1][x-1] == "@":
        count += 1
    if data[y-1][x] == "@":
        count += 1
    if data[y-1][x+1] == "@":
        count += 1

    if data[y][x-1] == "@":
        count += 1
    if data[y][x+1] == "@":
        count += 1

    if data[y+1][x-1] == "@":
        count += 1
    if data[y+1][x] == "@":
        count += 1
    if data[y+1][x+1] == "@":
        count += 1

    return(count)

loop = True
old_total = 0
while loop:
    for i in range(1, len(data)-1):         # Y
        for j in range(1, len(data[0])-1):  # X
            if findRolls(j, i) < 4 and data[i][j] == '@':
                total += 1
                data[i][j] = '.'

    if old_total != total:
        old_total = total
    else:
        loop = False

print(total)