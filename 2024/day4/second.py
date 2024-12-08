f = open('input.txt', 'r')
data = f.read().strip().split('\n')


for i in range(len(data)):
    data[i] = list(data[i])


rows = len(data)
cols = len(data[0])

dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
summ = 0
for i in range(rows-2):
    newi = i+1
    for j in range(cols-2):
        newj = j+1
        if data[newi][newj] != 'A':
            continue
        AllSOrM = True
        for dx, dy in dirs:
            AllSOrM = AllSOrM and (data[newi+dx][newj+dy] == 'S' or data[newi+dx][newj+dy] == 'M')

        PairsAreDifferent = data[newi + 1][newj + 1] != data[newi - 1][newj - 1]
        PairsAreDifferent1 = data[newi - 1][newj + 1] != data[newi + 1][newj - 1]

        if AllSOrM and PairsAreDifferent and PairsAreDifferent1:
            print(newi, newj)
            summ += 1

print(summ)
