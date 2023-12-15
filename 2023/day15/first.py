f = open("inp.txt","r")

def hash_algo(string):
    res = 0
    for ch in string:
        res += ord(ch)
        res *= 17
        res = res % 256
    return res

data = f.read().split(",")
sum = 0
for string in data:
    sum += hash_algo(string)
print(sum)
print(hash_algo("qp"))