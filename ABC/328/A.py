n, x = map(int, input().split())
s = list(map(int, input().split()))

ans = 0
for i in s:
    ans += i if i <= x else 0

print(ans)
