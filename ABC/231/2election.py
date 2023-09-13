#正解

n = int(input())
s = [input() for _ in range(n)]

max = 0
point = 0

for i in range(n):
    count = 0
    for j in range(i, n):
        if s[i] == s[j]:
            count += 1
    if count > max:
        max = count
        point = i

print(s[point])