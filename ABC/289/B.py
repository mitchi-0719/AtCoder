n, m = map(int, input().split())
a = set(map(int, input().split()))

nums = [i + 1 for i in range(n)]
tmp = []

for num in nums:
    if num in a:
        tmp.append(num)
    else:
        print(num, end=" ")
        if len(tmp) != 0:
            print(*reversed(tmp), end=" ")
        tmp = []

print()
