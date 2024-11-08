from collections import defaultdict

h, w, m = map(int, input().split())
t, a, x = [], [], []

cnt = defaultdict(int)
cnt[0] = h * w

for i in range(m):
    query = list(map(int, input().split()))
    t.append(query[0])
    a.append(query[1])
    x.append(query[2])


print(len(cnt.values()) - list(cnt.values()).count(0))
for k, v in sorted(cnt.items()):
    if v != 0:
        print(k, v)
