import math

x, y = map(int, input().split())

print(max(math.ceil((y - x) / 10), 0))