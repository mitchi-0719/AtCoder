s = sorted(list(input()), reverse=True)
t = sorted(list(input()), reverse=True)

s_diff = ord(s[0]) - ord(s[1])
if s_diff == 3:
    s_diff = 2
elif s_diff == 4:
    s_diff = 1

t_diff = ord(t[0]) - ord(t[1])
if t_diff == 3:
    t_diff = 2
elif t_diff == 4:
    t_diff = 1

print("Yes" if s_diff == t_diff else "No")
