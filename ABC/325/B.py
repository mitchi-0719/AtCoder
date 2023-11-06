n = int(input())
w, x = [], []

for i in range(n):
    W, X = map(int, input().split())
    w.append(W)
    x.append(X)

ans = 0

for i in range(24):
    cnt = 0
    for j in range(n):
        if 9 <= (i + x[j]) % 24 <= 17:
            cnt += w[j]
    ans = max(ans, cnt)

print(ans)
