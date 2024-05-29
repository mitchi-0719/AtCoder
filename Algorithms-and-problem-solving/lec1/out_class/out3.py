n, m, t = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
j = 0
i = 0
fin = False
while i < t:
    if not fin and a[j] - i == m:
        i += m
    elif not fin and a[j] == i:
        j += 1
        fin = j == n
        if not fin and a[j] - a[j - 1] < m * 2:
            i = a[j]
        else:
            i += m
    else:
        ans += 1
        i += 1

print(ans)
