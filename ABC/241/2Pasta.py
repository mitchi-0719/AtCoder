#正解

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(m):
    search = B[i]

    if search in A:
        find = A.index(search)
        A[find] = -100
    else:
        print("No")
        exit()
print("Yes")