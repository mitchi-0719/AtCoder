import bisect

n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

for ai in a:
    i = bisect.bisect_left(a, ai - x)
    if 0 <= i < n and ai - a[i] == x:
        print("Yes")
        exit()

print("No")
