f = open("inp.txt", "r")

def line_sym(line, i, diff):
    j = 1
    end = min(len(line)-i, i)+1
    while j < end  and diff < 2:
        if line[i-j] != line[i+j-1]:
            diff += 1
        j += 1
    return diff

def all_lines_sym(lines, i):
    diff = 0
    for line in lines:
        diff = line_sym(line, i, diff)
        if diff > 1:
            return False
    return diff == 1



def mirror_vertical(map):
    for i in range(1,len(map[0])):
        if all_lines_sym(map,i):
            return [True, i]
    return [False, 0]

maps = f.read().split("\n\n")
sum = 0
for ter in maps:
    terV = ter.split("\n")
    l, num = mirror_vertical(terV)
    if l:
        sum += num
    else:
        terH = []
        for i in range(len(terV[0])):
            line = []
            for j in range(len(terV)):
                line.append(ter[j*(len(terV[0])+1)+i])
            terH.append(line)
        l, num = mirror_vertical(terH)
        sum += num * 100

print(sum)