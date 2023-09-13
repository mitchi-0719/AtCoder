from copy import deepcopy

h, w = map(int, input().split())

c = []
cnt = h*w

marks_true= [True for i in range(w)]
marks_false= [False for i in range(w)]
marks = []

for i in range(h):
    c.append(input())
    if len(set(c[i])) == 1:
        marks.append(deepcopy(marks_true))
        cnt -= w
    else:
        marks.append(deepcopy(marks_false))

for j in range(w):
    arr = []
    for i in range(h):
        arr.append(c[i][j])
    if len(set(arr)) == 1 and len(arr) != 1:
        for k in range(h):
            if not marks[k][j]:
                marks[k][j] = True
                cnt -= 1
    arr.clear()

print(marks)

print(cnt)
