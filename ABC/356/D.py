mod = 998244353

n, m = map(int, input().split())

ans = 0
l = 60

for i in range(l):
    if m >> i & 1:
        c = 1 << i
        cnt = m // c * c
        ans += (cnt - 1) // 2 + 1
        if (cnt / c) % 2 == 1:
            ans += m % c

print(ans % mod)
