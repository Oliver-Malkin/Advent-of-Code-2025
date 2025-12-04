with open("Day 3/input.txt", "r") as file:
    data = file.read().split('\n')

total = 0

for i, bank in enumerate(data):
    batteries = list(bank)
    max_value = max(batteries[:-1]) # find the max value from the bank (excluding last)
    next_max = max(batteries[batteries.index(max_value)+1:])

    total += int(max_value+next_max)

print(total)
    