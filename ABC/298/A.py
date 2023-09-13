n = int(input())
s = input()

if set(["o"]).issubset(set(s)) and not(set(["x"]).issubset(set(s))):
    print("Yes")
else:
    print("No")
