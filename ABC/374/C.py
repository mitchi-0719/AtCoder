n = int(input())
k = sorted(list(map(int, input().split())))

k_sum = sum(k)
s = 0
ans = float("inf")

for bit in range(2**(n-1)):
    s = k[-1]
    for i in range(n - 1):
        if bit & (1 << i):
            s+=k[i]
    ans = min(ans, max(k_sum - s, s))
print(ans)
