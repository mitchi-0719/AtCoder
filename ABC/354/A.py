h = int(input())

i = 0
p_h = 0
while True:
    p_h += 2**i
    if h < p_h:
        print(i + 1)
        exit()
    i += 1
