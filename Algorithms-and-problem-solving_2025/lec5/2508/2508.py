alf = [chr(ord("a") + i) for i in range(26)] + [chr(ord("A") + i) for i in range(26)]

d = {}
for i, a in enumerate(alf):
    d[a] = i + 52

alf = alf + alf


def solve():
    n = int(input())
    if n == 0:
        return 1

    k = list(map(int, input().split()))
    s = input()

    ans = []
    for i, si in enumerate(s):
        key = k[i % n]
        s_idx = d[si]
        ans.append(alf[s_idx - key])

    print("".join(ans))


while not solve():
    ...
