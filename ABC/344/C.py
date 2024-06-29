from collections import defaultdict

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

d = defaultdict(int)
for ai in a:
    for bi in b:
        for ci in c:
            d[ai + bi + ci] += 1

for xi in x:
    if d[xi] != 0:
        print("Yes")
    else:
        print("No")
