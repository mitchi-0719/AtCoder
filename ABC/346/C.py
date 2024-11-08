n, k = map(int, input().split())
a = set(map(int, input().split()))

ans = (k * (k + 1)) // 2
for ai in a:
    ans -= ai if ai <= k else 0

print(ans)
