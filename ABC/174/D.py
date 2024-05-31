n = int(input())
c = list(input())

ans = 0

l = 0
r = n - 1
while l < r:
    for i in range(n):
        if c[l] == "W":
            l += 1
        else:
            break

    for i in range(n):
        if c[-(r + 1)] == "R":
            r += 1
        else:
            break
    c[l] = "R"
    c[r] = "W"
    ans += 1
    print(l, r, c)

print(ans)
