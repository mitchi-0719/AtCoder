n = int(input())
a = list(map(int, input().split()))

li = [0] * 3
for i in a:
    li[i-1] += 1

cnt = 0

for i in li:
    cnt += (i*(i-1)) / 2

print(int(cnt))