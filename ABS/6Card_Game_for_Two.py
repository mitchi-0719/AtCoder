n = int(input())
a = list(map(int, input().split()))
escape = 0
alice = 0
bob = 0

for i in range(1, n):
    for j in range(n - i):
        if a[j] < a[j + 1]:
            escape = a[j]
            a[j] = a[j + 1]
            a[j + 1] = escape

for i in range(n):
    if i % 2 == 0:
        alice += a[i]
    else:
        bob += a[i]

print(alice - bob)