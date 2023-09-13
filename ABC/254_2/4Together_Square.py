#不正解

n = int(input())

squares = [i**2 for i in range(1, n + 1)]

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(n):
            if i * j == squares[k]:
                count += 1
                break
print(count)