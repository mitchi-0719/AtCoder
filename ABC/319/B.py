n = int(input())
divisor = [i for i in range(1, 10) if n % i == 0]

for i in range(n+1):
    isDivide = False
    for j in divisor:
        if i % (n//j) == 0:
            print(j, end="")
            isDivide = True
            break
    isDivide or print("-", end="")