n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = a + b
c_judge = [True if i <= n else False for i in range(1, n+m+1)]

c, c_judge = zip(*sorted(zip(c, c_judge)))

for i in range(n+m):
    if c_judge[i]:
        print(i+1, end=" ")

print()

for i in range(n+m):
    if not c_judge[i]:
        print(i+1, end=" ")

