# AC

n, a, b = map(int, input().split())
c = list(map(int, input().split()))

idx = c.index(a+b)+1
print(idx)