data = []
total = 0

with open("Day 7/input.txt", "r") as file:
    for line in file:
        if '^' in (x := list(line.rstrip().replace('.', '0'))) or 'S' in (x := list(line.rstrip().replace('.', '0'))):
            data.append(x)

data[0][data[0].index('S')] = 1

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char not in ['0', '^', '.'] : # Theres a beam
            try:
                if data[i+1][j] == "^": # Splitter directly below
                    data[i+1][j-1] = char + int(data[i+1][j-1]) # Add the current value on
                    data[i+1][j+1] = char + int(data[i+1][j+1])
                else:
                    data[i+1][j] = char + int(data[i+1][j])
            except IndexError:
                break

for x in data[-1]:
    try:
        total += x
    except TypeError:
        pass

print(total)