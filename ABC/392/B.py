n, m = map(int, input().split())
a = set(map(int, input().split()))
x = []

for i in range(n):
    if i + 1 not in a:
        x.append(i + 1)

print(len(x))
print(*x)
