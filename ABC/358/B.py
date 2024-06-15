n, a = map(int, input().split())
t = list(map(int, input().split())) + [float("inf")]

for i in range(n):
    print(t[i] + a)
    if t[i] + a > t[i + 1]:
        t[i + 1] = t[i] + a
