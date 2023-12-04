f = open("inp", "r")

def get_numbers(line):
    game , numbers = line.split(":")
    own, winning = numbers.split("|")
    return [int(game.split()[1]) ,winning.split() , own.split()]

sum = 0
dic = { }
def maybe_add_one(dic, key, value=1):
    if key in dic:
        dic[key] = dic[key] + value
    else:
        dic[key] = value

for line in f:
    game,winning, numbers = get_numbers(line)
    maybe_add_one(dic, game)
    count = 0
    for num in winning:
        if any(i == num for i in numbers):
            count = count + 1
    j = game + 1
    while j < game + count+1:
        maybe_add_one(dic, j, dic[game])
        j = j + 1
    sum = sum + dic[game]

print(sum)