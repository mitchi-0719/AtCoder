n = int(input())
a = list(map(int, input().split()))
li = [i + 1 for i in range(n)]

ans = []
while a != li:
    for i in range(n):
        j = a[i] - 1
        if i != j:
            ans.append(sorted([i + 1, j + 1]))
            a[i], a[j] = a[j], a[i]

print(len(ans))
for _ans in ans:
    print(*_ans)
