f = open("inp.txt", 'r')

coordinates = []
cols = [False] * 10000

part = {
    1 : 2,
    2 : 1000000
}

magic = part[2]

row = 0
for line in f:
    col = 0
    galaxy = False
    for char in line:
        if char == '#':
            coordinates.append([row,col])
            galaxy = True
            cols[col] = True
        col = col + 1
    add = 1 if galaxy else magic
    row = row + add

def empty_cols_before(col, cols):
    i = 0
    count = 0
    while i < col:
        if cols[i] == False:
            count = count + 1
        i = i + 1
    res = 0 if count == 0 else count * (magic - 1)
    return res

coordinates = list(map(lambda x:  [ x[0] , x[1] + empty_cols_before(x[1], cols)],coordinates))


def get_distance(x,y):
    a, b = x
    c, d = y
    return abs(a -c) + abs(b -d)

sum = 0
for coor1 in coordinates:
    mind = 150000
    for coor2 in coordinates:
        if coor1[0] == coor2[0] and coor2[1] == coor1[1]:
            continue
        dist = get_distance(coor1, coor2)
        sum = sum + dist

print(int(sum / 2))

