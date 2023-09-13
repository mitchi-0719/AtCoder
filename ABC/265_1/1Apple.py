#正解

x, y, n = map(int, input().split())

x_cnt = n % 3
y_cnt = n // 3

ans = x_cnt * x + y_cnt * y

if x * n < ans:
    print(x * n)
else:
    print(ans)