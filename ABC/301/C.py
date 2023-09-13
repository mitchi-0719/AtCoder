s = input()
t = input()

card = "atcoder"

s_cnt = 0
t_cnt = 0
rm_cnt = 0

l = len(s)

for i in range(l):
    c = s[i-rm_cnt]

    if t[i-rm_cnt] == "@":
        t_cnt += 1
    if c == "@":
        s_cnt += 1
        continue
    if c in t:
        t = t.replace(c, "", 1)
        s = s.replace(c, "", 1)
        rm_cnt += 1

print(s)
print(t)

if len(s) - s_cnt <= t_cnt and len(t) - t_cnt <= s_cnt:
    print("Yes")
else:
    print("No")