a, b = map(int, input().split())

ans = 0
cnt = 1
while True:
    if cnt >= b:
        print(ans)
        break

    cnt -= 1
    cnt += a
    ans += 1
