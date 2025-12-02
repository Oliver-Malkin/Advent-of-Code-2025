with open("Day 2/input.txt", "r") as file:
    data = file.read().split(',')

total = 0

for i, seqence in enumerate(data):
    start = int(seqence.split('-')[0])
    end = int(seqence.split('-')[1])
    for x in range(start, end+1):
        size = len(str(x))
        if size % 2 == 0: # number has even number of digets
            if str(x)[size//2:] == str(x)[:size//2]:
                total += x

print(total)