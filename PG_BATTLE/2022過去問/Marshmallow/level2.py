n = int(input())
a = list(input().split())

buffer = -1
a_sum = 0
for i in range(n * 2 + 1):
    if i % 2 == 0:
        a_sum += int(a[i])
    else:
        if a[i] == "=":
            if buffer != -1 and buffer != a_sum:
                print("No")
                exit()
            buffer = a_sum
            a_sum = 0

if buffer == a_sum:
    print("Yes")
else :
    print("No")