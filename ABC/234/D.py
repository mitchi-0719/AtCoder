import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))

l = p[:k]
heapq.heapify(l)
for i in range(k, n):
    m = l[0]
    if m < p[i]:
        heapq.heappush(l, p[i])
        m = heapq.heappop(l)
    print(m)

print(l[0])
