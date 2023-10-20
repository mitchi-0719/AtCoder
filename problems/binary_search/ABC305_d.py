n = int(input())
a = list(map(int, input().split()))
q = input()
l, r = [], []

for _ in range(q):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)

