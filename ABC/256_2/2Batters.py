#正解

n = int(input())
A = list(map(int, input().split()))

li = [0]
for i in range(n):
    for j in range(len(li)):
        li[j] += A[i]
    li.append(0)

print(sum(i >= 4 for i in li))