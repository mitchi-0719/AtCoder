n, s, k = map(int, input().split())

ans = 0
for i in range(n):
    p, q = map(int, input().split())
    ans += p * q

print(ans + (0 if ans >= s else k))
