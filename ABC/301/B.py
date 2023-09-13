n = int(input())
a = list(map(int, input().split()))

for i in range(n-1):
    print(a[i], end=" ")
    if abs(a[i] - a[i+1]) != 1:
        if a[i] < a[i+1]:
            j = a[i]+1
            while j < a[i+1]:
                print(j, end=" ")
                j += 1
        elif a[i] > a[i+1]:
            j = a[i]-1
            while j > a[i+1]:
                print(j, end=" ")
                j -= 1

print(a[-1])