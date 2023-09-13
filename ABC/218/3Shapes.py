n = int(input())

S = [input() for _ in range(n)]
T = [input() for _ in range(n)]
check_s = S

def rotation(li):
    global n
    buffer_li = []
    for i in range(n-1, -1, -1):
        buffer = ""
        for j in range(n):
            buffer += check_s[j][i]
        buffer_li.append(buffer)
    return buffer_li

def check(chk_li, ans_li):
    idx = 0
    while idx < n:
        cnt = 0
        for j, k in zip(chk_li, ans_li):
            if j == k:
                cnt += 1
            else:
                break
        if cnt == n:
            print("Yes")
            exit()
        else:
            chk_li.append(chk_li.pop(0))
        idx += 1

check(check_s, T)
for i in range(3):
    check_s = rotation(check_s)
    check(check_s, T)
print("No")