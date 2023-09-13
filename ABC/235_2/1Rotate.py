#正解

num = list(input())

for i in range(3):
    num[i] = int(num[i])

a = 0
b = 0
c = 0
for i in range(3):
    a += num[i] * (10 ** i)
    b += num[(i + 1) % 3] * (10 ** i)
    c += num[(i + 2) % 3] * (10 ** i)

print(a + b + c)