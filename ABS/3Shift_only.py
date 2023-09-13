n = int(input())
a = list(map(int, input().split()))
check = True
count = 0

def division():
    global n, check
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i] / 2
        else:
            check = False
            break

while check == True:
    division()
    if check == True:
        count += 1
print(count)