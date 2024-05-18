"""
import bisect

n = int(input())
a, c = [], []
ai, ci = [], []

del_card = set([])

for i in range(n):
    _a, _c = map(int, input().split())
    if len(a) == 0:
        a.append(_a)
        c.append(_c)
        ai.append(i + 1)
        ci.append(i + 1)
    else:
        a_idx = bisect.bisect_left(a, _a)
        c_idx = bisect.bisect_right(c, _c)
        part_a = set(ai[:a_idx])
        part_c = set(ci[c_idx:])

        not_part_a = set(ai[a_idx:])
        not_part_c = set(ci[:c_idx])

        not_part = not_part_a & not_part_c
        if len(not_part) != 0:
            del_card.add(i)

        del_card = (part_a & part_c) - del_card

        a.append(_a)
        ai.append(i + 1)
        a, ai = zip(*sorted(zip(a, ai)))
        a = list(a)
        ai = list(ai)

        c.append(_c)
        ci.append(i + 1)
        c, ci = zip(*sorted(zip(c, ci)))
        c = list(c)
        ci = list(ci)


ans = set(ai) - del_card
print(len(ans))
for i in sorted(list(ans)):
    print(i, end=" ")

"""

# answer
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())) + [i + 1])
p = sorted(p)

ans = []
min_cost = 10 * 18
print(p)
for a, c, i in p[::-1]:
    if c < min_cost:
        min_cost = c
        ans.append(i)

print(len(ans))
print(*sorted(ans))
