cnt = 0

for i in range(12):
    s = input()
    if len(s) == i+1:
        cnt += 1

print(cnt)