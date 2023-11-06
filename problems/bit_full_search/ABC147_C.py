n = int(input())
a = []
evidence = []

for i in range(n):
    a.append(int(input()))
    buffer = []
    for j in range(a[i]):
        buffer.append(list(map(int, input().split())))
    evidence.append(buffer)

for bit in range(1 << n):
    person = [1 for i in range(n)]
    for i in range(n):
        if bit & (1 << i):
            for j in range(a[i]):
                evidence[i]