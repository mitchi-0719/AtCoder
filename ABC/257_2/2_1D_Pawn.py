n, k, q = map(int, input().split())

a = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(q):
    if a[l[i]-1] != n and  a[l[i]%k] != a[l[i]-1] + 1:
        a[l[i]-1] += 1

print(*a)