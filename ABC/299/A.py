n = int(input())
s = input()

if s.index("|") < s.index("*") < n-s[::-1].index("|")-1:
    print("in")
else:
    print("out")