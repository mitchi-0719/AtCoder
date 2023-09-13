h, w = map(int, input().split())
a = []

ans = 0

def dfs(i, j, s):
    if a[i][j] in s:
        return
    s.add(a[i][j])
    if i == h-1 and j == w-1:
        global ans
        ans += 1
        return
    if j+1 < w: dfs(i, j+1, s)
    if i+1 < h: dfs(i+1, j, s)

for i in range(h):
    A = list(map(int, input().split()))
    a.append(A)

s = set()
dfs(0, 0, s)

print(ans)