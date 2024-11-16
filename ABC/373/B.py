s = list(input())
n = len(s)
l = [i for i in range(n)]

s, l = zip(*sorted(zip(s, l)))

ans = 0
for i in range(n - 1):
    ans += abs(l[i + 1] - l[i])

print(ans)
