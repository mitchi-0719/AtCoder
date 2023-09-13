#clear

n = int(input())
A = [input() for _ in range(n)]
li = [[] for i in range(n)]

for i in range(n):
    s = A[i]
    for j in range(n):
        li[i].append(s[j])

k = 0
l = 0
check = True

while(k < n and check):
    l = k
    while(l < n and check):
        check = False
        if k == l:
            if A[k][l] == "-":
                check = True
        else:
            if A[k][l] == "W" and A[l][k] == "L":
                check = True
            elif A[k][l] == "L" and A[l][k] == "W":
                check = True
            elif A[k][l] == "D" and A[l][k] == "D":
                check = True
        l += 1
    k += 1
if check:
    print("correct")
else:
    print("incorrect")