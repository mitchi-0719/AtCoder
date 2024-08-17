x = input()

ans = ""
rm = True
for xi in x[::-1]:
    if xi != "0":
        rm = False

    if not rm:
        ans = xi + ans

if ans[-1] == ".":
    print(ans[:-1])
else:
    print(ans)
