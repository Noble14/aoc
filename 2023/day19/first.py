f = open("inp.txt", "r")

rules, values = f.read().split("\n\n")

D =  {}

def str_to_dict(str):
    str = str[1:-1]
    vals = str.split(",")
    res = {}
    for val in vals:
        a, b = val.split("=")
        res[a] = int(b)
    return(res)
def convert_fun(fun):
    res = {}
    fun , nextwf = fun.split(":")
    res["fun"] = lambda x: eval(f"x['{fun[0]}'] {fun[1]} {fun[2:]}")
    res["next"] = nextwf
    return res


for rule in rules.split("\n"):
    id, rule = rule.split("{")
    rule = rule[:-1]
    funs = rule.split(",")
    last = funs[-1]
    funs = funs[:-1]
    funs = list(map(lambda x: convert_fun(x), funs))
    D[id] = {
        "funs" : funs,
        "last" : last
    }


#print(D)
new_values = []
for value in values.split("\n"):
    d = str_to_dict(value)
    d["wf"] = "in"
    new_values.append(d)

ret = D["in"]["funs"][0]["fun"]({"s" : 3000})
accepted = []
while new_values:
    val = new_values[0]
    rule = D[val["wf"]]
    end = True
    nextwf = None
    for fun in rule["funs"]:
        if fun["fun"](val):
            nextwf = fun["next"]
            end = False
            break
    if end:
        nextwf = rule["last"]
    val["wf"] = nextwf
    if nextwf == "R":
        new_values.remove(val)
    elif nextwf == "A":
        accepted.append(val)
        new_values.remove(val)

sum = 0
for ac in accepted:
    for i in "xmas":
        sum += ac[i]
print(sum)
