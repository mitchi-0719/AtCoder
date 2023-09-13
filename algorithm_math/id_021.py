n, r = map(int, input().split())

def fact(m):
    if m == 0:
        return 1
    else:
        return m * fact(m-1)

print(int(fact(n)/(fact(n-r)*fact(r))))