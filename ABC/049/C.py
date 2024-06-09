s_list = ["dream", "dreamer", "erase", "eraser"]
s = input()

while True:
    change = False
    for _s in s_list:
        l = len(_s)
        if _s == s[-l:]:
            s = s[:-l]
            change = True
            break

    if not change:
        print("NO")
        exit()
    if len(s) == 0:
        print("YES")
        exit()
