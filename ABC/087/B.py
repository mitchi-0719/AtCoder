coins = [int(input()) for _ in range(3)]
x = int(input())

ans = 0
for i in range(coins[0] + 1):
    for j in range(coins[1] + 1):
        for k in range(coins[2] + 1):
            m = i * 500 + j * 100 + k * 50
            if m == x:
                ans += 1

print(ans)
