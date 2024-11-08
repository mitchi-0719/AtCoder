n = int(input())
s = input()
c = list(map(int, input().split()))

l0 = [c[0] if s[0] == 1 else 0]
l1 = [c[0] if s[0] == 0 else 0]
r0 = [c[-1] if s[-1] == 1 else 0]
r1 = [c[-1] if s[-1] == 0 else 0]

for i in range(1, n):
    l0.append(l0[i - 1] + (c[i] if s[i] == str(i % 2) else 0))
    l1.append(l1[i - 1] + (c[i] if s[i] == str(i % 2 + 1) else 0))
    r0.append(r0[i - 1] + (c[-(i - 1)] if s[-(i - 1)] == str(i % 2) else 0))
    r1.append(r1[i - 1] + (c[-(i - 1)] if s[-(i - 1)] == str(i % 2 + 1) else 0))

print(l0, l1, r0, r1)
