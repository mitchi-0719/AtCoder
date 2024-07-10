n = int(input())

area = [["." for i in range(100)] for j in range(100)]

for i in range(n):
    a, b, c, d = map(int, input().split())

    for j in range(c, d):
        for k in range(a, b):
            area[j][k] = "#"

ans = 0
for i in range(100):
    for j in range(100):
        if area[i][j] == "#":
            ans += 1

print(ans)
