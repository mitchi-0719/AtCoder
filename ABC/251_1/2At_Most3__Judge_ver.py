#不正解

n, w = map(int, input().split())
A = list(map(int, input().split()))

li = []

if n == 1:
    print(1)
    exit()
elif n == 2:
    for i in range(2):
        if not(A[i] in li) and  A[i] <= w:
            li.append(A[i])
    total = A[0] + A[1]
    if not(total in li) and total <= w:
        li.append(total)
else:
    for i in range(n - 2):
        total = 0
        for j in range(3):
            total += A[i + j]
            print(total)
            if not(total in li) and total <= w:
                li.append(total)

print(li)
print(len(li))