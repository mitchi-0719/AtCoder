n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    s, t = map(int, input().split())
    if a[i] >= s:
        a[i + 1] += t * (a[i] // s)

print(a[-1])
