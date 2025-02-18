import bisect

n = int(input())
a = list(map(int, input().split()))

ans = 0
for ai in a:
    i = bisect.bisect_left(a, ai * 2)
    ans += n - i

print(ans)
