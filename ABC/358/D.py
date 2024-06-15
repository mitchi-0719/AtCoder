from collections import defaultdict
import bisect

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
buy = []

for bi in b:
    i = bisect.bisect_left(a, bi)
    if len(buy) == 0:
        buy.append(i)
    elif buy[-1] >= i:
        buy.append(buy[-1] + 1)
    else:
        buy.append(i)

if max(buy) >= n:
    print(-1)
    exit()

ans = 0
for _buy in buy:
    ans += a[_buy]

print(ans)
