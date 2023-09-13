n = int(input())

s = set()

for i in range(n):
    S = input()
    if not (set([S]).issubset(s) or set([S[::-1]]).issubset(s)):
        s.add(S)

print(len(s))