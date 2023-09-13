n, m = map(int, input().split())

li = [[] for _ in range(n)]
cnt = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    li[a-1].append(b)
    li[b-1].append(a)
    cnt[a-1] += 1
    cnt[b-1] += 1

for i in range(n):
    print(cnt[i], end=" ")
    li[i].sort()
    for j in li[i]:
        print(j, end=" ")
    print()
