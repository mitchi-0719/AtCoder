n, k = map(int, input().split())
a = set(list(map(int, input().split())) + [k + 1, 0])
a = sorted([i for i in list(a) if i <= k + 1])

ans = 0
for i in range(len(a) - 1):
    n1 = (a[i] * (a[i] + 1)) // 2
    n2 = (a[i + 1] * (a[i + 1] - 1)) // 2
    ans += n2 - n1

print(ans)
