k = int(input())
a = [0]
a.append(7 % k)

for i in range(2, k + 1):
    a.append((a[i - 1] * 10 + 7) % k)

for i in range(1, k + 1):
    if a[i] == 0:
        print(i)
        print(a)
        exit()

print(-1)
