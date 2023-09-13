#正解

s = input()

p = sorted(list(s))
chk1 = False
chk2 = False

if s.upper() != s and s.lower() != s:
    chk1 = True

i = 0
while i < len(p) - 1 and p[i] != p[i + 1]:
    i += 1

if i == len(p) - 1:
    chk2 = True

if chk1 and chk2:
    print("Yes")
else:
    print("No")