import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(3500)

f = open("inp.txt", "r")

data = f.read().split("\n")

pos = (0,0)
dir = (0,1)


def init_energized():
    energized = []
    for i in range(len(data)):
        line = []
        for j in range(len(data[0])):
            line.append({"val" : False, "from":[]})
        energized.append(line)
    return energized

def go_next(pos, dir, data, lenx, leny, prevpos):
    x, y = pos
    dx, dy = dir
    counter = 0
    setit = False
    if x < 0 or x >= lenx or y < 0 or y >= leny:
        return 0
    if energized[x][y]["val"] == True:
        if prevpos in energized[x][y]["from"]:
            return 0
    else:
        counter += 1
        setit = True
        energized[x][y]["val"] = True

    if data[x][y] ==".":
        newpos = (x + dx, y + dy)
        counter += go_next(newpos, dir, data, lenx, leny, pos)
    if data[x][y] == "/":
        newdir = (-dy,-dx)
        newpos = (x + newdir[0], y + newdir[1])
        counter += go_next(newpos, newdir, data, lenx, leny, pos)
    if data[x][y] == "\\":
        newdir = (dy,dx)
        newpos = (x + newdir[0], y + newdir[1])
        counter += go_next(newpos, newdir, data, lenx, leny, pos)
    if data[x][y] == "-":
        if dy == 0:
            energized[x][y]["from"].append(prevpos)
            if setit:
                energized[x][y]["from"].append((x+dx, y+dy))
            counter += go_next((x,y+1), (0, 1), data, lenx, leny, pos)
            counter += go_next((x,y-1), (0, -1), data, lenx, leny, pos)
        else:
            newpos = (x + dx, y + dy)
            counter += go_next(newpos, dir, data, lenx, leny, pos)
    if data[x][y] == "|":
        if dx == 0:
            energized[x][y]["from"].append(prevpos)
            if setit:
                energized[x][y]["from"].append((x+dx, y+dy))
            counter += go_next((x+1,y), (1, 0), data, lenx, leny, pos)
            counter += go_next((x-1,y), (-1, 0), data, lenx, leny, pos)
        else:
            newpos = (x + dx, y + dy)
            counter += go_next(newpos, dir, data, lenx, leny, pos)
    return counter

lenx = len(data)
leny = len(data[0])
max = 0

for i in range(len(data)):
    energized = init_energized()
    k = go_next((i,0), (0,1), data, lenx,leny,(i, -1))
    if (max < k):
        max = k

for i in range(len(data)):
    energized = init_energized()
    k = go_next((i,leny-1), (0, -1), data, lenx,leny,(i, leny))
    if (max < k):
        max = k

for i in range(leny):
    energized = init_energized()
    k = go_next((0, i), (1, 0), data, lenx,leny,(-1, i))
    if (max < k):
        max = k

# down
for i in range(leny):
    energized = init_energized()
    k = go_next((lenx-1, i), (-1, 0), data, lenx,leny,(lenx, i))
    if (max < k):
        max = k
print(max)