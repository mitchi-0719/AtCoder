n = int(input())

isLogin = False
ans = 0

for _ in range(n):
    s = input()
    if s == "login":
        isLogin = True
    elif s == "logout":
        isLogin = False
    elif s == "public":
        pass
    else:
        if not isLogin:
            ans += 1

print(ans)
