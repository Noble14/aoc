f = open('inp.txt', 'r')

map = f.read().split('\n')

def change_dir(char, dir):
    x, y = dir
    if char == "|" or char == "-":
        return (x,y)
    elif char == "L" or char == "7":
        return (y, x)
    elif char == "J" or char == "F":
        return (-y, -x)

for i, line in enumerate(map):
    for j, char in enumerate(line):
        if char == 'S':
            start = (i, j)
            break
i, j = start

dx, dy = (1, 0)
x, y = (i + dx, j + dy)
counter = 1
while map[x][y] != 'S':
    dx, dy = change_dir(map[x][y], (dx, dy))
    x, y = x + dx , y + dy
    counter += 1

print(counter/2)

