from itertools import accumulate

n, x, y = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())), reverse=True)

a_acc = list(accumulate(a))
b_acc = list(accumulate(b))

for i in range(n):
    if a_acc[i] > x or b_acc[i] > y:
        print(i + 1)
        exit()

print(n)
