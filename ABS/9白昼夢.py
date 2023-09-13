s = input()
change = False

while True:
    change = False
    if s[:10] == "dreamerase":
        s = s[5:]
        change = True

    elif s[:9] == "eraserase":
        s = s[5:]
        change = True

    elif s[:6] == "eraser":
        s = s[6:]
        change = True

    elif s[:5] == "erase":
        s = s[5:]
        change = True

    elif s[:7] == "dreamer":
        s = s[7:]
        change = True

    elif s[:5] == "dream":
        s = s[5:]
        change = True

    if s == "":
        print("YES")
        break
    elif change == False:
        print("NO")
        break