while True:
    n = int(input())
    if n == 0:
        exit()

    a = list(map(int, input().split()))

    ans = 0
    for i in range(1, n):
        d = abs(a[i] - 2023)
        if abs(a[ans] - 2023) > d:
            ans = i

    print(ans + 1)
