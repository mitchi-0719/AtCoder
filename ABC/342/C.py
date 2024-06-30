n = int(input())
s = input()

dic = {x: x for x in "abcdefghijklmnopqrstuvwxyz"}

q = int(input())

for i in range(q):
    c, d = input().split()
    for k, v in dic.items():
        if v == c:
            dic[k] = d

for si in s:
    print(dic[si], end="")
print()
