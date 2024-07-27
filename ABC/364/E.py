def solve_sum():
    s = [a[i] + b[i] for i in range(n)]

    _, idx = zip(*sorted(zip(s, [i for i in range(n)])))

    a_sum = 0
    b_sum = 0
    for i in range(n):
        j = idx[i]
        if a_sum + a[j] > x or b_sum + b[j] > y:
            return i + 1
        a_sum += a[j]
        b_sum += b[j]

    return n


def solve_rank():
    idx = [i for i in range(n)]
    _, a_idx = zip(*sorted(zip(a, [*idx])))
    _, b_idx = zip(*sorted(zip(b, [*idx])))

    _, a_rank = zip(*sorted(zip(a_idx, [*idx])))
    _, b_rank = zip(*sorted(zip(b_idx, [*idx])))

    s_rank = [a_rank[i] + b_rank[i] for i in range(n)]
    _, s_idx = zip(*sorted(zip(s_rank, [*idx])))

    a_sum = 0
    b_sum = 0
    for i in range(n):
        j = s_idx[i]
        if a_sum + a[j] > x or b_sum + b[j] > y:
            return i + 1
        a_sum += a[j]
        b_sum += b[j]

    return n


n, x, y = map(int, input().split())
a, b = [], []

for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)

print(max(solve_sum(), solve_rank()))
