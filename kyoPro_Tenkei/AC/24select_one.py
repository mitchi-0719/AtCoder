# AC

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dis = 0

for i in range(n):
    dis += abs(A[i] - B[i])

if dis <= k and abs(dis - k) % 2 == 0:
    print("Yes")
else:
    print("No")