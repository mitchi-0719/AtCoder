# AC

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = max(a)

for i in range(n):
    if m == a[i] and i + 1 in b:
        print("Yes")
        exit()

print("No")
