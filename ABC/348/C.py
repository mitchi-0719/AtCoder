from collections import defaultdict

n = int(input())
d = defaultdict(lambda: float("inf"))

for i in range(n):
    a, c = map(int, input().split())
    if d[c] > a:
        d[c] = a

print(max(d.values()))
