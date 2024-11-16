s = input()

cnt = 0
for i in range(1, len(s)):
    if s[i] == "|":
        print(cnt, end=" ")
        cnt = 0
    else:
        cnt += 1
