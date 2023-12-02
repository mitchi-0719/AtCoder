n, q = map(int, input().split())
p = []

for i in range(n):
    P = input()
    p.append(P)


def g(h, w):
    ans = 0
    for i in range(h):
        for j in range(w):
            ans += 1 if p[i % n][j % n] == "B" else 0
    print(ans)
    return ans


def f(query):
    a, b, c, d = query
    return g(c, d) - g(c, b) - g(a, d) + g(a, b)


for i in range(q):
    print(f(map(int, input().split())))
