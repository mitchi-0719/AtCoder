from collections import defaultdict

n = int(input())
s = defaultdict(int)

for i in range(n):
    si = input()
    if si < si[::-1]:
        s[si] += 1
    else:
        s[si[::-1]] += 1

print(len(s.keys()))
