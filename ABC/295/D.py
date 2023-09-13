from itertools import groupby

s = input()
n = len(s)

cnt = 0

for l in range(n):
    for r in range(l+1, n):
        good = True
        if l+r % 2 == 0: continue
        for k, g in groupby(sorted(s[l:r+1])):
            if len(list(g)) % 2 == 1:
                good = False
                break
        if good:
            cnt += 1

print(cnt)