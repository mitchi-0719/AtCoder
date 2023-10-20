n = int(input())
a = list(map(int, input().split()))
x = int(input())

a_sum = sum(a)
cnt = (x // a_sum) * n
m = x % a_sum

for val in a:
    if m < 0:
        print(cnt)
        exit()
    m -= val
    cnt += 1

print(cnt)
