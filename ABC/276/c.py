n = int(input())
p = list(map(int, input().split()))

def judge(li):
    if li == sorted(li):
        return 1
    elif li == sorted(li, reverse=True):
        return -1
    else:
        return 0

for i in range(1, n):
    j = judge(p[i:])
    if j == 1:
        for k in range(i):
            print(p[:i-1])
        print(p[i]-1, end=" ")
        a = sorted(p[i:], reverse=True)
        for k in range(len(p)-i):
            print(a[k], end=" ")
        exit()
    elif j == -1:
        for k in range(i):
            print(p[:len(p)-2], end=" ")
        print(p[-1], p[-2])
        exit()