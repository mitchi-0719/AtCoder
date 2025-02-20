x = int(input())

i = 1
cnt = 0
while True:
    if i == x:
        print(cnt)
        break

    cnt += 1
    i *= cnt
