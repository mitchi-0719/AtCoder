#answer

n = int(input())
P = list(map(int, input().split()))

cnt = [0 for _ in range(n)]

for i in range(n):
    for j in range(3):
        cnt[(P[i] - 1 - i - j) % n] += 1

print(cnt)
print(max(cnt))