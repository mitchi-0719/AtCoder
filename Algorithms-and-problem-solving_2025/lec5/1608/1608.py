def solve():
    n = int(input())
    if n == 0:
        return 1

    a = sorted(list(map(int, input().split())))
    ans = float("inf")

    for i in range(n - 1):
        ans = min(ans, abs(a[i] - a[i + 1]))

    print(ans)


while not solve():
    ...
