while 1:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if ans + a[i] <= 300:
            ans += a[i]
    print(ans)
