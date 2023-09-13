# AC

n, m, h, k = map(int, input().split())
s = input()

move_list = {"R":[1, 0], "L":[-1, 0], "U":[0, 1], "D":[0, -1]}

item = [tuple(map(int, input().split())) for l in range(m)]
item = set(item)

x = 0
y = 0

for i in s:
    move = move_list[i]
    x += move[0]
    y += move[1]
    h -= 1

    if h <= -1:
        print("No")
        exit()
    elif h < k and set([(x, y)]).issubset(item):
        h = k
        item.remove((x, y))

print("Yes")