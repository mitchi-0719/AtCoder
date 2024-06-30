s = list(input())
ss = list(set(s))

if s.count(ss[0]) == 1:
    print(s.index(ss[0]) + 1)
else:
    print(s.index(ss[1]) + 1)
