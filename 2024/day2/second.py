# f = open("inp.txt", "r")
# lines = f.read().strip().split("\n")

# safesum = 0

# for line in lines:
#     numbers = line.split(" ")
#     increasing = int(numbers[0]) - int(numbers[1]) < 0
#     n = len(numbers)
#     bad = 0
#     i = 0
#     while bad < 2 and i < n -1:
#         diff = int(numbers[i+1]) - int(numbers[i])
#         ab = abs(diff)
#         stillIncreasing = int(numbers[i]) - int(numbers[i+1]) < 0
#         if not (ab > 0 and ab < 4 and not ( stillIncreasing != increasing)):
#             bad += 1
#             del numbers[i+1]
#             n = n - 1
#         else:
#             i += 1
#     if bad < 2:
#         safesum += 1

# print(safesum)

def is_line_ok(numbers):
    increasing = int(numbers[0]) - int(numbers[1]) < 0
    n = len(numbers)
    i = 0
    while i < n -1:
        diff = int(numbers[i+1]) - int(numbers[i])
        ab = abs(diff)
        stillIncreasing = int(numbers[i]) - int(numbers[i+1]) < 0
        if not (ab > 0 and ab < 4 and not ( stillIncreasing != increasing)):
            return False
        i += 1
    return True

f = open("inp.txt", "r")
lines = f.read().strip().split("\n")

safesum = 0



for line in lines:
    numbers = line.split(" ")
    good = is_line_ok(numbers)
    i = 0
    n = len(numbers)
    while i < n and not good:
        lessnumbers = list(numbers)
        del lessnumbers[i]
        good = good or is_line_ok(lessnumbers)
        i += 1

    if good:
        safesum += 1

print(safesum)
