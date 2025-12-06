data = []
total = 0

with open("Day 6/input.txt", "r") as file:
    for line in file:
        data.append(line.split())

operations = data[-1]
data = data[:-1]

for i, opp in enumerate(operations):
    temp = 1
    match opp:
        case '+':
            for x in data:
                total += int(x[i])
        case '*':
            for x in data:
                temp = temp*int(x[i])
            total += temp

print(total)