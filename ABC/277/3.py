#
n = int(input())
A = []
B = []
now = 1
top = []
allWay = {}

for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


def searchTop(now):
    if now in allWay:
        nowL = allWay[now]
    else:
        nowL = [i for i, x in enumerate(A) if x == now]
        allWay.setdefault(1, nowL)

    if nowL:
        for i in nowL:
            searchTop(i)
    else:
        top.append(now)

searchTop(1)
print(max(top))