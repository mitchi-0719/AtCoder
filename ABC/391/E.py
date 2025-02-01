n = int(input())
a = list(input())
ans = []


def check(i1, i2, i3):
    if i1 == i2 or i1 == i3:
        return i1
    return i2


i = 1
ans.append([*a])
while len(ans[i - 1]) != 1:
    ans.append([])
    for j in range(len(ans[i - 1]) // 3):
        ans[i].append(check(a[i - 1][i * 3], a[i - 1][i * 3 + 1], a[i - 1][i * 3 + 2]))
    i += 1

print(ans)
