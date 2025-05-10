def solve():
    n, m = map(int, input().split())
    if n == m == 0:
        return True

    a = list(map(int, input().split()))
    ans = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] <= m:
                ans = max(ans, a[i] + a[j])

    print(ans if ans != 0 else "NONE")


while 1:
    if solve():
        break
