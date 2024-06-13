n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    print(*[j + 1 for j in range(n) if a[j] == 1])
