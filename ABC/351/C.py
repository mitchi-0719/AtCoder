n = int(input())
a = list(map(int, input().split()))

b = []

for i in range(n):
    b.append(a[i])
    while True:
        if len(b) != 1 and b[-1] == b[-2]:
            b[-2] += 1
            b.pop(-1)
        else:
            break


print(len(b))
