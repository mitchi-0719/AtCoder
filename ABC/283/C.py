s = input()

i = 0
ans = 0
while True:
    if i >= len(s):
        break
    if s[i] == "0" and i + 1 < len(s) and s[i + 1] == "0":
        i += 1
    ans += 1
    i += 1

print(ans)
