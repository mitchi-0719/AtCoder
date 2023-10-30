from itertools import product

n, m = map(int, input().split())
s = []

for i in range(m):
    s.append(list(map(int, input().split()))[1:])

p = list(map(int, input().split()))

cnt = 0
for bit in product((0, 1), repeat=n):
    for i in range(m):
        if sum(bit[si - 1] == 1 for si in s[i]) % 2 != p[i]:
            break
    else:
        cnt += 1

print(cnt)
