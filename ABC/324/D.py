# 解説AC

from math import sqrt

n = int(input())
s = list(input())
s.sort()

max_value = pow(10, n)

ans = 0

i = 0
while i * i < max_value:
    t = str(i * i)
    t += "0" * (n - len(t))
    t = list(t)
    t.sort()
    if t == s:
        ans += 1
    i += 1

print(ans)