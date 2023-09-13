n, Y = map(int, input().split())

x = -1
y = -1
z = -1
end = False

for i in range(n + 1):
    for j in range(n + 1):
        k = n - i - j
        if k < 0:
            break
        man = i * 10000
        sen_5 = j * 5000
        sen = k * 1000
        yen = man + sen_5 + sen
        if Y - yen == 0:
            print(i, j, k)
            end = True
            break
    if end == True:
        break

if end == False:
    print(x, y, z)