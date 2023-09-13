#不正解

import math

s = input()

bottom = 0
top = len(s) - 1
top_a = 0
bottom_a = 0
fin_t = True
fin_b = True

for i in range(len(s) // 2):
    if fin_b or fin_t:
        if fin_t and s[top] == "a":
            top_a += 1
        else:
            fin_t = False
        if fin_b and s[bottom] == "a":
            bottom_a += 1
        else:
            fin_b = False
        top -= 1
        bottom += 1
    else:
        break

times = math.ceil(len(s) / 2) - top_a
bottom = bottom_a
top = len(s) - top_a - 1

for _ in range(times):
    if s[top] != s[bottom]:
        print("No")
        exit()
print("Yes")