f = open("inp", "r")

seeds = list(map(lambda x: int(x),f.readline().split(":")[1].split()))

def convert_seeds(seed, mapping):
    h = list(filter(lambda x:  seed < x[1]+x[2] and seed >= x[1] ,mapping))
    if h == []:
        return seed
    h = h[0]
    return seed - h[1] + h[0]
f.readline()
for para in f.read().split("\n\n"):
    lines = para.split("\n")
    mapping = list(map(lambda x: list(map(lambda y: int(y), x.split())),lines[1:]))
    # print(mapping)
    # print(lines[0])
    seeds = list(map(lambda x: convert_seeds(x, mapping),seeds))
    # print("mapped ",list(seeds))

print(seeds)
print(min(seeds))
