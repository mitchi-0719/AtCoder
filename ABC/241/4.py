# 

q = int(input())
cnt = {}

for i in range(q):
    query = map(int, input().split())

    if query[0] == 1:
        buffer = cnt
        cnt.setdefault(str(query[1]), 1)
        if buffer == cnt:
            cnt[str(query[1])] += 1
    elif query[0] == 2:

    else:
        