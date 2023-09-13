n = int(input())

while n != 0:
    a = list(map(int, input().split()))
    diff = abs(2023 - a[0])
    diff_idx = 0
    for i in range(1, len(a)):
        if diff > abs(2023 - a[i]):
            diff_idx = i
            diff = abs(2023 - a[i])
    print(diff_idx+1)
    n = int(input())
