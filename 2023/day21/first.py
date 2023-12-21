import heapq
from collections import defaultdict

f = open("inp.txt", "r")

data = f.read().split("\n")

STEPS = 64

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
dists = defaultdict(lambda: float('inf') )

xlen = len(data)
ylen = len(data[0])

def get_neigh(i,j):
    res = []
    for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        if 0 <= x < xlen and 0 <= y < ylen:
            if data[x][y] == "." or data[x][y] == 'S':
                res.append((x,y))
    return res

counter = 0


while heap:
    dist, (x, y) = heapq.heappop(heap)
    if dist > STEPS:
        break
    for pos in get_neigh(x,y):
        if dists[pos] != dist +1:
            heapq.heappush(heap,(dist+1, pos))
        if dist != STEPS:
            dists[pos] = dist+1


for key in dists:
    if dists[key] == STEPS:
        counter += 1
print(counter)