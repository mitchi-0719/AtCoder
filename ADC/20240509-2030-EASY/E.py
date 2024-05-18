n = int(input())
s = []

for i in range(n):
    si = input()
    if si[0] < si[-1]:
        si = si[::-1]
    s.append(si)

print(len(set(s)))
