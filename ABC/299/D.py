n = int(input())
af_s = 1
n -= 1
print("?", n)
s = int(input())

while True:
    if af_s + s == 1:
        print("!", n)
        exit()
    else:
        n -= 1
        print("?", n)
        af_s = s
        s = int(input())