n, k = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))
x = [xi - 1 for xi in x]
visit = [False] * n
ans = [-1] * n

if k == 0:
    print(*a)
    exit()

for i, xi in enumerate(x):
    if visit[i]:
        continue
    arr = [i, xi]
    tmp = xi
    while True:
        if xi == x[tmp]:
            break
        arr.append(x[tmp])
        tmp = x[tmp]

    print(i, arr)
    arr_n = len(arr)
    for j in range(arr_n):
        visit[arr[j]] = True
        print((k % arr_n) - 1 + j)
        print(arr[(k % arr_n) - 1 + j])
        ans[arr[j]] = a[arr[(k % arr_n) - 1 + j]]

print(ans)
