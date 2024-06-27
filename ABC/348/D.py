h, w = map(int, input().split())
a = []
s = None
t = None

for i in range(h):
    ai = list(input())
    if not s and "S" in ai:
        s = (i, ai.index("S"))

    if not t and "T" in ai:
        t = (i, ai.index("T"))


n = int(input())
r, c, e = [], [], []

for i in range(n):
    ri, ci, ei = map(int, input().split())
    r.append(ri)
    c.append(ci)
    e.append(ei)

print(s, t)
