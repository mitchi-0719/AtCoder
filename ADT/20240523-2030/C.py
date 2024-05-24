n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    for j, _a in enumerate(a):
        if _a == 1:
            print(j + 1, end=" ")
    print()
