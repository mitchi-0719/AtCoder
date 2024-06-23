s = list(input())
t = input()

c = list(t)
b = [False for _ in range(3)]
if t[-1] == "X":
    c.pop()
    b.pop()

ci = 0
for i in range(len(s)):
    if s[i] != None and s[i].upper() == c[ci]:
        s[i] = None
        b[ci] = True
        ci += 1
        if ci == len(c):
            print("Yes")
            exit()

print("No")
