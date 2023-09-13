#answer

n, m = map(int, input().split())
S = input().split()
T = set(input().split())

for i in S:
    print("Yes" if i in T else "No")