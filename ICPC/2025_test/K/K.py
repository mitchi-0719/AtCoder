def solve():
    a, b = map(int, input().split())
    if a == b == 0:
        return True

    print(a * b)


while not solve():
    ...
