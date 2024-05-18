a, b, c, d = map(int, input().split())

ans = 0
if b % 2 == d % 2:
    times_4 = abs(a - c) // 4
    ans += times_4 * 4 * abs(b - d) // 2
    d -= b

print(ans)
