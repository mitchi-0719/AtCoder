a = list(map(int, input().split()))

sum = 0

for i in range(len(a)):
    sum += a[i] * pow(2, i)

print(sum)