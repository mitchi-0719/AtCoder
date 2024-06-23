n, q = map(int, input().split())
s = input()
acc = [0]

for i in range(n - 1):
    acc.append(acc[i] + (1 if s[i] == s[i + 1] else 0))

for _ in range(q):
    l, r = map(int, input().split())
    print(acc[r - 1] - acc[l - 1])
