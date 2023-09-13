#正解

n = int(input())
A = list(map(int, input().split()))

A = sorted(A)
count = 1
hold = A[0]

for i in range(1, 4 * n - 1):
    if hold == A[i]:
        count += 1
    else:
        if count != 4:
            print(hold)
            exit()
        count = 1
        hold = A[i]
print(A[-1])