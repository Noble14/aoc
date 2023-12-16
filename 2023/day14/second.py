import numpy as np
from collections import defaultdict
f = open("inp.txt","r")

def get_row_value(row):
    h = len(row)
    j = h
    sum = 0
    for i, el in enumerate(row):
        if el == "O":
            sum += h - i
    return sum

def convert_row(row,  reverse=False):
    row = list(row)
    if reverse:
        row.reverse()
    new_row =[]
    all_sum = 0
    sum = 0
    for i, el in enumerate(row):
        if el == "#":
            new_row = new_row + (["O"] * sum) + (["."] * (all_sum - sum)) + ["#"]
            sum, all_sum = 0, 0
            continue
        elif el == "O":
            sum += 1
        all_sum += 1
    new_row = new_row + (["O"] * sum) + (["."] * (all_sum - sum))
    if reverse:
        new_row.reverse()
    return new_row

#print(convert_row("OO.##O..#..O"))

data = f.read().split("\n")
new_data = []
for line in data:
    li = []
    for char in line:
        li.append(char)
    new_data.append(li)
data = new_data

def transform_array(arr, reverse=False):
    new_arr = []
    for line in arr:
        new_arr.append(convert_row(line, reverse))
    return np.array(new_arr)

def print_arr(arr):
    for line in arr:
        str = ""
        for char in line:
            str = str + char
        print(str)


def cycle(data):
    arr = np.array(data)
    arr = arr.transpose()
    arr = transform_array(arr).transpose()
    arr = transform_array(arr, False)
    arr = arr.transpose()
    arr = transform_array(arr, True).transpose()
    return transform_array(arr,True)


def solve(data):
    sum = 0
    data = data.transpose()
    for line in data:
        sum += get_row_value(line)

    return sum

scores = defaultdict(list)

arr = np.array(data)

t = 0
target = 10 ** 9
while t < target:
    t += 1
    data = cycle(data)
    score = solve(data)
    scores[score].append(t)
    steps= scores[score]
    if len(steps) >= 6:
        cyc_len = steps[-1] - steps[-2]
        if cyc_len == steps[-2] - steps[-3]:
            amt = (target-t) // cyc_len
            t += amt * cyc_len
print(solve(data))