
f = open("inp.txt", "r")
lines = f.read().strip().split("\n")

safesum = 0

for line in lines:
    numbers = line.split(" ")
    increasing = int(numbers[0]) - int(numbers[1]) < 0
    n = len(numbers)
    good = True
    i = 0
    while good and i < n -1:
        diff = int(numbers[i+1]) - int(numbers[i])
        ab = abs(diff)
        stillIncreasing = int(numbers[i]) - int(numbers[i+1]) < 0
        if not (ab > 0 and ab < 4 and not ( stillIncreasing != increasing)):
            good = False
        i += 1
    if good:
        safesum += 1

print(safesum)
