from numpy import roll, array

with open("Day 2/input.txt", "r") as file:
    data = file.read().split(',')

total = 0

for i, seqence in enumerate(data):
    start = int(seqence.split('-')[0])
    end = int(seqence.split('-')[1])
    for x in range(start, end+1):
        size = len(str(x))
        original = array(list(str(x)))
        for j in range(size//2):
            if (original == roll(original, j+1)).all():
                total += x
                break

print(total)