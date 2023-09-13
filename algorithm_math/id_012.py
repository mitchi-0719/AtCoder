import math

n = int(input())

i = 2
while i <= math.sqrt(n):
    if n % i == 0:
        print("No")
        exit()
    i += 1

print("Yes")