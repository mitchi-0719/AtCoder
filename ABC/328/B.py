n = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(1, d[i] + 1):
        if (
            set(str(i + 1)) == set(str(j))
            and len(set(str(i + 1))) == len(set(str(j))) == 1
        ):
            ans += 1

print(ans)
