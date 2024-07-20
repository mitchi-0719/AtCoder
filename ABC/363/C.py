n, k = map(int, input().split())
s = list(input())
frac = [0 for _ in range(10)]
frac[0] = 1
for i in range(9):
    frac[i + 1] = frac[i] * (i + 2)
