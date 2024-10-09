s = input()
t = input()

l = min(len(s), len(t))

for i in range(l):
    if s[i] == t[i]:
        continue
    print(i+1)
    exit()

if not(len(s) == len(t) == l):
    print(l+1)
    exit()

print(0)

