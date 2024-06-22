def print_s(n, s, i):
    if i + 1 == n:
        pass


def solve(n, s):
    for i in range(n):
        l = s[i].count(".")
        if l == 0:
            print(s[i])
        elif l == 1:
            print(f"+{s[i]}")
        else:
            print_s(n, s, i)


while True:
    n = int(input())
    if n == 0:
        exit()
    s = [input() for _ in range(n)]

    solve(n, s)
