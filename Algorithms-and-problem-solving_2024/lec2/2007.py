def calc(r):
    a = r // 500
    r -= r // 500
    b = r // 100
    r -= r // 100
    c = r // 50
    r -= r // 50
    d = r // 10
    r -= r // 10
    return [a, b, c, d]


def solve(p):
    a, b, c, d = map(int, input().split())
    cnt = [a, b, c, d]
    ans = [a, b, c, d]

    now = 0
    for i in range(a + 1):
        now = i * 10
        if now >= p:
            tmp = calc(now - p)
            if sum(ans) > sum(cnt) - i + sum(tmp):
                ans = [ci + t for ci, t in zip(cnt, tmp)]
                ans[0] -= i
        for j in range(b + 1):
            now = i * 10 + j * 50
            if now >= p:
                tmp = calc(now - p)
                if sum(ans) > sum(cnt) - i - j + sum(tmp):
                    ans = [ci + t for ci, t in zip(cnt, tmp)]
                    ans[0] -= i
                    ans[1] -= j
            for k in range(c + 1):
                now = i * 10 + j * 50 + k * 100
                if now >= p:
                    tmp = calc(now - p)
                    if sum(ans) > sum(cnt) - i - j - k + sum(tmp):
                        ans = [ci + t for ci, t in zip(cnt, tmp)]
                        ans[0] -= i
                        ans[1] -= j
                        ans[2] -= k
                for l in range(d + 1):
                    now = i * 10 + j * 50 + k * 100 + l * 500
                    if now >= p:
                        tmp = calc(now - p)
                        if sum(ans) > sum(cnt) - i - j - k - l + sum(tmp):
                            ans = [ci + t for ci, t in zip(cnt, tmp)]
                            ans[0] -= i
                            ans[1] -= j
                            ans[2] -= k
                            ans[3] -= l
    print(ans)
    ans[0] > 0 and print(10, ans[0])
    ans[1] > 0 and print(50, ans[1])
    ans[2] > 0 and print(100, ans[2])
    ans[3] > 0 and print(500, ans[3])
    print()


while True:
    p = int(input())
    if p == 0:
        exit()
    solve(p)
