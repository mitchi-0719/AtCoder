import math
n, x = map(int, input().split())

print(chr(64 + math.ceil(x / n)))