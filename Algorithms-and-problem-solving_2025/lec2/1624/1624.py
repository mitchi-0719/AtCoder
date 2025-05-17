def solve():
    n = int(input())
    if n == 0:
        return True

    a = list(map(int, input().split()))
    s = sum(a)

    ans = 0
    for i in range(n):
        ans += 1 if a[i] * n <= s else 0

    print(ans)


while 1:
    if solve():
        break
