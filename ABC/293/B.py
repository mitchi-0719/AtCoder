n = int(input())
a = list(map(int, input().split()))
b = [True for i in range(n)]

for i in range(n):
    if b[i]:
        b[a[i]-1] = False

print(b.count(True))
for i in range(n):
    if b[i]:
        print(i+1, end=" ")
