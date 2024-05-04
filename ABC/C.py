n = int(input())
a, b = [], []
diff = []

for i in range(n):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)
    diff.append(B - A)

diff, a, b = zip(*sorted(zip(diff, a, b)))
diff = list(diff)
a = list(a)
b = list(b)

print(sum(a[0: -1], b[-1]))