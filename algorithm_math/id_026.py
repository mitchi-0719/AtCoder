n = int(input())

expected = 0

for i in range(n):
    expected += n/(i+1)

print(expected)