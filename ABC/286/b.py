# AC

n = int(input())
s = input()

i = 0
while i < n-1:
    if s[i] == "n" and s[i+1] == "a":
        s = s[:i+1] + "y" + s[i+1:]
        n += 1
    i += 1

print(s)