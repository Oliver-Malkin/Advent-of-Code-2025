data = []
total = 0

with open("Day 7/input.txt", "r") as file:
    for line in file:
        data.append(list(line.rstrip()))

data[0][data[0].index('S')] = '|'

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == '|': # Theres a beam
            try:
                if data[i+1][j] == "^": # Splitter directly below
                    data[i+1][j-1] = '|'
                    data[i+1][j+1] = '|'
                    total += 1
                else:
                    data[i+1][j] = '|'
            except IndexError:
                break

for x in data:
    print(''.join(x))

print(total)