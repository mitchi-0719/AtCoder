n = int(input())
a = list(map(int, input().split()))

b = []

for i in range(n):
    t = a[i]
    while len(b) != 0 and b[-1] == t:
        p = b.pop()
        t += 1
    b.append(t)


print(len(b))
