f = open("input.txt", "r")

start =  (0,0)
def get_dir(char):
    if char == 0:
        return (0, 1)
    if char == 2:
        return (0, -1)
    if char == 1:
        return (1, 0)
    if char == 3:
        return (-1, 0)

curr = (0,0)
coords = []
sum1 = 0
for line in f:
    dir, cnt, color = line.split()
    cnt = color[2:-2]
    cnt = int(cnt,16)
    dir = int(color[-2])
    sum1 += cnt
    dx, dy = get_dir(dir)
    x ,y = curr
    curr = (x + (cnt)*dx, y +(cnt)*dy)
    coords.append(curr)


sum = 0
coords.reverse()
for i in range(len(coords)-1):
    a, b = coords[i+1]
    x, y = coords[i]
    sum += (x * b) - (a * y)

#a, b = coords[0]
#x, y = coords[-1]

#sum += x * b - a * y
i = (sum / 2) + 1 - sum1 // 2
print(int(i + sum1))