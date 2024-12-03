def toInt(c):
    return ord(c) - (ord("a") - 1)


def base_10(num_n, n):
    num_10 = 0
    for c in str(num_n):
        num_10 *= n
        num_10 += toInt(c)
    return num_10


print(base_10(input().lower(), 26))
