def solve():
    n = int(input())
    if n == 0:
        return 1
    a = list(map(int, input().split()))
    a = [abs(ai - 2023) for ai in a]
    a, i = zip(*sorted(zip(a, [i + 1 for i in range(n)])))

    print(i[0])


while 1:
    if solve():
        break
