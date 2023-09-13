import math

a, b, d = map(int, input().split())

rad_d = math.radians(d)

rote_a = a * math.cos(rad_d) - b * math.sin(rad_d)
rote_b = a * math.sin(rad_d) + b * math.cos(rad_d)

print(rote_a, rote_b)