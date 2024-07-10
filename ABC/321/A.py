n = input()
before = int(n[0])

for ni in n[1:]:
    if before <= int(ni):
        print("No")
        exit()
    before = int(ni)

print("Yes")
