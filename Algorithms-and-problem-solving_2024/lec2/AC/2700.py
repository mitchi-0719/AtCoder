def encode(s):
    vowels = "aiueo"
    res = ""
    for i, _s in enumerate(s):
        if i == 0:
            res += _s
        else:
            if s[i - 1] in vowels:
                res += _s
    return res


def solve(n):
    s = [encode(input()) for _ in range(n)]
    m = max([len(_s) for _s in s])

    for k in range(1, m + 1):
        codes = set()
        for _s in s:
            codes.add(_s[:k])
        if len(codes) == len(s):
            print(k)
            return
    print(-1)


while True:
    n = int(input())
    if n == 0:
        exit()
    solve(n)
