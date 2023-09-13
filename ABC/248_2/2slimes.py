#正解

a, b, k = map(int, input().split())

n = 0
while True:
    if b <= a * (k ** n):
        break
    n += 1
print(n)