import matplotlib.pyplot as plt

with open("Day 9/input.txt", "r") as file:
    data = [[int(x) for x in line.rstrip().split(',')] for line in file]

x_coords, y_coords = zip(*data)
x_coords = list(x_coords)
y_coords = list(y_coords)

plt.plot(x_coords, y_coords, '.')
plt.axvline(x=94916)
plt.axhline(y=66770)
plt.show()
rectSize = 0

# yeah ngl i did this manually after plotting it :smile:


