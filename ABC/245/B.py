n = int(input())
a = [-1] + sorted(list(set(map(int, input().split()))))

for i in range(len(a) - 1):
    if a[i] + 1 != a[i + 1]:
        print(a[i] + 1)
        exit()

print(a[-1] + 1)
