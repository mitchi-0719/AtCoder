from collections import defaultdict


n = int(input())
d = defaultdict(int)

ans = 0

for i in range(n):
    if i == 0:
        d[i] = sum([j + 1 for j in range(6)]) / 6
    else:
        max_p = max(d.values())
        c = int(max_p)
        d[i] = ((6 - c) / 6) * (sum([j for j in range(c + 1, 7)]) / (6 - c)) + (
            c / 6
        ) * d[i - 1]

print(d[n - 1])
