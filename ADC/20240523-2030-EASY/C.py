n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    for i, _a in enumerate(a):
        if _a == 1:
            print(i + 1, end=" ")
    print()
