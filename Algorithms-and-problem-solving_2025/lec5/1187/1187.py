def solve():
    M, T, P, R = map(int, input().split())
    if M == T == P == R == 0:
        return 1

    mtpj = [list(map(int, input().split())) for _ in range(R)]

    team = [[0, 0, [0 for _ in range(P)]] for _ in range(T)]

    for m, t, p, j in mtpj:
        _team = team[t - 1]
        if j == 0:
            _team[0] += 1
            _team[1] -= m + _team[2][p - 1]
        else:
            _team[2][p - 1] += 20

    team, idx = zip(
        *sorted(
            zip([_team[:2] for _team in team], [i + 1 for i in range(T)]), reverse=True
        )
    )

    ans = str(idx[0])
    bef = team[0]

    for t, i in zip(team[1:], idx[1:]):
        if t == bef:
            ans += "="
        else:
            ans += ","
        ans += str(i)
        bef = t

    print(ans)


while not solve():
    ...
