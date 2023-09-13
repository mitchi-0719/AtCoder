import math
a, b = map(int, input().split())

if len(str(a)) >= 17:
    a1 = int(str(a)[:9])
    a2 = int(str(a)[9:])
    print(math.floor(a1/b*1000000000) + math.ceil(a2/b))
else:
    print(math.ceil(a/b))
