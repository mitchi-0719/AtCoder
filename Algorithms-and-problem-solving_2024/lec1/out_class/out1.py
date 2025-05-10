def solve(n, k, s):
    s_list = [chr(ord("a") + i) for i in range(26)] + [
        chr(ord("A") + i) for i in range(26)
    ]
    s_i_obj = {_s: i for i, _s in enumerate(s_list)}
    i_s_obj = {i: _s for i, _s in enumerate(s_list)}

    ans = ""
    for i, _s in enumerate(s):
        ans += i_s_obj[(s_i_obj[_s] - k[i % n]) % 52]

    print(ans)


while True:
    n = int(input())
    if n == 0:
        exit()

    k = list(map(int, input().split()))
    s = input()

    solve(n, k, s)
