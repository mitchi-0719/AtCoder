s = input()

if s[0].isupper():
    for si in s[1:]:
        if si.isupper():
            print("No")
            exit()
    print("Yes")
else:
    print("No")
