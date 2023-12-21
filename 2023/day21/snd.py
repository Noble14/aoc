import heapq
from collections import defaultdict

f = open("inp.txt", "r")

data = f.read().split("\n")

STEPS = 1000

i = 0
start = False
for line in data:
    j = 0
    for char in line:
        if char == 'S':
            start = True
            break
        j += 1
    if start:
        break
    i += 1

heap = []
heapq.heappush(heap,(0, (i,j)))
dists = defaultdict(lambda: float('inf'))

xlen = len(data)
ylen = len(data[0])

def get_neigh(i,j):
    res = []
    for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        rx, ry = x, y
        x = x % xlen
        y = y % ylen
        if data[x][y] == "." or data[x][y] == 'S':
            res.append((rx,ry))
    return res

counter = 0


while heap:
    dist, (x, y) = heapq.heappop(heap)
    if dist > STEPS:
        break
    for pos in get_neigh(x,y):
        if dists[pos] > dist + 1 or (dists[pos] % 2 == 1 and (dist + 1) % 2 == 0):
            dists[pos] = dist + 1
            if ((dist + 1) % 2) == 0:
                counter += 1
            heapq.heappush(heap,(dist+1, pos))

print(counter)