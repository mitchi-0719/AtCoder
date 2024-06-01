import itertools

n, m, k = map(int, input().split())
a = []
r = []

keys = [i for i in range(1, n + 1)]

for i in range(m):
    li = list(input().split())
    r.append(li.pop(-1))
    a.append(set([int(j) for j in li[1:]]))

ans = 0
for i in range(n + 1):
    for c in itertools.combinations(keys, i):
        correct = True
        for j in range(m):
            if r[j] == "o":
                if len(set(c) & a[j]) < k:
                    correct = False
                    break
            else:
                if len(set(c) & a[j]) >= k:
                    correct = False
                    break

        if correct:
            ans += 1

print(ans)
