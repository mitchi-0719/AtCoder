n, m = map(int, input().split())
a = list(map(int, input().split()))
idx = [i for i in range(n)]
a_sort, idx = zip(*sorted(zip(a, idx), reverse=True))
scores = [i + 1 for i in range(n)]
solves = [set() for _ in range(n)]

for i in range(n):
    s = input()
    for j, si in enumerate(s):
        if si == "o":
            scores[i] += a[j]
            solves[i].add(j)

scores_sort = sorted(scores, reverse=True)
for i in range(n):
    score = scores[i]
    cnt = 0
    max_score = scores_sort[0] if score != scores_sort[0] else scores_sort[1]
    if score > max_score:
        print(cnt)
        continue

    for j in range(m):
        if idx[j] not in solves[i]:
            cnt += 1
            score += a_sort[j]

        if score > max_score:
            print(cnt)
            break
