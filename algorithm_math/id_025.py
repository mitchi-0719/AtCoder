n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

expected = 0

for i in range(n):
    expected += a[i]/3 + b[i]/3*2

print(expected)