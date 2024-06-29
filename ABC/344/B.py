a = int(input())
al = []
while a != 0:
    al.append(a)
    a = int(input())
al.append(a)

for i in al[::-1]:
    print(i)
