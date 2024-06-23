n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted([(ai, True) for ai in a] + [(bi, False) for bi in b])

before = c[0]
for ci in c[1:]:
    if before[1] and ci[1]:
        print("Yes")
        exit()
    before = ci


print("No")
