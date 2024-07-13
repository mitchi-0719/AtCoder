l = list(map(int, input().split()))
c = input()
ci = 0 if c == "Red" else 1 if c == "Green" else 2

if min(l) == l[ci]:
    l[ci] = 10000
    print(min(l))
else:
    print(min(l))
