n, q = map(int, input().split())
a = list(map(int, input().split()))

x = [int(input()) for _ in range(q)]
num = [i for i in range(q)]

ans = [0 for i in range(q)]

a = sorted(a, reverse=True)
x, num = zip(*sorted(zip(x, num), reverse=True))

j = 0
for i in range(len(x)):
    while j < len(a) and a[j] >= x[i]:
        j += 1
    ans[num[i]] = j

for i in ans:
    print(i)