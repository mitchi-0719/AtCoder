n, m = map(int, input().split())
c = list(map(str, input().split()))
d = list(map(str, input().split()))
p = list(map(int, input().split()))

sum = 0
for i in range(n):
    if c[i] in d:
        sum += p[d.index(c[i])+1]
    else:
        sum += p[0]

print(sum)