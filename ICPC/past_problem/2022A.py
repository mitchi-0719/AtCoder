while True:
    n = int(input())
    if n == 0:
        exit()

    v = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if v[i - 1] < v[i] and v[i + 1] < v[i]:
            ans += 1

    print(ans)
