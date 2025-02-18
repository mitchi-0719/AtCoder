n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
s = [0 for _ in range(n)]

for i in range(n):
    s[q[i] - 1] = q[p[i] - 1]

print(*s)
