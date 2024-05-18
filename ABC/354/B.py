n = int(input())

s, c = [], []
for i in range(n):
    _s, _c = input().split()
    s.append(_s)
    c.append(int(_c))

t = sum(c)

print(sorted(s)[t % n])
