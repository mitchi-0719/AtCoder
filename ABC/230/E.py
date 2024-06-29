import math

n = int(input())

l = n - n // 2
ans = l
for i in range(1, int(math.sqrt(n) + 1)):
    p = n // i
    print(i, p)
    ans += p
    if p <= l and p != n // p:
        print(i, n // p)
        ans += n // p


print(ans)

s = 0
for i in range(1, n + 1):
    s += n // i
print(s)
