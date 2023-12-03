f = open("inp.txt", "r")

arr = []
for line in f:
    arr.append(line)

col_len= len(arr)
row_len= len(arr[0]) - 1
def find_number(row, b):
    start_ind,end_ind = b, b
    while start_ind > 0 and row[start_ind-1].isnumeric():
        start_ind = start_ind - 1
    while end_ind < len(row) and row[end_ind+1].isnumeric():
        end_ind = end_ind + 1
    return {
        "number": int(row[start_ind:end_ind+1]),
        "ind" : max(end_ind, b) - b
    }

def are_there_neighbouring_numbers(arr, row, start):
    neighbours = []
    i = -1
    while i < 2:
        j = -1
        while j < 2:
            a = row + i
            b = start + j
            if a < 0 or a >= col_len or b >= row_len or b < 0:
                j = j + 1
                continue
            if arr[a][b].isnumeric():
                res = find_number(arr[a], b)
                neighbours.append(res["number"])
                j = j + res["ind"]
            j = j + 1
        i = i + 1
    if len(neighbours) == 2:
        return neighbours[0] * neighbours[1]
    return 0

sum = 0
for row in range(len(arr)):
    col = 0
    while col < row_len:
        if arr[row][col] != "*":
            col = col + 1
            continue
        else:
            sum = sum + are_there_neighbouring_numbers(arr,row,col)
        col = col + 1

print(sum)
