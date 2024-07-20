n, t, p = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse=True)

m = min(l[:p])
print(max(0, t - min(l[:p])))
