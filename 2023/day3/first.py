f = open("inp.txt", "r")

arr = []
for line in f:
    arr.append(line)

col_len= len(arr)
row_len= len(arr[0]) - 1
def any_symbols_in_neighbour(arr, row, start):
    for i in range(-1,2):
        for j in range(-1,2):
            a = row + i
            b = start + j
            if a < 0 or a >= col_len or b >= row_len or b < 0:
                continue
            if not arr[a][b].isnumeric() and arr[a][b] != ".":
                return True
    return False

sum = 0
# print("row_len ", row_len)
for row in range(len(arr)):
    col = 0
    while col < row_len:
        # print("col: ", col)
        if arr[row][col] == ".":
            col = col + 1
            continue
        elif arr[row][col].isnumeric():
            start_ind = col
            num = str(arr[row][col])
            i = col+1
            while arr[row][i].isnumeric() and i < row_len:
                num = num + arr[row][i]
                i = i + 1
            end_ind = i - 1
            if any(any_symbols_in_neighbour(arr,row, ind) for ind in range(start_ind,end_ind+1)):
                print(num)
                sum = sum + int(num)
            col = i
            # print(num)
        col = col + 1

print(sum)
