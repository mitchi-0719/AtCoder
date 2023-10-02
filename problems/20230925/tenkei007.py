import bisect

n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())

for i in range(q):
    b = int(input())
    idx = bisect.bisect(a, b)
    if idx == n:
        idx -= 1
    print(min(abs(b-a[idx]), abs(b-a[idx-1 if idx-1 >= 0 else idx])))

