n = list(map(int, input().split()))

if len(set(n)) == 1:
    print("Yes")
    exit()

s = sum(n)
for ni in n:
    if s == ni * 2:
        print("Yes")
        exit()

print("No")
