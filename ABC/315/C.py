n = int(input())

f, s = [], []

for i in range(n):
    F, S = map(int, input().split())
    f.append(F)
    s.append(S)

s, f = zip(*sorted(zip(s, f), reverse=True))

m = 0

for i in range(1, n):
    if f[0] == f[i]:
        m = max(m, s[0]+s[i]//2)
    else:
        m = max(m, s[0]+s[i])

print(m)