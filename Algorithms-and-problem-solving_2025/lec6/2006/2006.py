buttons = [
    [],
    [".", ",", "!", "?", " "],
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"],
    ["p", "q", "r", "s"],
    ["t", "u", "v"],
    ["w", "x", "y", "z"],
]

n = int(input())
for _ in range(n):
    ans = ""
    b = 0
    k = 0
    t = input()

    for ti in t:
        if int(ti) == 0:
            if b != 0:
                ans += buttons[b][k]
                b = 0
                k = 0
        else:
            if int(ti) == b:
                k = (k + 1) % len(buttons[b])
            else:
                b = int(ti)
                k = 0

    print(ans)
