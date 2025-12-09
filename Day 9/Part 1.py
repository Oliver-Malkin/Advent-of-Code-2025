with open("Day 9/input.txt", "r") as file:
    data = [[int(x) for x in line.rstrip().split(',')] for line in file]

rectSize = 0

for i in data:
    for j in data:
        rect = (abs(i[0]-j[0])+1) * (abs(i[1]-j[1])+1)
        if rect > rectSize:
            rectSize = rect

print(rectSize)