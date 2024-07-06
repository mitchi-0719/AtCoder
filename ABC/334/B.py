import math

a, m, l, r = map(int, input().split())
print(
    max(
        0,
        (r - a) // m - ((l - a) // m + (1 if ((l - a) % m) != 0 else 0)) + 1,
    )
)
