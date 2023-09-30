n, m = map(int, input().split())
a = list(map(int, input().split()))

idx = 0
for i in range(1, n+1):
    print(a[idx] - i)
    if a[idx] == i:
        idx += 1