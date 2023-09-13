n = int(input())
a = list(map(int, input().split()))
a_diff = [a[i+1]-a[i] for i in range(n-1)]
q = int(input())

print(a_diff)
for i in range(q):
    l, r = map(int, input().split())
    sum = 0
    for j in range(n):
        if a[j] <= l <= a[j+1] and j % 2 == 1:
            sum += a[j+1] - l
            print("1", sum, j)
        elif a[j-1] <= r <= a[j]:
            sum -= a[j] - r
            print("2", sum, j)
            break
        elif l <= a[j] <= r and j % 2 == 1:
            sum += a_diff[j]
            print("3", sum, j)
    print(sum)