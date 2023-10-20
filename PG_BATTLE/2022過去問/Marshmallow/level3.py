n, p, q = map(int, input().split())
grade = []

for i in range(n):
    a, b = map(int, input().split())
    grade.append(p * a + q * b)


grade, idx = zip(*sorted(zip(grade, range(1, n + 1)), reverse=True))

rank = []
for i in range(n):
    if i == 0 or grade[i] != grade[i - 1]:
        rank.append(i + 1)
    else:
        rank.append(rank[i - 1])

idx, grade, rank = zip(*sorted(zip(idx, grade, rank)))

for i in rank:
    print(i)
