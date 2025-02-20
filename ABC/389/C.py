q = int(input())

acc = [0]
diff = 0
s = 0

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        acc.append(acc[-1] + query[1])

    elif query[0] == 2:
        s += 1
        diff = acc[s]

    else:
        print(acc[query[1] + s - 1] - diff)
