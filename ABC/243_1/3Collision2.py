#不正解

n = int(input())
X = [0] * n
Y = [0] * n
for i in range(n):
    X[i], Y[i] = map(int, input().split())
s = input()

for i in range(n):
    for j in range(i + 1, n):
        if Y[i] == Y[j]:
            if s[i] == "R" and s[j] == "L" and X[i] < X[j] or s[i] == "L" and s[j] == "R" and X[i] > X[j]:
                print("Yes")
                exit()

print("No")