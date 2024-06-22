n = int(input()) * 2
a = list(map(int, input().split()))

cnt = 0
for i in range(n - 2):
    if a[i] == a[i + 2]:
        cnt += 1

print(cnt)
