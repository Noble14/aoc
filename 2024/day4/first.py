
f = open('input.txt', 'r')
data = f.read().strip().split('\n')


for i in range(len(data)):
    data[i] = list(data[i])


rows = len(data)
cols = len(data[0])

summ = 0
arr = ['X', 'M', 'A', 'S']
dirs = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]
for i in range(rows):
    for j in range(cols):
        if data[i][j] != 'X':
            continue
        for x, y in dirs:
            k = 0
            newi = i+(x*k)
            newj = j+(y*k)
            while k < 4 and data[newi][newj] == arr[k]:
                k += 1
                newi = i+(x*k)
                newj = j+(y*k)
                if newi< 0 or newi >= rows or newj < 0 or newj >= cols:
                    break
            if k == 4:
                summ += 1

print(summ)
