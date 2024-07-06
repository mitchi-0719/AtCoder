from collections import defaultdict

d = defaultdict(int)
s = input()

for si in s:
    d[si] += 1


print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])
