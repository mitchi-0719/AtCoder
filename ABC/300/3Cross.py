# WA

h, w = map(int, input().split())
ans = [0 for _ in range(h)]

c = []
cnt = 0
for i in range(h):
    x = input()
    cnt += x.count("#")
    x = list(x)
    c.append(x)

if cnt == 0:
    for i in range(h):
        print(0, end=" ")

def print_ans():
    for x in ans:
        print(x, end=" ")

def replace(centerY, centerX, count):
    c[centerY][centerX] = "."
    for x in range(1, count+1):
        c[centerY-x][centerX-x] = "."
        c[centerY+x][centerX-x] = "."
        c[centerY-x][centerX+x] = "."
        c[centerY+x][centerX+x] = "."

for i in range(h):
    for j in range(w):
        ans_cnt = 1
        if c[i][j] == "#":

            idxh = i+1
            idxw = j+1

            get = c[idxh][idxw]

            while get == "#" and c[idxh-1][idxw+1] != "#":
                ans_cnt += 1
                idxh += 1
                idxw += 1
                get = c[idxh][idxw]
            ans[ans_cnt-1] += 1
            cnt -= (ans_cnt*4+1)

            if cnt <= 0:
                print_ans()
                exit()

            replace(idxh, idxw, ans_cnt)
            j += (ans_cnt*2+1)