n = int(input())
a = [-1] + [int(input()) for _ in range(n)]
v = [False for _ in range(n + 1)]

now = 1
cnt = 0


while True:
    if v[now]:
        print(-1)
        break

    v[now] = True
    now = a[now]
    cnt += 1

    if now == 2:
        print(cnt)
        break
