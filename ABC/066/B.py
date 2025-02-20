s = input()
n = len(s)

for i in range(n):
    s = s[:-1]
    if len(s) % 2 == 1:
        continue

    m = len(s) // 2
    if s[:m] == s[m:]:
        print(len(s))
        exit()

print(1)
