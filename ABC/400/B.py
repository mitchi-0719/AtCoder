n, m = map(int, input().split())

try:
    x = sum([n**i for i in range(m + 1)])

    if x > 10**9:
        print("inf")
    else:
        print(x)
except:
    print("inf")
