# AC

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        exit()

    ans = "NONE"
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i] + a[j] <= m:
                if ans == "NONE":
                    ans = a[i] + a[j]
                else:
                    ans = max(ans, a[i] + a[j])
    print(ans)
