n = int(input())
a = list(map(int, input().split()))

li = [0] * 100000

for i in a:
    li[i-1] += 1

cnt = 0

for i in range(49999):
    cnt += li[i] * li[100000 - (i+2)]

cnt += li[49999] * (li[49999] - 1) // 2

print(cnt)