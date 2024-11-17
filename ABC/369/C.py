n = int(input())
a = list(map(int, input().split()))

d = [a[i] - a[i + 1] for i in range(n - 1)]
ans = 2 * n - 1

if n >= 2:
    b = d[0]
    bi = 0
    for i in range(1, n - 1):
        if d[i] == b:
            ans += i - bi
        else:
            bi = i
            b = d[i]

print(ans)
