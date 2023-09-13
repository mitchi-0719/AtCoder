h, w = map(int, input().split())

for i in range(h):
    a = list(map(int, input().split()))
    for j in a:
        if j == 0:
            print(".", end="")
        else:
            print(chr(j+64), end="")
    print()
