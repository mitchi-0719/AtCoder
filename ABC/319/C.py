import itertools

c = []

for i in range(3):
    C = list(input().split())
    c.append(C)

lists = []

cnt = 0
li = [c[0][0], c[1][1], c[2][2]]

if len(set(li)) == 2:
    lists.append(li)

li = [c[0][2], c[1][1], c[2][0]]
if len(set(li)) == 2:
    lists.append(li)

for i in range(3):
    li = [c[i][0], c[i][1], c[i][2]]
    if len(set(li)) == 2:
        lists.append(li)

    li = [c[0][i], c[1][i], c[2][i]]
    if len(set(li)) == 2:
        lists.append(li)

all_count = 362880

str_c = [str(c[i][j]) for i in range(3) for j in range(3)]

for l in itertools.permutations(str_c):
    for m in lists:
        if "".join(m) in "".join(l):
            cnt += 1

print(cnt, all_count)
print(cnt / all_count)
