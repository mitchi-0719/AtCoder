n = int(input())
s = [input() for _ in range(n)]

for i in range(n - 2):
    if s[i] == s[i + 1] == "sweet":
        print("No")
        exit()

print("Yes")
