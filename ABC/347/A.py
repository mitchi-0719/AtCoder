n, k = map(int, input().split())
a = list(map(int, input().split()))

for ai in a:
    if ai % k == 0:
        print(ai // k, end=" ")
print()
