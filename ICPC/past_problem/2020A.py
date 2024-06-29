while 1:
    n = int(input())
    if n == 0:
        break

    d = list(input().split())
    ans = 0
    for i in range(n - 3):
        if d[i : i + 4] == ["2", "0", "2", "0"]:
            ans += 1

    print(ans)
