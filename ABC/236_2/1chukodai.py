#正解

s = list(input())
a, b = map(int, input().split())

buffer = s[a - 1]
s[a - 1] = s[b - 1]
s[b - 1] = buffer

for i in range(len(s)):
    print(s[i], end="")