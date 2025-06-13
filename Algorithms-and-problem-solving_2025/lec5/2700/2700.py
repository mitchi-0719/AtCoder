vowel = "aiueo"


def solve():
    n = int(input())
    if n == 0:
        return 1

    s = [input() for _ in range(n)]
    s_code = [[] for _ in range(n)]

    for i, si in enumerate(s):
        s_code[i].append(si[0])
        for j in range(1, len(si)):
            if si[j - 1] in vowel:
                s_code[i].append(si[j])

    max_l = max([len(si) for si in s_code])

    for k in range(1, max_l + 1):
        st = set()
        for i in range(n):
            ss = "".join(s_code[i][:k])
            if ss in st:
                break
            st.add(ss)
        else:
            if len(st) == n:
                print(k)
                return
    print(-1)


while not solve():
    ...
