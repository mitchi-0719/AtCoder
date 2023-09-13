import math

n, d = map(int, input().split())
x = []
y = []

for i in range(n):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

def is_inside(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

inf_true_idx = {0}
inf_false_idx = {i for i in range(1, n)}
cont = True
add_item = set([])

while cont:
    cont = False
    inf_true_idx = inf_true_idx.union(add_item)
    add_item.clear()
    for i in inf_true_idx:

        inf_false_idx = inf_false_idx - inf_true_idx
        for j in inf_false_idx:
            if d >= is_inside(x[i], y[i], x[j], y[j]):
                add_item.add(j)
                cont = True

for i in range(n):
    if set([i]).issubset(set(inf_true_idx)):
        print("Yes")
    else:
        print("No")