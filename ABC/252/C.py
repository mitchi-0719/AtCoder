# AC

n = int(input())
s = []
max_sec = 10000

for i in range(n):
    s.append(input())

for i in range(10):
    sec_arr = []
    for j in s:
        sec = j.index(str(i))
        while sec in sec_arr:
            sec += 10
        sec_arr.append(sec)
    buffer = max(sec_arr)
    max_sec = min(max_sec, buffer)

print(max_sec)
