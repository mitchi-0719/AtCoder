def solve(m, n):
    N = 10**7
    li = set([i for i in range(m, N + 1)])

    for i in range(m, N + 1):
        if i not in li:
            continue

        j = i * 2
        while j <= N:
            li.remove()
            j += i

    cnt = 0
    for i in range(N):
        if li[i]:
            cnt += 1
        if cnt == n + 1:
            print(i)
            return


while True:
    m, n = map(int, input().split())
    if m == n == 0:
        exit()
    solve(m, n)
