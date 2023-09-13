#AC
a, b = map(str, input().split())

if int(len(a)) < int(len(b)):
    shorter_len = len(a)
else:
    shorter_len = len(b)

for i in range(shorter_len):
    j = (i+1)*-1
    if int(a[j]) + int(b[j]) >= 10:
        print("Hard")
        exit()

print("Easy")