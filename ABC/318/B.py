n = int(input())

area = [["." for i in range(100)] for j in range(100)]

for i in range(n):
    a, b, c, d = map(int, input().split())

    for j in range(c, d+1):
        for k in range(a, b+1):
            area[j][k] = "#"

for i in 