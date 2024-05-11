# AC

n, k = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
emp = 0

for i in a:
    if emp - i <= 0:
        cnt += 1
        if emp - i == 0:
            emp = k
        else:
            emp = k - i
    else:
        emp -= i

print(cnt)
