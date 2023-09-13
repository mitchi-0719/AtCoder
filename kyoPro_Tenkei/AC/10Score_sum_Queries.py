#AC

n = int(input())
C = [0] * n
P = [0] * n
S1 = [0] * n
S2 = [0] * n

for i in range(n):
    C[i], P[i] = map(int, input().split())
    if i == 0:
        if C[i] == 1:
            S1[i] = P[i]
        else:
            S2[i] = P[i]
    else:
        if C[i] == 1:
            S1[i] = S1[i - 1] + P[i]
            S2[i] = S2[i - 1]
        else:
            S1[i] = S1[i - 1]
            S2[i] = S2[i - 1] + P[i]

q = int(input())
L = [0] * q
R = [0] * q

for i in range(q):
    L[i], R[i] = map(int, input().split())
    if L[i] == 1:
        left_S1 = 0
        left_S2 = 0
    else:
        left_S1 = S1[L[i] - 2]
        left_S2 = S2[L[i] - 2]
    C_one = S1[R[i] - 1] - left_S1
    C_two = S2[R[i] - 1] - left_S2
    print(C_one, C_two)