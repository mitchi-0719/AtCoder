s = list(map(int, input().split()))

judge = 100 <= s[0] <= 675 and s[0] % 25 == 0
for i in range(1, len(s)):
    if not(judge) or s[i-1] > s[i] or not(100 <= s[0] <= 675) or s[0] % 25 != 0:
            print("No")
            exit()

print("Yes")