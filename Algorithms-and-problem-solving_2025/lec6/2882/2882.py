def solve():
    n, l, r = map(int, input().split())
    if n == 0:
        return 1

    a = [int(input()) for _ in range(n)]

    ans = 0
    for x in range(l, r + 1):
        for i in range(n):
            if x % a[i] == 0:
                if i % 2 == 0:
                    ans += 1
                break
        else:
            if n % 2 == 0:
                ans += 1

    print(ans)


while not solve():
    ...
