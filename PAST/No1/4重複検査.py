#正解

n = int(input())
A = [int(input()) for _ in range(n)]

A_sort = sorted(A)
nums = [i for i in range(1, n+1)]

if nums == A_sort:
    print("Correct")
else:
    is_buffer1 = True
    is_buffer2 = True
    idx = 0
    if A_sort[0] != 1:
        buffer2 = 1
        is_buffer2 = False
    if A_sort[-1] != n:
        buffer2 = n
        is_buffer2 = False
    while idx < n and (is_buffer1 or is_buffer2):
        if A_sort[idx] == A_sort[(idx+1)%n]:
            buffer1 = A_sort[idx]
            is_buffer1 = False
        if is_buffer2 and abs(A_sort[idx] - A_sort[(idx+1%2)]) == 2:
            buffer2 = (A_sort[idx] + A_sort[idx+1]) // 2
            is_buffer2 = False
        idx += 1
    print(buffer1, buffer2)