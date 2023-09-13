#TLE

n = int(input())
S = [input() for _ in range(n)]
cnt = []
cntId = []
find = False

for i in range(n):
    count = 0
    find = False
    for j in range(len(cnt)):
        if S[i] == cntId[j]:
            cnt[j] += 1
            find = True
            count = cnt[j]
            break
    if find:
        print(S[i] + "(" + str(count) + ")")
    else:
        cntId.append(S[i])
        cnt.append(0)
        print(S[i])