l = 0
h = (10**9) // 2
mid = l + h

while True:
    mid = l + h
    print(mid)
    s = input()

    if s == "=":
        break
    elif s == "<":
        h = mid
    else:
        l = mid
