q = int(input())

s = "1"
n = 998244353

for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        s += str(query[1])
    elif query[0] == 2:
        s = s[1:]
    else:
        print(int(s)%n)
