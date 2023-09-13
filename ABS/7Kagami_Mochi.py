n = int(input())
d = [int(input()) for _ in range(n)]
comp = 0
count = 1

for i in range(n):
    comp = i
    for j in range(i + 1, n):
        if d[comp] < d[j]:
            comp = j
    if comp != i:
        escape = d[comp]
        d[comp] = d[i]
        d[i] = escape

for i in range(n - 1):
    if d[i] != d[i + 1]:
        count += 1

print(count)