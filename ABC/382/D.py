def plus(arr, i):
    for j in range(i, len(arr)):
        arr[j] += 1

    return arr


def solve(arr, i):
    while True:
        if arr[-1] > m:
            return

        if i + 1 == n:
            ans.append(arr[:])
        else:
            solve(arr[:], i + 1)

        arr = plus(arr[:], i)


n, m = map(int, input().split())
arr = [1 + 10 * i for i in range(n)]
ans = []
solve(arr[:], 0)

print(len(ans))
for _ans in ans:
    print(*_ans)
