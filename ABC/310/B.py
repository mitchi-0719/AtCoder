n, m = map(int, input().split())

item = []

for i in range(n):
    ITEM = list(map(int, input().split()))
    item.append(ITEM)

for i in range(n):
    p = item[i][0]
    f = item[i][2:]
    for j in range(n):
        if i == j: continue
        if p >= item[j][0] and set(set(f)).issubset(item[j][2:]) and (p > item[j][0] or set(item[j][2:]) != (set(f))):
            print("Yes")
            exit()

print("No")