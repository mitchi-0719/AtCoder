a, b = map(int, input().split())
print([i for i in range(10) if i != a + b][0])
