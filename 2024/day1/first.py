


f = open("inp.txt", "r")
data = f.read()
A = []
B = []

for i in data.strip().split("\n"):
    a = i.split(" ")
    A.append(int(a[0]))
    B.append(int(a[-1]))

summa = 0
n = len(A)

for i in range(n):
    diff = B[i] - A[i]
    summa += abs(diff)

print(summa)
