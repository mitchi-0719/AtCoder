from collections import defaultdict

n = int(input())
h = list(map(int, input().split()))

d = defaultdict(list)
ans = 1

for i in range(n):
    d[h[i]].append(i)

# for v in d.items():
#     for k in range(ans, )
