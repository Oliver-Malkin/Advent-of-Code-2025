with open("Day 1/input.txt", "r") as file:
    data = file.read().strip().split('\n')

start = 50
counter = 0

for i, turn in enumerate(data):
    if turn[0] ==  'L':
        start = start - int(turn[1:])%100
    else:
        start = start + int(turn[1:])%100

    if start < 0:
        start = start%100
    if start > 99:
        start = start - 100
    if start == 0 :
        counter += 1

print(counter)