f = open("inp.txt", "r")

def minimum_set_of_cubes(game):
    norm =  {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }
    for turn in game.split(";"):
        for draw in turn.split(","):
            count = int(draw.split()[0])
            color = draw.split()[1]
            if norm[color] < count:
                norm[color] = count
    return norm["blue"] * norm["green"] * norm["red"]

sum = 0
for line in f:
    colon = line.split(":")
    id = int(colon[0].split()[1])
    sum = sum + minimum_set_of_cubes(colon[1])

print(sum)