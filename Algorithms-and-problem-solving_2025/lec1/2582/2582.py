def solve():
    n = int(input())
    if n == 0:
        return False

    f = input().split()
    ans = 0

    for i in range(0, n, 2):
        j = i + 1
        if j >= n:
            break
        f_set = {f[i], f[j]}
        if f_set == {"lu", "ru"} or f_set == {"ld", "rd"}:
            ans += 1

    print(ans)
    return True


while 1:
    if not solve():
        break
