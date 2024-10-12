from collections import defaultdict

s = input()
n = len(s)
d = defaultdict(list)

for i in range(n):
    d[s[i]].append(i)

ans = 0
for li in d.values():
    ln = len(li)
    if ln == 1:
        continue
    if ln == 2:
        ans += abs(li[0] - li[1]) - 1
        continue

    sum = 0
    diff = 0
    for i in range(1, ln):
        temp = li[i] - li[0]
        sum += temp - 1
        if i != 1:
            diff += temp * (ln - i) + 1

    ans += sum * (ln - 1) - diff

print(ans)
