s = list(map(int, input().split()))
t = list(map(int, input().split()))

y_dist = abs(s[1] - t[1])
if sum(s) % 2 == 0:
    s[0] += 1

if sum(t) % 2 == 0:
    t[0] += 1

x_dist = max(0, abs(s[0] - t[0]) // 2 - y_dist // 2)

print(max(0, x_dist + y_dist))
