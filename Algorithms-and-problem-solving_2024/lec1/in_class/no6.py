while True:
    M, T, P, R = map(int, input().split())
    if M == T == P == R == 0:
        break

    idx = [i + 1 for i in range(T)]
    ac_cnt = [0 for i in range(T)]
    total_time = [0 for i in range(T)]
    wa_cnt = [[0 for i in range(P)] for j in range(T)]

    for i in range(R):
        m, t, p, j = map(int, input().split())
        if j == 0:
            ac_cnt[t - 1] += 1
            total_time[t - 1] += m + wa_cnt[t - 1][p - 1] * 20
        else:
            wa_cnt[t - 1][p - 1] += 1

    ac_cnt, total_time, idx = zip(
        *sorted(
            zip(ac_cnt, total_time, idx),
            reverse=True,
            key=lambda x: (x[0], -x[1], x[2]),
        )
    )

    for i, item in enumerate(idx):
        if i != 0:
            if ac_cnt[i - 1] == ac_cnt[i] and total_time[i - 1] == total_time[i]:
                print("=", end="")
            else:
                print(",", end="")

        print(item, end="")
    print()
