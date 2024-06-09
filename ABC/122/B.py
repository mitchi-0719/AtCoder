s = input()
acgt = set(["A", "C", "G", "T"])

ans = 0
l = len(s)
for i in range(0, l):
    for j in range(l - i):
        part_s = list(s[i : l - j])
        if len(set(part_s) - acgt) == 0:
            ans = max(ans, len(part_s))

print(ans)
