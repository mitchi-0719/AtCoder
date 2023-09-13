m = int(input())
d = list(map(int, input().split()))

mid = (sum(d)+1)//2
s = 0

for i in range(m):
    if s+d[i] >= mid:
        print(i+1, mid-s)
        exit()
    s += d[i]

print(m, mid)