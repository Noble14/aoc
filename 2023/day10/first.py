f = open('inp.txt', 'r')

map = f.read().split('\n')

print(map)
i, j = 0, 0
start = False
while i < len(map) and map[i][j] != 'S':
    j = 0
    while j < len(map[i]) and map[i][j] != 'S':
        j = j + 1
    i = i + 1

print(i-1, j-1)