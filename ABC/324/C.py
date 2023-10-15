# AC

n, t_ = input().split()
n = int(n)
s = []
ans = []
t_len = len(t_)


for i in range(n):
    s.append(input())

for i in range(n):
    # 等しい
    if s[i] == t_:
        ans.append(i + 1)

    # 挿入
    elif len(s[i]) + 1 == t_len:
        find = -1
        for j in range(len(s[i])):
            if s[i][j] == t_[j]:
                continue
            else:
                find = j
                break
        if s[i][find:] == t_[find + 1 :] or find == -1:
            ans.append(i + 1)

    # 削除
    elif len(s[i]) - 1 == t_len:
        find = -1
        for j in range(t_len):
            if s[i][j] == t_[j]:
                continue
            else:
                find = j
                break
        if s[i][find + 1 :] == t_[find:] or find == -1:
            ans.append(i + 1)

    # 変更
    elif len(s[i]) == t_len:
        find = -1
        for j in range(t_len):
            if s[i][j] == t_[j]:
                continue
            else:
                find = j + 1
                break
        if s[i][find:] == t_[find:] or find == -1:
            ans.append(i + 1)

print(len(ans))
print(*ans)
