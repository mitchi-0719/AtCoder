n = int(input())
l, r = [], []

for _ in range(n):
    a, s = input().split()

    if s == "L":
        l.append(int(a))
    else:
        r.append(int(a))


ans = 0
for i in range(len(l) - 1):
    ans += abs(l[i] - l[i + 1])

for i in range(len(r) - 1):
    ans += abs(r[i] - r[i + 1])

print(ans)
