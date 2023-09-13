n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

cnt = 0
a = sorted(a)
while True:
    if abs(a[0] - a[-1]) <= 1:
        print(cnt)
        exit()
    a[0] += 1
    a[-1] -= 1
    cnt += 1
    a = sorted(a)
    print(a)