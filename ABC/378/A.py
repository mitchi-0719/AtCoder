a = list(map(int, input().split()))
ans = 0

for i in range(3):
    for j in range(i + 1, 4):
        if a[i] == a[j] and a[i] != -1:
            a[i] = -1
            a[j] = -1
            ans += 1

print(ans)
