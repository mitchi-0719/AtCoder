from collections import defaultdict

s = input()


d = defaultdict(int)
for si in s:
    d[si] += 1

d2 = defaultdict(int)
for v in d.values():
    d2[v] += 1

for v in d2.values():
    if v != 0 and v != 2:
        print("No")
        exit()

print("Yes")
