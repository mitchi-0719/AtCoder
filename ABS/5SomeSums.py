n, a, b = list(map(int, input().split()))

sum = 0

for i in range(1, n + 1):
    k = str(i)
    check = 0
    for j in k:
        check += int(j)
    if check >= a and check <= b:
        sum += i

print(sum)