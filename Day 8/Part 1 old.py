from math import sqrt
import uuid

data = []
routes = {}

with open("Day 8/test.txt", "r") as file:
    for line in file:
        tmp = line.rstrip().split(',')
        tmp.append(None)
        tmp.append(None)
        data.append(tmp)

def findClosest(junctBox):
    dist = 1e+12
    closest = None
    for x in data:
        if x != junctBox and (
            x[4] != junctBox[4] or (x[4] is None) or (junctBox[4] is None)): # Not self, not directly connected
            tempDist = sqrt((
                int(junctBox[0]) - int(x[0]))**2 + (
                int(junctBox[1]) - int(x[1]))**2 + (
                int(junctBox[2]) - int(x[2]))**2)
            if tempDist < dist:
                dist = tempDist
                closest = x

    return(closest, dist)

temp = []

for i in range(4):
    for x in data:
        result = findClosest(x)
        temp.append([x, result[0], result[1]])
        
    temp = sorted(temp, key=lambda x: x[2])
    for y in temp:
        if (y[0][3] != y[1][3]) or (y[0][3] is None) or (y[1][3] is None): # Are they in the same circuit
            closest = y
            break

    closest[0][4] = str(uuid.uuid4())
    closest[1][4] = closest[0][4]
    if (first := closest[0][3]) is None and (second := closest[1][3]) is None: # Both are not in a circuit
        closest[0][3] = str(uuid.uuid4())
        closest[1][3] = closest[0][3]
    elif first is None:
        closest[0][3] = closest[1][3]
    else:
        closest[1][3] = closest[0][3]

    if (route := closest[0][3]) in routes: # Circuit already exists
        if closest[0][:-2] not in routes[route]: # Add the new junction boxes
            routes[route].append(closest[0][:-2])
        else:
            routes[route].append(closest[1][:-2])
    else:
        routes[route] = [closest[0][:-2], closest[1][:-2]]

for x in routes:
    print(routes[x])
