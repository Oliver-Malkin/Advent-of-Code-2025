data = []
total = 0
state = ''
temp = ''
temptemp = []

with open("Day 6/input.txt", "r") as file:
    for line in file:
        data.append(list(line.strip('\n')+' '))

operations = data[-1]
data = data[:-1]

for i, opp in enumerate(operations):
    if opp == '+':
        state = "ADD"
    elif opp == "*":
        state = "TIMES"

    temp = ''
    for j in data:
        temp += j[i]
    
    if temp.strip() == '' or i == len(data[0])-1:
        if state == 'ADD':
            for k in temptemp:
                total += k
        else:
            temptemptemp = 1
            for k in temptemp:
                temptemptemp = temptemptemp * k
            total += temptemptemp
        temptemp = []
    else:
        temptemp.append(int(temp))

print(total)