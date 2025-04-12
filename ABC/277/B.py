#AC
n = int(input())

s = [input() for _ in range(n)]
char1 = ["H", "D", "C", "S"]
char2 = ["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" ]

for i in range(n):
    if not(s[i][0] in char1) or not(s[i][1] in char2) or s.count(s[i]) != 1:
        print("No")
        exit()

print("Yes")