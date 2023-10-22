n = int(input())
a = list(map(int, input().split()))

p = 1
for i in a:
    p *= i

if p > 0:
    print("+")
elif p < 0:
    print("-")
else:
    print(0)
