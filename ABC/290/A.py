n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for b in list(map(int, input().split())):
    ans += a[b - 1]

print(ans)
