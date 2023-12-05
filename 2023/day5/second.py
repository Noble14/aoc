f = open("inp", "r")

seeds = list(map(lambda x: int(x),f.readline().split(":")[1].split()))
j = 0
all_seeds = []
while j < len(seeds):
    all_seeds.append([seeds[j], seeds[j+1]])
    j = j + 2

seeds = all_seeds

def get_intersect(a,b,x,y):
    if y < a or x > b:
        return False
    if x < a:
        if y > b:
            return [[a,b], [x,a-1], [b+1,y]]
        return [[a,y], [x, a-1]]
    if y <= b:
        return [[x, y]]
    return [[x, b], [b+1, y]]

f.readline() # for the empty line
for para in f.read().split("\n\n"):
    lines = para.split("\n")
    mapping = list(map(lambda x: list(map(lambda y: int(y), x.split())),lines[1:]))
    for i, [x,y] in enumerate(seeds):
        for a, b, c in mapping:
            res = get_intersect(b,b+c-1, x, x+y-1)
            if res == False:
                continue
            res  = list(map(lambda x: [x[0], x[1]-x[0] + 1] , res))
            seeds[i] = [res[0][0]+ a - b, res[0][1]]
            if len(res) > 1:
               for r in res[1:]:
                    seeds.append(r)
            break

print(min(seeds, key= lambda x: x[0]))
