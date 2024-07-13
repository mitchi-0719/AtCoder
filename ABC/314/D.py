n = int(input())
s = input()
q = int(input())

s = list(s)
ans = [None for _ in range(n)]
state = "org"
org_idx = set()

for _ in range(q):
    t, x, c = input().split()
    if int(t) == 1:
        ans[int(x) - 1] = c
        org_idx.add(int(x) - 1)

    elif int(t) == 2:
        state = "lower"
        org_idx = set()
    else:
        state = "upper"
        org_idx = set()

for i in range(n):
    if i in org_idx:
        print(ans[i], end="")
    elif ans[i] != None:
        if state == "lower":
            print(ans[i].lower(), end="")
        elif state == "upper":
            print(ans[i].upper(), end="")
        else:
            print(ans[i], end="")
    else:
        if state == "lower":
            print(s[i].lower(), end="")
        elif state == "upper":
            print(s[i].upper(), end="")
        else:
            print(s[i], end="")

print()
