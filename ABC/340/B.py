a = []
q = int(input())

for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        a.append(que[1])
    else:
        print(a[-que[1]])
