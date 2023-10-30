n, m = map(int, input().split())
rule = []

for i in range(m):
    a, b = map(int, input().split())
    rule.append(set([a, b]))

k = int(input())
choice = []

for i in range(k):
    c, d = map(int, input().split())
    choice.append([c, d])


def build_bit(bit):
    choice_bit = set()
    for i in range(k):
        if bit & (1 << i):
            choice_bit.add(choice[i][1])
        else:
            choice_bit.add(choice[i][0])
    return choice_bit


def calc(bit):
    choice_bit = build_bit(bit)
    cnt = 0
    for val in rule:
        cnt += 1 if val.issubset(choice_bit) else 0
    return cnt


max_cnt = 0
for bit in range(1 << k):
    max_cnt = max(max_cnt, calc(bit))

print(max_cnt)
