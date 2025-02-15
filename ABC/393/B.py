s = input()

cnt = 0
for i in range(len(s) - 2):
    for j in range(i + 1, len(s) - 1):
        for k in range(j + 1, len(s)):
            if ("A", "B", "C") == (s[i], s[j], s[k]) and j - i == k - j:
                cnt += 1

print(cnt)
