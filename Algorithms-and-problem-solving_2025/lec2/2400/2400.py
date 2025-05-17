from collections import defaultdict


def solve():
    t, p, r = map(int, input().split())
    if t == p == r == 0:
        return True
    team = [
        {"t_id": i, "ac": 0, "penalty": 0, "rank": 0, "wa": defaultdict(int)}
        for i in range(t)
    ]

    for _ in range(r):
        t_id, p_id, tm, ms = input().split()
        t_id, p_id, tm = map(int, [t_id, p_id, tm])
        t_id -= 1

        if ms == "WRONG":
            team[t_id]["wa"][p_id] += 1
        else:
            team[t_id]["ac"] += 1
            team[t_id]["penalty"] += team[t_id]["wa"][p_id] * 1200 + tm

    s_team = sorted(team, key=lambda x: (-x["ac"], x["penalty"], x["t_id"]))
    for st in s_team:
        t_id = st["t_id"]
        ac = st["ac"]
        penalty = st["penalty"]
        print(t_id + 1, ac, penalty)


while 1:
    if solve():
        break
