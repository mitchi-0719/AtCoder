n = int(input())
q = int(input())

box = [[] for _ in range(n)]
cards = [set([]) for _ in range(2*(10**5))]

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        box[query[2]-1].append(query[1])
        cards[query[1]-1].add(query[2])
    elif query[0] == 2:
        box[query[1]-1] = sorted(box[query[1]-1])
        for j in range(len(box[query[1]-1])):
            print(box[query[1]-1][j], end=" ")
        print()
    else:
        sort_card = sorted(list(cards[query[1]-1]))
        for j in range(len(sort_card)):
            print(sort_card[j], end=" ")
        print()

