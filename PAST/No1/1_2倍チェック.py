li = [str(i) for i in range(10)]

check = True
s = input()
for i in range(3):
    if s[i] not in li:
        check = False
        break

if check:
    print(int(s) * 2)
else:
    print("error")