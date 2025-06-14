coin = [10, 50, 100, 500]
flag = False


def solve():
    global flag
    m = int(input())
    if m == 0:
        return 1

    if flag:
        print()

    flag = True
    cnt = list(map(int, input().split()))

    ans = []
    ans_cnt = float("inf")

    for ten in range(cnt[0] + 1):
        for fifty in range(cnt[1] + 1):
            for hun in range(cnt[2] + 1):
                for five_hun in range(cnt[3] + 1):
                    c = [ten, fifty, hun, five_hun]
                    s = sum(c[i] * coin[i] for i in range(4))
                    if s < m:
                        continue

                    rest = s - m
                    rev = 0

                    for i in range(4):
                        if rest >= coin[~i]:
                            temp = rest // coin[~i]
                            rev += temp
                            rest -= coin[~i] * temp

                    if ans_cnt > rev:
                        ans_cnt = rev
                        ans = [ten, fifty, hun, five_hun]

    for c, k in zip(coin, ans):
        if k == 0:
            continue
        print(c, k)


while not solve():
    ...
