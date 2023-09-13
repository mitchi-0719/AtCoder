#正解

A = list((map(int, input().split())))

A = sorted(A)
buffer = A[0]
count = 1
for i in range(1, 5):
    if buffer != A[i]:
        count += 1
    buffer = A[i]

print(count)