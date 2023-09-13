#AC

import math

a, b, c = map(int, input().split())


r = int(math.gcd(a, math.gcd(b, c)))

print(int((a // r - 1) + (b // r - 1) + (c // r - 1)))