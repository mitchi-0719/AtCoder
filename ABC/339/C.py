n = int(input())
a = list(map(int, input().split()))

ans = 0
now = 0
for i in range(n):
    now += a[i]
    ans = min(ans, now)

print(ans * -1 + now)
