n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(101):
    s = sum(sorted(a + [i])[1:-1])
    if x <= s:
        print(i)
        exit()

print(-1)
