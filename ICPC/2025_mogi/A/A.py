def solve():
    N = int(input())
    if N == 0:
        return 1

    a = list(map(int, input().split()))
    before = 0
    for i in range(N):
        if before + 1 != a[i]:
            print(before + 1)
            return
        before = a[i]

    print(a[-1] + 1)


while 1:
    if solve():
        break
