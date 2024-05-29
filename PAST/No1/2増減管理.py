n = int(input())
A = [int(input()) for _ in range(n)]

str_li = ["up", "stay", "down"]

for i in range(1, n):
    num = A[i] - A[i - 1]
    if num > 0:
        print(str_li[0], str(num))
    elif num == 0:
        print(str_li[1])
    else:
        print(str_li[2], str(abs(num)))