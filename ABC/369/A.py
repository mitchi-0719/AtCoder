a, b = map(int, input().split())
cnt = 1

if a != b:
    cnt += 1

    if abs(a - b) % 2 == 0:
        cnt += 1

print(cnt)
