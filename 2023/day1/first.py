f = open("input.txt", "r")


sum = 0

for x in f:
    isFirst = True
    firstDigit = ""
    lastDigit = ""
    for char in x:
        if char.isnumeric():
            if isFirst:
                isFirst = False
                firstDigit = char
            lastDigit=char
    sum = sum + int(firstDigit + lastDigit)


print(sum)