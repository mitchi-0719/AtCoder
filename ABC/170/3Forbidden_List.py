# AC

x, n = map(int, input().split())
p = list(map(int, input().split()))
ab = []

diff = 0
while True:
    if x-diff not in p:
        print(x-diff)
        exit()
    elif x+diff not in p:
        print(x+diff)
        exit()
    diff += 1