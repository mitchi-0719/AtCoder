from collections import defaultdict

q = int(input())

s = set()
d = defaultdict(int)
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        s.add(query[1])
        d[query[1]] += 1
    elif query[0] == 2:
        d[query[1]] -= 1
        if d[query[1]] == 0:
            s.remove(query[1])
    else:
        print(len(s))
