f = open("inp.txt","r")

def get_row_value(row):
    h = len(row)
    j = h
    sum = 0
    for i, el in enumerate(row):
        if el == "O":
            sum += h
            h -= 1
        elif el == "#":
            h = j - i - 1
    return sum

st = "OO.#O....O"
print(len(st))
print(get_row_value(st))

data = f.read()
terV = data.split("\n")
terH = []
for i in range(len(terV[0])):
    line = []
    for j in range(len(terV)):
        line.append(data[j*(len(terV[0])+1)+i])
    terH.append(line)
res = 0
for line in terH:
    res += get_row_value(line)

print(res)