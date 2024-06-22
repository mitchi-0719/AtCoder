import heapq

n, d = map(int, input().split())
dic = dict()

for i in range(n):
    x, y = map(int, input().split())
    dic[x] = [*dic.get(x, []), -y]

w = []
ans = 0
for i in range(1, d + 1):
    if dic.get(i):
        for di in dic[i]:
            heapq.heappush(w, di)
    if len(w) != 0:
        ans += -heapq.heappop(w)

print(ans)
