a, b = map(int, input().split())

def swap(i, j):
    if i < j:
        return j, i
    else:
        return i, j

def rep(A, B, cnt):
    if B == 0:
        print(cnt-1)
    else:
        cnt += A//B
        A, B = swap(A%B, B)
        rep(A, B, cnt)

a, b = swap(a, b)
rep(a, b, 0)