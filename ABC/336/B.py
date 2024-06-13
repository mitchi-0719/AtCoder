import itertools

n = int(input())

ans = 0
for i in itertools.count():
    if n >> i & 1:
        break
    else:
        ans += 1

print(ans)
