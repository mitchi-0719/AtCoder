#正解
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        esc = "1"
    else:
        st = str(i)
        esc = esc + " " + st + " " + esc

print(esc)