def solve():
    n = int(input())
    if n == 0:
        return 1

    v = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n - 1):
        if v[i - 1] < v[i] > v[i + 1]:
            cnt += 1

    print(cnt)


while 1:
    if solve():
        break
