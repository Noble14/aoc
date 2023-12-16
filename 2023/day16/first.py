import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(3500)

f = open("inp.txt", "r")

data = f.read().split("\n")

pos = (0,0)
dir = (0,1)

energized = []

for i in range(len(data)):
    line = []
    for j in range(len(data[0])):
        line.append({"val" : False, "from":[]})
    energized.append(line)

def go_next(pos, dir, data, lenx, leny, prevpos):
    x, y = pos
    dx, dy = dir
    setit = False
    if x < 0 or x >= lenx or y < 0 or y >= leny:
        return
    if energized[x][y]["val"] == True:
        if prevpos in energized[x][y]["from"]:
            return
    else:
        setit = True
        energized[x][y]["val"] = True
        energized[x][y]["from"].append(prevpos)

    if data[x][y] ==".":
        newpos = (x + dx, y + dy)
        go_next(newpos, dir, data, lenx, leny, pos)
    if data[x][y] == "/":
        newdir = (-dy,-dx)
        newpos = (x + newdir[0], y + newdir[1])
        go_next(newpos, newdir, data, lenx, leny, pos)
    if data[x][y] == "\\":
        newdir = (dy,dx)
        newpos = (x + newdir[0], y + newdir[1])
        go_next(newpos, newdir, data, lenx, leny, pos)
    if data[x][y] == "-":
        if dy == 0:
            energized[x][y]["from"].append(prevpos)
            if setit:
                energized[x][y]["from"].append((x+dx, y+dy))
            go_next((x,y+1), (0, 1), data, lenx, leny, pos)
            go_next((x,y-1), (0, -1), data, lenx, leny, pos)
        else:
            newpos = (x + dx, y + dy)
            go_next(newpos, dir, data, lenx, leny, pos)
    if data[x][y] == "|":
        if dx == 0:
            energized[x][y]["from"].append(prevpos)
            if setit:
                energized[x][y]["from"].append((x+dx, y+dy))
            go_next((x+1,y), (1, 0), data, lenx, leny, pos)
            go_next((x-1,y), (-1, 0), data, lenx, leny, pos)
        else:
            newpos = (x + dx, y + dy)
            go_next(newpos, dir, data, lenx, leny, pos)
    return

lenx = len(data)
leny = len(data[0])
go_next(pos, dir, data, lenx, leny,(-1, -1))
counter = 0
for line in energized:
    l = ""
    for x in line:
        if x["val"]:
            counter += 1
            l = l + "#"
        else:
            l = l + "."
    # print(l)
print(counter)