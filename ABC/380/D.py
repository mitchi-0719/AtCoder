s = input()
_q = int(input())
k = list(map(int, input().split()))
n = len(s)


def flip(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()


ans = []
for q in k:
    q -= 1
    c = s[q % n]
    t = q // n + 1

    cnt = 0
    while t > 0:
        p = (t - 1) // 2
        if p * 2 + 2 == t:
            cnt += 1

        t = p
    ans.append(c if cnt % 2 == 0 else flip(c))

print(" ".join(ans))
