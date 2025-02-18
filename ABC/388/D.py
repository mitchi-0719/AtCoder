import heapq

n = int(input())
a = list(map(int, input().split()))
celebrated = []
offset = 0

for i in range(n):
    print(max(0, a[i] - (n - i - 1) + len(celebrated)), end=" ")

    if len(celebrated) > 0 and celebrated[0] - offset <= 0:
        heapq.heappop(celebrated)

    heapq.heappush(celebrated, a[i] + offset)
    offset += 1
