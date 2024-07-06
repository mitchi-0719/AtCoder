n, m = map(int, input().split())
s = list(input())
shirt = m
tmp = 0
add = 0

for si in s:
    if si == "0":
        shirt = m
        add = max(add, tmp)
        tmp = 0
    elif si == "2":
        tmp += 1
    else:
        if shirt != 0:
            shirt -= 1
        else:
            tmp += 1

print(max(tmp, add))
