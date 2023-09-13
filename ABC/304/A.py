n = int(input())
s = []
a = []

for i in range(n):
    S, A = input().split()
    s.append(S)
    a.append(int(A))

minA = min(a)
idx = a.index(minA)

for i in range(n):
    print(s[(idx+i) % n])