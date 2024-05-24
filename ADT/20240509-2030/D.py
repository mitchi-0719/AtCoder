n = int(input())
a = [input() for _ in range(n)]

m = 0
d_list = [[i, j] for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]

for i in range(n):
    for j in range(n):
        for d in d_list:
            temp = 0
            di = 0
            dj = 0
            for k in range(n):
                temp = temp * 10 + int(a[(i + di) % n][(j + dj) % n])
                di += d[0]
                dj += d[1]
            m = max(m, temp)

print(m)
