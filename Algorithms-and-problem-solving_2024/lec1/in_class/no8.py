def solve(s):
    rnd = ["(", ")"]
    sq = ["[", "]"]
    start = ["(", "["]
    end = [")", "]"]
    stack = []
    for t in s:
        if t in start:
            stack.append(t)
        elif t in end:
            if len(stack) != 0:
                if not (
                    (stack[-1] == rnd[0] and t == rnd[1])
                    or (stack[-1] == sq[0] and t == sq[1])
                ):
                    return False
                else:
                    stack.pop(-1)
            else:
                return False

    return len(stack) == 0


while True:
    s = input()
    if s == ".":
        exit()

    print("yes" if solve(s) else "no")
