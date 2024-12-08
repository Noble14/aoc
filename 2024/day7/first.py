f = open("inp.txt", "r")
data = f.read().strip().split("\n")
for i in range(len(data)):
    summ, others = data[i].split(":")
    arr = others.strip().split(" ")
    arr = [int(x) for x in arr]
    data[i] = (int(summ), arr)

def solve_line(Acc, Numbers, Sum):
    return do_solve_line(Acc, Numbers, Sum, True) or do_solve_line(Acc, Numbers, Sum, False)

def do_solve_line(Acc, Numbers, Sum, IsAdd):
    if len(Numbers) == 1:
        if IsAdd:
            return Acc + Numbers[0] == Sum
        else:
            return Acc * Numbers[0] == Sum
    if IsAdd:
        newSum = Acc + Numbers[0]
        if newSum > Sum:
            return False
    else:
        newSum = Acc * Numbers[0]
        if newSum > Sum:
            return False
    A = do_solve_line(newSum, Numbers[1:], Sum, True)
    if A:
        return True
    B = do_solve_line(newSum, Numbers[1:], Sum, False)
    return B

c = 0
for i in range(len(data)):
    if solve_line(data[i][1][0], data[i][1][1:], data[i][0]):
        c += data[i][0]
print(c)


