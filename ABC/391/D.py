n, w = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]
q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
