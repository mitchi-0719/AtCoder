s = input()
t = input()

diff = ord(s[0]) - ord(t[0])
for i in range(1, len(s)):
    if diff != ord(s[i]) - ord(t[i]):
        print("No")
        exit()

print("Yes")