n = int(input())
s = input()

ss = "ABC"

for i in range(n-2):
    if s[i:i+3] == ss:
        print(i+1)
        exit()

print(-1)