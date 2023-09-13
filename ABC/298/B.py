n = int(input())

from pprint import pprint

a = []
b = []

for i in range(n):
    A = list(map(int, input().split()))
    a.append(A)

for i in range(n):
    B = list(map(int, input().split()))
    b.append(B)

def judge():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] == 0:
                return False
    return True

def rotation():
    new_a = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new_a[n-j-1][i] = a[i][j]
    return new_a

for i in range(4):
    if judge():
        print("Yes")
        exit()
    a = rotation()

print("No")