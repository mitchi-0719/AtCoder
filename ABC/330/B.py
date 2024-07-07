n, l, r = map(int, input().split())

for ai in list(map(int, input().split())):
    if ai <= l:
        print(l, end=" ")
    elif r <= ai:
        print(r, end=" ")
    else:
        print(ai, end=" ")

print()
