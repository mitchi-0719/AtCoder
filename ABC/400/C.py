import math

n = int(input())

cnt = int(math.log2(n)) - 1
i = 3
while True:
    t = i**2
    if t > n:
        break

    i += 1


print(cnt)
