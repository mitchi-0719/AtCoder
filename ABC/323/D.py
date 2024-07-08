from collections import defaultdict

n = int(input())
d = defaultdict(int)
s_sum = 0
merge = 0

for i in range(n):
    si, ci = map(int, input().split())
    s_sum += ci
    d[si] += ci
    while True:
        cnt = d[si]
        if cnt >= 2:
            d[si] = (cnt) % 2
            si *= 2
            merge += cnt // 2
            d[si] += cnt // 2
        else:
            break

print(s_sum - merge)
