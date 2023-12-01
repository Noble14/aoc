
f = open("input.txt", "r")

digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

def startingWithDigitString(line, index):
    i = 0
    while i < len(digits):
        res = line.find(digits[i], index, index + len(digits[i]))
        if res == index:
            return i + 1
        i = i + 1
    return -1

sum = 0

for x in f:
    isFirst = True
    firstDigit = ""
    lastDigit = ""
    index = 0
    while index < len(x):
        char=x[index]
        res = startingWithDigitString(x, index)
        if res > -1:
            # index = index + len(digits[res-1])-1
            digit = str(res)
        elif char.isnumeric():
            digit = char
        else:
            index = index + 1
            continue
        if isFirst:
            isFirst = False
            firstDigit = digit
        lastDigit = digit
        index = index + 1
    sum = sum + int(firstDigit + lastDigit)


print(sum)