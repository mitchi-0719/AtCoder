n, m = map(int, input().split())
a = list(map(int, input().split()))

s = [0 for i in range(m)]

for i in range(n):
    x = list(map(int, input().split()))
    s = [s[j] + x[j] for j in range(m)]

for i in range(m):
    if s[i] < a[i]:
        print("No")
        exit()

print("Yes")
