n = int(input())
s = list(input())
now = [0, 0]
xy = set([tuple(now)])
move = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}

for si in s:
    x, y = move[si]
    now[0] += x
    now[1] += y

    if tuple(now) in xy:
        print("Yes")
        exit()
    else:
        xy.add(tuple(now))

print("No")
