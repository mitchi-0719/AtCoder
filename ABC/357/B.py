s = input()
l_cnt = 0
r_cnt = 0

for i in s:
    if "a" <= i <= "z":
        r_cnt += 1
    else:
        l_cnt += 1

if r_cnt < l_cnt:
    print(s.upper())
else:
    print(s.lower())
