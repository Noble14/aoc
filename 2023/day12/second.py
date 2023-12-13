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

DP = {}
def sol(line, nums, i, bi, current):
    key = (i, bi, current)
    if key in DP:
        return DP[key]
    if len(line) == i:
        if bi == len(nums) and current == 0:
            return 1
        if bi == len(nums)-1 and current == nums[bi]:
            return 1
        else:
            return 0
    ret = 0
    for c in ["#", "."]:
        if line[i] == c or line[i] == '?':
            if c == "." and current ==0:
                ret += sol(line, nums, i+1, bi, current)
            elif c == "#":
                ret += sol(line, nums, i+1,bi, current+1)
            elif c == '.' and current > 0 and bi < len(nums) and nums[bi] == current:
                ret += sol(line, nums, i+1, bi+1, 0)
    DP[key] = ret
    return ret


res = 0
for line in f:
    line, nums = line.split()
    line = '?'.join([line, line, line, line, line])
    nums = ','.join([nums, nums, nums, nums, nums])
    nums = list(map(lambda x: int(x) ,nums.split(",")))
    DP.clear()
    r = sol(line, nums, 0, 0, 0)
    res += r

print(res)