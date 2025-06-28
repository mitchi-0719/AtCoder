def solve():
    N, M = map(int, input().split())
    if N == 0:
        exit()

    cnt = [0] * (N + 1)
    q = []
    for _ in range(M):
        a, b = map(int, input().split())
        q.append((a, b))

    for a, b in reversed(q):
        if cnt[b] == 0:
            cnt[a] += 1
        else:
            cnt[b] -= 1
            cnt[a] += 1
    print(sum(cnt))


while 1:
    solve()
