n = int(input())
s = input()

for i in range(n - 1):
    j = i + 1

    l = 0
    for k in range(n - j):
        if s[k] == s[k + j]:
            break
        l += 1

    print(l)
