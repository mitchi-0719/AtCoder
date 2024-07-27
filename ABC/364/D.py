import bisect

n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))

for i in range(q):
    b, k = map(int, input().split())
    print(bisect.bisect(a, b))
