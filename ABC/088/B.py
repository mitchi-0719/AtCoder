n = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0
turn = 0

while True:
    if len(a) == 0:
        break
    if turn % 2 == 0:
        alice += a.pop(a.index(max(a)))
    else:
        bob += a.pop(a.index(max(a)))
    turn += 1

print(alice - bob)
