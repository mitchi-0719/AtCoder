M, D = map(int, input().split())
y, m, d = map(int, input().split())

if D == d:
    d = 1
    if M == m:
        m = 1
        y += 1
    else:
        m += 1
else:
    d += 1

print(y, m, d)