n, m, p = map(int, input().split())

cnt = 0
while True:
    if n < m:
        print(cnt)
        exit()
    m += p
    cnt += 1