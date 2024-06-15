from collections import defaultdict

d = {"a": 0, "b": 1, "c": 2, "d": 3}


def calc_hash(s, p):
    if s in "abcd":
        return int(p[d[s]])

    s = s[1:-1]
    op = s[0]
    x = None
    nex = 2

    if s[1] == "[":
        e = 2
        cnt = 0
        while cnt != 1:
            if s[e] == "[":
                cnt -= 1
            elif s[e] == "]":
                cnt += 1
            e += 1
        x = int(calc_hash(s[1:e], p))
        nex = e
    else:
        x = int(p[d[s[1]]])

    y = None
    if s[nex] == "[":
        e = nex + 1
        cnt = 0
        while cnt != 1:
            if s[e] == "[":
                cnt -= 1
            elif s[e] == "]":
                cnt += 1
            e += 1
        y = int(calc_hash(s[nex:e], p))
        nex = e + 1
    else:
        y = int(p[d[s[nex]]])

    if op == "+":
        return x | y
    if op == "*":
        return x & y
    if op == "^":
        return x ^ y


def solve(s):
    p = input()
    p_hash = None
    dic = defaultdict(int)

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    _p = f"{i}{j}{k}{l}"
                    h = calc_hash(s, _p)
                    if _p == p:
                        p_hash = h
                    dic[h] += 1

    print(p_hash, dic[p_hash])


while True:
    s = input()
    if s == ".":
        exit()

    solve(s)
