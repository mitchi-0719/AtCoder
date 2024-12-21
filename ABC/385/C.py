from collections import defaultdict

# n = int(input())
# h = list(map(int, input().split()))
n = 3000
h = [1 for i in range(n - 1)] + [0]
dic = defaultdict(list)
ans = 1

if len(set(h)) == 1:
    print(n)
    exit()

for i in range(n):
    dic[h[i]].append(i)

for v in sorted(dic.values(), key=len, reverse=True):
    l = len(v)
    if l == 1:
        continue

    if l <= ans:
        break

    for s in range(l):
        for s2 in range(s + 1, l):
            cnt = 1
            diff = v[s2] - v[s]
            now = v[s]
            for i in range(s2, l):
                if v[i] - now == diff:
                    cnt += 1
                    now = v[i]
                elif v[i] - now < diff:
                    continue
                else:
                    ans = max(ans, cnt)
                    break
            ans = max(ans, cnt)

print(ans)
