n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
is_not_pair = [True for i in range(n)]

cnt = 0
for i in range(1, n):
    if a[i-1] == a[i] and is_not_pair[i-1] and is_not_pair[i]:
        cnt += 1
        is_not_pair[i] = is_not_pair[i-1] = False

print(cnt)