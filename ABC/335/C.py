n, q = map(int, input().split())
d = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}
li = [[n - i, 0] for i in range(n)]
s = n - 1

for i in range(q):
    query = input().split()
    if query[0] == "1":
        dire = d[query[1]]
        head = [l + dire[j] for j, l in enumerate(li[s])]
        li.append(head)
        s += 1
    else:
        p = int(query[1])
        print(*li[s - p + 1])
