import uuid

data = []
routes = {}

with open("Day 8/test.txt", "r") as file:
    for line in file:
        tmp = line.rstrip().split(',')
        tmp.append(None) # Circuit
        tmp.append([]) # Connection's
        data.append(tmp)

def findClosest(junctBox):
    dist = 1e+12
    closest = None
    index = 0
    for i, x in enumerate(data):
        if x != junctBox and (i not in junctBox[4]): # Not self AND Not directly connected
            tempDist = (int(junctBox[0]) - int(x[0]))**2 + (int(junctBox[1]) - int(x[1]))**2 + (int(junctBox[2]) - int(x[2]))**2
            if tempDist < dist:
                dist = tempDist
                closest = x
                index = i

    return(closest, dist, index)

temp = []

for i in range(1):
    for j, node in enumerate(data): # Find the closest node to node j
        result = findClosest(node)
        temp.append([node, result[0], result[1]])

    temp = sorted(temp, key=lambda x: x[2]) # Sort the list of nodes by distance
    for x in temp:
        print(x)
    closest = temp[0]
    data[data.index(closest[0])][4].append(data.index(closest[1]))
    data[data.index(closest[1])][4].append(data.index(closest[0]))

    if closest[0][3] is None and closest[1][3] is None: # Both not in a circuit yet
        newRoute = str(uuid.uuid4())
        closest[0][3] = newRoute
        closest[1][3] = newRoute
        routes[str(uuid.uuid4())] = [closest[0][:-2], closest[1][:-2]]
    elif closest[0][3] is not None and closest[1][3] is None: # First is in a circuit
        routes[closest[0][3]].append(closest[1][:-2])
    elif closest[0][3] is None and closest[1][3] is not None: # Second is in a circuit
        routes[closest[1][3]].append(closest[0][:-2])
    # If they are in the same circuit we dont care

    print(data,'\n')
    
for x in routes:
    print(routes[x])
