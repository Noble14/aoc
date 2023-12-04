f = open("inp", "r")


def get_numbers(line):
    game , numbers = line.split(":")
    own, winning = numbers.split("|")
    return [winning.split() , own.split()]

sum = 0
for line in f:
    winning, numbers = get_numbers(line)
    count = 0
    for num in winning:
        if any(i == num for i in numbers):
            count = count + 1
    sum = sum + (0 if count == 0 else 2 ** (count-1))

print(sum)