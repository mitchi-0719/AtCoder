p, q = map(str, input().split())

dist = [3, 1, 4, 1, 5, 9]

if p < q:
    min_idx = ord(p)-65
    max_idx = ord(q)-65
else:
    min_idx = ord(q)-65
    max_idx = ord(p)-65

print(sum(dist[min_idx:max_idx]))