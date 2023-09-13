#正解

n = int(input())
A = list(map(int, input().split()))

A_sort = sorted(A)

i = 0
buffer = A_sort[0]
print_bool = True

if buffer != 0:
    print_bool = False
    print(0)
else:
    for j in range(1, n):
        if buffer == A_sort[j]:
            continue
        buffer = A_sort[j]
        i += 1
        if A_sort[j] != i:
            print_bool = False
            print(i)
            break

if print_bool:
    print(A_sort[n - 1] + 1)