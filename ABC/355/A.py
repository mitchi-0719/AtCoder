a, b = map(int, input().split())
n = [1, 2, 3]
try:
    n.remove(a)
    n.remove(b)
    print(n[0])
except:
    print(-1)
