f = open("inp.txt", "r")
data = f.read().strip().split("\n")
for i in range(len(data)):
    summ, others = data[i].split(":")
    arr = others.strip().split(" ")
    arr = [int(x) for x in arr]
    data[i] = (int(summ), arr)

def solve_line(Acc, Numbers, Sum):
    A = do_solve_line(Acc, Numbers, Sum, "+")
    if A:
        return True
    B = do_solve_line(Acc, Numbers, Sum, "*")
    if B:
        return True
    C = do_solve_line(Acc, Numbers, Sum, "|")
    return C


def do_solve_line(Acc, Numbers, Sum, Operator):
    if len(Numbers) == 1:
        if Operator == "+":
            return Acc + Numbers[0] == Sum
        elif Operator == "*":
            return Acc * Numbers[0] == Sum
        else:
            return int(str(Acc) + str(Numbers[0])) == Sum
    if Operator == "+":
        newSum = Acc + Numbers[0]
    elif Operator == "*":
        newSum = Acc * Numbers[0]
    else:
        newSum = int(str(Acc) + str(Numbers[0]))
    if newSum > Sum:
        return False
    A = do_solve_line(newSum, Numbers[1:], Sum, "|")
    if A:
        return True
    B = do_solve_line(newSum, Numbers[1:], Sum, "*")
    if B:
        return True
    C = do_solve_line(newSum, Numbers[1:], Sum, "+")
    return C

c = 0
for i in range(len(data)):
    if solve_line(data[i][1][0], data[i][1][1:], data[i][0]):
        c += data[i][0]
print(c)


