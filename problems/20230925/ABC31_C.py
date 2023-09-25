N, M = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

low = 10 ** 10

for i in range(N):
    h = len(b)-1
    l = 0
    m = (h + l)//2

    while 0 <= m < M and l <= h:
        if b[m] < a[i]:
            l = m+1
        elif b[m] > a[i]:
            h = m-1
        else:
            break
        m = (h + l)//2
    if i >= M - m:
        low = min(low, a[i])

for i in range(M):
    h = len(b)-1
    l = 0
    m = (h + l)//2

    while 0 <= m < N and l <= h:
        if a[m] < b[i]+1:
            l = m+1
        elif a[m] > b[i]+1:
            h = m-1
        else:
            break
        m = (h + l)//2
    if M - i <= m:
        low = min(low, b[i]+1)

print(low)