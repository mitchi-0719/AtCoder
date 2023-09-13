a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0

for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            five_hundred = i * 500
            hundred = j * 100
            fifty = k * 50
            yen = five_hundred + hundred + fifty
            print(yen)
            if yen == x:
                count += 1

print(count)