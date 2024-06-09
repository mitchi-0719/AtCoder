n = int(input())
a = list(map(int, input().split()))
n = [i + 1 for i in range(n)]

ans = []
for i in range(n - 1):
    for j in range(i, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            ans.append([i + 1, j + 1])

print(len(ans))
for _ans in ans:
    print(*_ans)
