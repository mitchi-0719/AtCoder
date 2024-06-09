n, a, b = map(int, input().split())

ans = 0
for i in range(n + 1):
    s = sum(list(map(int, str(i))))
    if a <= s <= b:
        ans += i

print(ans)
