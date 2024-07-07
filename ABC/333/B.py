def dist(arr1, arr2, c1, c2):
    d1 = 0
    i1 = arr1.index(c1)

    i = i1
    while True:
        if arr1[i % 5] == c2:
            d1 = i - i1
            break
        i += 1

    d2 = 0
    i2 = arr2.index(c1)

    i = i2
    while True:
        if arr2[i % 5] == c2:
            d2 = i - i2
            break
        i += 1
    return min(d1, d2)


s = list(input())
t = list(input())
c = ["A", "B", "C", "D", "E"]
c_rev = c[::-1]

print("Yes" if dist(c, c_rev, s[0], s[1]) == dist(c, c_rev, t[0], t[1]) else "No")
