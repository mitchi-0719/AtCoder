#正解

v, a, b, c = map(int, input().split())
li = [a, b, c]
printer = ["F", "M", "T"]
i = -1

v = v % (a + b + c)

while v >= 0:
    i = (i + 1) % 3
    v -= li[i]

print(printer[i])