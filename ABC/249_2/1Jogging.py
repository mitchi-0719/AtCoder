#正解

a, b, c, d, e, f, x = map(int, input().split())

time = a + c
takahashi = x // time * a * b
if x % time <= a:
    takahashi += (x % time) * b
else:
    takahashi += a * b

time = d + f
aoki = x // time * d * e
if x % time <= d:
    aoki += (x % time) * e
else:
    aoki += d * e

if takahashi < aoki:
    print("Aoki")
elif takahashi > aoki:
    print("Takahashi")
else:
    print("Draw")