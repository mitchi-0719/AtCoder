from collections import defaultdict


s = input()
n = len(s)
d = defaultdict(int)

for si in s:
    d[si] += 1

ans = 1 if max(d.values()) != 1 else 0
for i in range(25):
    for j in range(i + 1, 26):
        ans += d[chr(ord("a") + i)] * d[chr(ord("a") + j)]

print(ans)
