from itertools import accumulate

while 1:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_acc = accumulate(a)
    b_acc = accumulate(b)
    diff = [ai - bi for ai, bi in zip(a_acc, b_acc) if ai != bi]

    ans = 0
    for i in range(len(diff) - 1):
        if diff[i] * diff[i + 1] < 0:
            ans += 1

    print(ans)
