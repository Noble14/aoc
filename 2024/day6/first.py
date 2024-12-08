

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

# print(data)

# print(data[row][col])

def moveright(direction):
    X, Y = direction
    return (Y, -X)
def nextstep(data, direction, row, col):
    X, Y = direction
    return data[row + X][col + Y]
def take_next_step(direction, row, col):
    X, Y = direction
    return (row + X, col + Y)

direction = (-1, 0)

while col + direction[1] < collen and row +direction[0 ]< rowlen and row + direction[0] > -1 and col + direction[1] > -1:
    data[row][col] = "X"
    if nextstep(data, direction, row, col) == "#":
        direction = moveright(direction)
    row, col = take_next_step(direction, row, col)

data[row][col] = "X"

# for i in range(rowlen):
#     data[i] = "".join(data[i])
#     print(data[i])

sum = 0
for i in range(rowlen):
    sum += data[i].count("X")

print(sum)


