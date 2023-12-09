f = open("inp", "r")

result = 0

for line in f:
    numbers = [list(map(lambda x: int(x) , line.split()))]
    allZero = False
    ind = 0
    while not allZero:
        allZero = True
        l = []
        i = 1
        while i < len(numbers[ind]):
            n = numbers[ind][i] - numbers[ind][i-1]
            l.append(n)
            allZero = l[i-1] == 0 and allZero
            i = i + 1
        ind = ind + 1
        numbers.append(l)
    res = list(map(lambda x: x[0], numbers))
    prev = 0
    j = len(res) -1
    while j >= 0:
        prev = res[j] - prev
        j = j -1
    result = result + prev

print(result)