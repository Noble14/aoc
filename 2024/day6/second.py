


f = open("inp.txt", "r")

data = f.read().strip().split("\n")

rowlen = len(data[0])
collen = len(data)

row = 0
col = 0
found = False
while row < rowlen  and data[row][col] != "^":
    while col < collen and not found:
        found = data[row][col] == "^"
        if found:
            break
        col += 1
    if found:
        break
    col = 0
    row += 1

# print(row, col)
for i in range(rowlen):
    data[i] = list(data[i])
    for j in range(collen):
        data[i][j] = (data[i][j], [])

# print(data)

# print(data[row][col])

def moveright(dire):
    X, Y = dire
    return (Y, -X)
def nextstep(hellodata, dire, row, col):
    X, Y = dire
    return hellodata[row + X][col + Y][0]
def take_next_step(dire, row, col):
    X, Y = dire
    return (row + X, col + Y)

def iter(newdata, dire, r, c):
    while c+ dire[1] < collen and r+dire[0 ]< rowlen and r+ dire[0] > -1 and c+ dire[1] > -1:
        if any(a == dire[0] and b == dire[1] for a, b in newdata[r][c][1]):
            return True
        newdata[r][c] = ("X", newdata[r][c][1])
        if nextstep(newdata, dire, r, c) == "#":
            dire = moveright(dire)
        newdata[r][c][1].append(dire)
        r, c= take_next_step(dire, r, c)

    return False

dire = (-1, 0)
step = 0

while col + dire[1] < collen and row +dire[0 ]< rowlen and row + dire[0] > -1 and col + dire[1] > -1:
    data[row][col][1].append(dire)
    data[row][col] = ("X", data[row][col][1])
    while nextstep(data, dire, row, col) == "#":
        dire = moveright(dire)
    else:
        newdir = moveright(dire)
        nrow, ncol = take_next_step(newdir, row, col)
        prow, pcol = take_next_step(dire, row, col)
        newdata = []
        for i in range(rowlen):
            dd = []
            for j in range(collen):
                dd.append((data[i][j][0], list(data[i][j][1])))
            newdata.append(dd)
        newdata[prow][pcol] = ("#", newdata[prow][pcol][1])
        if iter(newdata, newdir, row, col):
            # print(f'prow: {prow}, pcol: {pcol} row: {row}, col: {col} nrow: {nrow}, ncol: {ncol}')
            step += 1
    row, col = take_next_step(dire, row, col)




print (step)

