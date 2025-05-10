# AC

n = int(input())
s = set()

for i in range(n):
    S = input()
    if not set([S]).issubset(s):
        s.add(S)
        print(i+1)
