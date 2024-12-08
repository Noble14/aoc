f = open("inp.txt", "r")
rulesdata, prods = f.read().strip().split("\n\n")
rulesdata = rulesdata.split("\n")
rules = {}
for i in range(len(rulesdata)):
    X , Y = rulesdata[i].split("|")
    X = int(X)
    Y = int(Y)
    if X not in rules:
        rules[X] = {Y}
    else:
        rules[X].add(Y)

prods = prods.split("\n")
for i in range(len(prods)):
    prods[i] = prods[i].split(",")
    for j in range(len(prods[i])):
        prods[i][j] = int(prods[i][j])

# print(rules)

summ = 0
for i in range(len(prods)):
    notOk = False
    lenj = len(prods[i])
    for j in range(lenj):
        curr = prods[i][j]
        if curr in rules:
            currRules = rules[curr]
            intersect = (set(prods[i][:j])).intersection(currRules)
            notOk =  intersect != set()
            if notOk:
                break
    if not notOk:
        num = lenj / 2
        summ += prods[i][int(num)]

print(summ)

