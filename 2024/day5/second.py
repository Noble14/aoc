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
    j = 0
    while j < lenj:
        print("checking ", prods[i][j])
        curr = prods[i][j]
        if curr in rules:
            currRules = rules[curr]
            change = []
            k = 0
            while k < j:
                print(prods[i][k])
                if any(x == prods[i][k] for x in currRules):
                    notOk = True
                    print("not ok: ", prods[i][k])
                    change.append(k)
                k += 1
            removed = 0
            change.sort()
            for ch in change:
                prods[i].pop(ch -removed)
                removed += 1

            prods[i].pop(j-removed)
            prods[i].insert(j - removed-1, curr)
            for h in range(removed):
                prods[i].insert(j - removed+ h, change[h])
        j += 1

    # if not notOk:
    #     num = lenj / 2
    #     summ += prods[i][int(num)]
    print(prods[i])

print(summ)

