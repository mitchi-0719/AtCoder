# AC

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        exit()

    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(m)]

    a_sum = sum(a)
    b_sum = sum(b)

    ans = [-1, -1]
    diff = a_sum - b_sum

    for i in range(n):
        for j in range(m):
            if (a[i] - b[j]) * 2 == diff:
                if ans == [-1, -1] or a[i] + b[j] < a[ans[0]] + b[ans[1]]:
                    ans = [i, j]

    if ans == [-1, -1]:
        print(-1)
    else:
        print(a[ans[0]], b[ans[1]])
