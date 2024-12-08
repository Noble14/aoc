f = open("inp.txt", "r")
data = f.read().strip().split("\n")
dic = {}
i, j = 0, 0
for line in data:
    j = 0
    for ch in line:
        if ch == '.':
            j += 1
            continue
        if ch in dic:
            dic[ch].append((i, j))
        else:
            dic[ch] = [(i, j)]
        j += 1
    i += 1

for i in range(len(data)):
    data[i] = list(data[i])

def add_antinode(antinode, data):
    x, y = antinode
    if x < 0 or x >= len(data) or y < 0 or y >= len(data[0]):
        return False
    data[x][y] = "#"
    return True


for key in dic.keys():
    i = 0
    antennas = dic[key]
    n = len(antennas)
    while i < n-1:
        j = i+1
        while j < n:
            x1, y1 = antennas[i]
            x2, y2 = antennas[j]
            dx = x2 - x1
            dy = y2 - y1
            antinode1 = (x2 + dx, y2 + dy)
            antinode2 = (x1 - dx, y1 - dy)
            add_antinode(antinode1, data)
            add_antinode(antinode2, data)
            j += 1
        i += 1


c = 0
for line in data:
    for ch in line:
        if ch == "#":
            c += 1

print(c)

