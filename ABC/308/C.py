n = int(input())
a = []
b = []
nums = []
ratios = []

for i in range(n):
    A, B = map(int, input().split())

    nums.append(i+1)
    a.append(A)
    b.append(B)
    ratio = a[i]/(a[i]+b[i])
    ratios.append(ratio)

ratios, nums = zip(*sorted(zip(ratios, nums)))

for i in range(1, n+1):
    print(nums[-i], end=" ")