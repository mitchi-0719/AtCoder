n = int(input())
s = input()

for i in range(n - 1):
    if (s[i], s[i + 1]) == ("a", "b") or (s[i], s[i + 1]) == ("b", "a"):
        print("Yes")
        exit()
print("No")
