n, s, m, l = map(int, input().split())

sum = 10**9

for i in range(100 // 12 + 10):
    for j in range(100 // 8 + 10):
        for k in range(100 // 6 + 10):
            if i * 12 + j * 8 + k * 6 >= n:
                sum = min(sum, i * l + j * m + k * s)

print(sum)
