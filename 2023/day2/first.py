f = open("inp.txt", "r")

def is_turn_possible(turn,red, green, blue):
    norm =  {
        "red" : red,
        "green" : green,
        "blue" : blue
    }
    for draw in turn.split(","):
        count = int(draw.split()[0])
        color = draw.split()[1]
        if norm[color] < count:
            return False
    return True

sum = 0
for line in f:
    colon = line.split(":")
    id = int(colon[0].split()[1])
    if all(is_turn_possible(turn, 12, 13,14) for turn in colon[1].split(";")):
        sum = sum + id

print(sum)