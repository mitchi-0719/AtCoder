start = False
find = False
a, b, c, d = 0, 0, 0, 0

for i in range(10):
    s = input()
    j = 0
    while j < 10 and not(find):
        if not(start) and s[j] == "#":
            a = i+1
            c = j+1
            start = True
        if start and s[j] == ".":
            d = j
            find = True
            break
        j += 1
    if find and "#" not in s:
        b = i

print(a, b)
print(c, d)