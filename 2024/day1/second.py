
f = open("inp.txt", "r")
data = f.read()
A = []
B = []

for i in data.strip().split("\n"):
    a = i.split(" ")
    A.append(int(a[0]))
    B.append(int(a[-1]))

A.sort()
B.sort()

summa = 0

i, j = 0, 0
n = len(A)

while i < n and j < n:
    currLeft = A[i]
    multiplierLeft = 1
    while i < n - 1 and A[i] == A[i+1]:
        multiplierLeft += 1
        i += 1
    multiplierRight = 0
    while B[j] == currLeft and j < n:
        multiplierRight += 1
        j += 1
    summa += multiplierLeft * currLeft * multiplierRight
    i += 1
    while j < n-1 and B[j] < A[i]:
        j += 1

print(summa)
