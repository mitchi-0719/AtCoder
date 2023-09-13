#正解

h, w = map(int, input().split())
r, c = map(int, input().split())

cnt = 4

if r == h:
    cnt -= 1
if r == 1:
    cnt -= 1
if c == w:
    cnt -= 1
if c == 1:
    cnt -= 1

print(cnt)