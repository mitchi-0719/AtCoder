# AC

n = int(input())
s = input()

if n > 2:
    for i in range(len(s)-1):
        buffer = s[i]
        if buffer == s[i+1]:
            print("No")
            exit()

print("Yes")