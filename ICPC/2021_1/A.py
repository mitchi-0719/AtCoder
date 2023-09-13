a = list(map(int, input().split()))
ans = []

while set(a) != {0}:
    cnt = 0
    for i in range(4):
        if a[i] > 0:
            cnt += 1
    while cnt != 1:
        m = a[0]
        idx = 0
        for i in range(1, 4):
            if a[i] > 0 and (m > a[i] or m <= 0):
                m = a[i]
                idx = i
        for i in range(4):
            if idx != i:
                a[i] -= m
        cnt = 0
        for i in range(4):
            if a[i] > 0:
                cnt += 1
    ans.append(max(a))
    a = list(map(int, input().split()))

for i in range(len(ans)):
    print(ans[i])