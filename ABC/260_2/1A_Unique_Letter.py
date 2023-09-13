#正解

s = input()
cnt = [0] * 3
check = True

for i in range(3):
    for j in range(3):
        if s[i] == s[j]:
            cnt[i] += 1

for i in range(3):
    if cnt[i] == 1:
        print(s[i])
        check = False
        break

if check:
    print(-1)