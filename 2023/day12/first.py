f = open("inp.txt", "r")

def is_valid(line, nums):
    current = 0
    seen = []
    for c in line:
        if current > 0:
            if c == '.':
                seen.append(current)
                current = 0
        if c == '#':
            current += 1
    if current > 0:
        seen.append(current)
    return seen == nums

def sol(line, nums, i):
    if len(line) == i:
        return 1 if is_valid(line, nums) else 0
    if line[i] == '?':
        return sol(line[:i] + "#" + line[i+1:], nums, i+1) + sol(line[:i] + "." + line[i+1:], nums, i+1)
    else:
        return sol(line, nums, i+1)


res = 0
for line in f:
    line, nums = line.split()
    nums = list(map(lambda x: int(x) ,nums.split(",")))
    r = sol(line, nums, 0)
    res += r

print(res)