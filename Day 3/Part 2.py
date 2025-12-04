with open("Day 3/input.txt", "r") as file:
    data = file.read().split('\n')

total = 0

for i, bank in enumerate(data):
    batteries = list(bank)
    j = 0

    while len(batteries) != 12:
        try:
            if int(batteries[j]) >= int(batteries[j+1]):
                j += 1
            else:
                batteries.pop(j)
                j = 0
        except IndexError:
            batteries = batteries[:-1]

    total += int(''.join(batteries))

print(total)