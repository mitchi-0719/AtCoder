import itertools

s = input()
before = ord("A") - 1
for s, i in itertools.groupby(s):
    if before >= ord(s):
        print("No")
        exit()
    before = ord(s)

print("Yes")
