
f = open("inp", "r")

inst = f.readline().strip()
f.readline()

d = {}

for line in f:
    dest, ways = line.split("=")
    left, right = ways.split(",")
    d[dest.strip()] = {
        "R" : right.strip().replace(")", ""),
        "L" : left.strip().replace("(", "")
    }

current = "AAA"
counter = 0
instLen = len(inst)
while current != "ZZZ":
    current = d[current][inst[counter % instLen]]
    counter = counter + 1

print(counter)
