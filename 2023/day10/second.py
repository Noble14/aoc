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
insides = [(x,y)]
minx, maxx, miny, maxy = x , x, y, y
while map[x][y] != 'S':
    dx, dy = change_dir(map[x][y], (dx, dy))
    x, y = x + dx , y + dy
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    if x < minx:
        minx = x
    if y < miny:
        miny = y
    insides.append((x,y))
    counter += 1

print(counter/2)
print("max x" , maxx)
print("max y" , maxy)
print("min x" , minx)
print("min y" , miny)

c = 0
for i in range(minx, maxx + 1):
    for j in range(miny, maxy +1):
        if (i, j) in insides:
            insides.remove(i,j)
            counter -= 1
        bordered = True
        for x,y in [(1,0),(1,-1),(1,1),(0,1),(-1,1),(-1,-1),(0,-1),(-1,0)]:
            l = True
            while l and x + i <= maxx and y + j <= maxy and x + i >= minx and y + j >= miny:
                if (x + i, y + j) in insides:
                    l = False
            if l:
                bordered = False
                break
        if bordered:
            c += 1
print(c)