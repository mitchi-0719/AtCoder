n, l = map(int, input().split())
ans = 0

for ai in list(map(int, input().split())):
    if ai >= l:
        ans += 1

print(ans)
