f = open("inp.txt","r")

def hash_algo(string):
    res = 0
    for ch in string:
        res += ord(ch)
        res *= 17
        res = res % 256
    return res

data = f.read().split(",")
boxes =  []
for i in range(256):
    boxes.append([])
sum = 0
for string in data:
    if string[-1] == '-':
        label = hash_algo(string[:-1])
        boxes[label] = [item for item in boxes[label] if item[0] != string[:-1]]
    else:
        labelstr, fl = string.split("=")
        label = hash_algo(labelstr)
        found = False
        for idx,item in enumerate(boxes[label]):
            if item[0] == labelstr:
                boxes[label][idx] = (labelstr, int(fl))
                found = True
                break
        if found:
            continue
        boxes[label].append((labelstr, int(fl)))

for i,box in enumerate(boxes):
    for j, (l, num) in enumerate(box):
        sum += (i+1) * (j+1) * num
print(sum)