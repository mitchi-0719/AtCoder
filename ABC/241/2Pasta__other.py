#正解

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

idx = 0
cnt = 0
check = True

while idx < m and check:
    A = sorted(A)
    search = B[idx]
    top = n - 1
    bottom = cnt
    mid = (top + bottom) // 2

    while top > bottom and search != A[mid]:
        if search < A[mid]:
            top = mid - 1
        else:
            bottom = mid + 1
        mid = (top + bottom) // 2

    if search != A[mid]:
        check = False
    else:
        A[mid] = -100
        cnt += 1
    idx += 1


if check:
    print("Yes")
else:
    print("No")