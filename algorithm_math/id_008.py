n, s = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        cnt += (1 if i+j <= s else 0)

print(cnt)