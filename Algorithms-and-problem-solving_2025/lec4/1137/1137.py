def encode(n):
    ans = ""
    for i, s in enumerate("ixcm"):
        ni = n // (10**i) % 10
        if ni != 0:
            ans = (str(ni) if ni != 1 else "") + s + ans

    return ans


def decode(s):
    ans = 0
    n = 1

    d = {"m": 1000, "c": 100, "x": 10, "i": 1}

    for si in s:
        if si in "mcxi":
            ans += n * d[si]
            n = 1
        else:
            n = int(si)

    return ans


n = int(input())

for _ in range(n):
    s1, s2 = input().split()
    print(encode(decode(s1) + decode(s2)))
