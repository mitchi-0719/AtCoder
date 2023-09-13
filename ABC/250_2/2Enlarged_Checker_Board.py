#正解

N, a, b = map(int, input().split())

buffer1 = ""
buffer2 = ""
for i in range(N):
    if i % 2 == 0:
        for j in range(b):
            buffer1 += '.'
            buffer2 += '#'
    else:
        for j in range(b):
            buffer1 += '#'
            buffer2 += '.'

out1 = ""
out2 = ""
for i in range(a):
    out1 += buffer1
    out1 += '\n'
    out2 += buffer2
    out2 += '\n'

for i in range(N):
    if i % 2 == 0:
        print(out1, end="")
    else:
        print(out2, end="")