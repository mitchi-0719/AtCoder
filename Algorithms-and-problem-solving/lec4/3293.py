def calc(s, k, removes):
    ans = 0
    _k = k
    tmp = 0
    for i in range(len(s)):
        if i not in removes:
            tmp += 10 ** (_k - 1) * int(s[i])
            _k -= 1
        if _k == 0:
            ans += tmp
            _k = k
            tmp = 0

    return ans


def solve(k):
    s = input()
    calc(s, k, [])


while True:
    k = int(input())
    if k == 0:
        exit()
    solve(k)
