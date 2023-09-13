# AC

a, b = map(int, input().split())

a -= 1
b -= 1

if a // 3 == b // 3 and a % 3 - b % 3 == -1:
    print("Yes")
else:
    print("No")