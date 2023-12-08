import math
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
current = list(filter(lambda x: x[2] == 'A', d.keys()))
numbers=[]
def all_ended(nodes,count):
    if nodes == []:
        return True
    for i,node in enumerate(nodes):
        if node[2] == 'Z':
            numbers.append(count)
            current.remove(node)
    return False
counter = 0
instLen = len(inst)
while not all_ended(current,counter):
    current = list(map(lambda x:d[x][inst[counter % instLen]] , current))
    counter = counter + 1

def get_prime_factors(number):
    i = 2
    d = {}
    rest = number
    while  rest != 1:
        if rest % i == 0:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
            rest = rest / i
        else:
            i=i+1
    return d

numbers = list(map(lambda x: get_prime_factors(x), numbers))

unique = {}

for num in numbers:
    for x in num:
        if x not in unique:
            unique[x] = num[x]
        else:
            if unique[x] < num[x]:
                unique[x] = num[x]

prod = 1
for x in unique:
    prod = prod * x ** unique[x]
print(prod)