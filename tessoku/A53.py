import heapq

q = int(input())
heap = []
heapq.heapify(heap)

for i in range(q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        heapq.heappush(heap, l[1])
    elif l[0] == 2:
        print(heap[0])
    else:
        heapq.heappop(heap)
