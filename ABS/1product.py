a, b = list(map(int, input().split()))

x = a * b

if x % 2 == 0:
    print("Even")
else:
    print("Odd")