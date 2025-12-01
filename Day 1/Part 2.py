with open("Day 1/input.txt", "r") as file:
    data = file.read().strip().split('\n')

dial = 50
counter = 0

for i, turn in enumerate(data):
    number = int(turn[1:])
    counter = counter + number//100 # count how many full revolutions there have been
    number = number%100             # number is always < 100

    if turn[0] ==  'L':
        if dial - number < 0 and dial != 0:
            counter += 1
        dial = dial - number
    else:
        if dial + number > 100:
            counter += 1
        dial = dial + number

    if dial < 0:
        dial = dial % 100
    if dial > 99:
        dial = dial - 100
    if dial == 0:
        counter += 1

print(counter)