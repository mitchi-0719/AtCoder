n = int(input())
s = input()

max_lev = -1

if len(set(s)) == 1:
    print(-1)
    exit()

def judge_level(ss, idx):
    j = 1
    while idx + j < n and ss[j] == "o":
        j += 1
    return j

i = 0
while i < n:
    lev = judge_level(s[i:], i)
    before_i = i
    i += lev
    if s[before_i] == "-":
        lev -= 1
    max_lev = max(lev, max_lev)

print(max_lev)