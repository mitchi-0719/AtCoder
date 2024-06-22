n = int(input())
li = []
for i in range(n):
    if len(li) == 0:
        li.append(1)
    else:
        li.append(li[i-1]*10 + 1)

digits = 1
for i in range(n):
    