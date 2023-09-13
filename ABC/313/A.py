n = int(input())
p = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

m = max(p[1:])
if m < p[0]:
    print(0)
else:
    print(m - p[0] + 1)