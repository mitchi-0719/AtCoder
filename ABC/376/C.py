n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)

ans = float("inf")
buy = False

for i in range(n):
    bi = i - (1 if buy else 0)
    if n - 1 > bi and b[bi] < a[i]:
        if buy:
            print(-1)
            exit()

        buy = True
        ans = a[i]

if buy:
    print(ans)
elif not buy:
    print(a[-1])
