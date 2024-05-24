n, m = map(int, input().split())
p, c, f = [], [], []

for i in range(n):
    li = list(map(int, input().split()))
    p.append(li[0])
    c.append(li[1])
    f.append(li[2:])

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if set(f[i]) <= (set(f[j])):

            if p[i] > p[j] or (p[i] == p[j] and len(set(f[j]) - (set(f[i]))) >= 1):
                print("Yes")
                exit()

print("No")
