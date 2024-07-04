n, m = map(int, input().split())
a = list(map(int, input().split()))

c = [0] * (n + 1)
i = a[0]
c[i] += 1
for ai in a[1:]:
    print(i)
    c[ai] += 1
    if c[i] < c[ai]:
        i = ai
    elif c[i] == c[ai] and ai < i:
        i = ai

print(i)
