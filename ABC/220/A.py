a, b, c = map(int, input().split())

n = c
while n < a:
    n += c

print(n if n <= b else -1)