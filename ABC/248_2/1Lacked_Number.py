#正解

s = input()
ans = 0
for j in range(10):
    check = False
    for i in s:
        if i == str(j):
            check = True
            break
    if not(check):
        ans = j
        break
print(ans)