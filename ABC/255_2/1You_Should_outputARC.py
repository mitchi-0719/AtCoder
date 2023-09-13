#正解

r, c = map(int, input().split())

a = [input().split() for i in range(2)]

print(a[r - 1][c - 1])
