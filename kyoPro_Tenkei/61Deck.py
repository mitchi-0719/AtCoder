#不正解

q = int(input())
T = [0] * q
X = [0] * q

for i in range(q):
    T[i], X[i] = map(int, input().split())

card = [X[0]]

def card_1(idx):
    card.append(card[len(card) - 1])
    for j in range(len(card) - 1, 0, -1):
        card[j] = card[j - 1]
    card[0] = X[idx]

def card_2(idx):
    card.append(X[idx])

def card_3(idx):
    print(card[X[idx] - 1])

for i in range(1, q):
    if T[i] == 1:
        card_1(i)
    elif T[i] == 2:
        card_2(i)
    elif T[i] == 3:
        card_3(i)