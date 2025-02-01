n, r = map(int, input().split())
ans = r

for _ in range(n):
    d, a = map(int, input().split())

    if d == 1:
        if 1600 <= ans <= 2799:
            ans += a
    else:
        if 1200 <= ans <= 2399:
            ans += a

print(ans)
