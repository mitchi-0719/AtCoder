n, k = map(int, input().split())
s = input()

for si in s:
    if si == "o":
        k -= 1

    print(si if k >= 0 else "x", end="")

print()
