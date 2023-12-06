import math

def break_the_record_count(b,c):
    a = -1
    res = (-b + (((b**2) - (4 * a * c))**0.5)) / (2*a)
    res = math.ceil(res)
    sec = b - res
    return abs(sec - res) + 1

f = open("inp", "r")
u, time = f.readline().split(":")
u, dist = f.readline().split(":")
b = int(time.replace(' ', ''))
c = int(dist.replace(' ', ''))
print(break_the_record_count(b,-c))
f.close()