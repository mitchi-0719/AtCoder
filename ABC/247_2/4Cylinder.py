#不正解
q = int(input())
query = [input() for _ in range(q)]

def calc():
    global point, ans, fin, num
    if num <= pole[point + 1]:
        ans += num * pole[point]
        pole[point + 1] -= num
        fin = True
    else:
        ans += pole[point + 1] * pole[point]
        num -= pole[point + 1]
        point += 2

pole = [0]
point = 1
stList = [0] * 3

for i in range(q):
    st = str(query[i])
    cnt = 0
    front = 0
    stList = [0 for i in range(3)]

    for j in range(len(st)):
        if st[j] == " ":
            stList[cnt] = int(st[front : j])
            front = j + 1
            cnt += 1
        elif cnt + int(st[0]) == 3:
            stList[cnt] = int(st[front :])


    if stList[0] == 1:
        pole.extend([stList[1], stList[2]])

    elif stList[0] == 2:
        ans = 0
        fin = False
        num = stList[1]
        while fin == False:
            calc()

        print(ans)