"""
n：グラフの頂点の数
m：グラフの辺の数
start：経路探索のスタート位置
pos：現在の位置
nex：posと連結している頂点
dist：startから各頂点の距離
"""

import queue

n, m = map(int, input().split())

# 隣接リストの作成
g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(start):

	# 初期化などなど
	dist = [-1] * (n + 1)
	q = queue.Queue()
	dist[start] = 0
	q.put(start)

	# 幅優先探索
	while not q.empty():
		pos = q.get()
		for nex in g[pos]:
			if dist[nex] == -1:
				dist[nex] = dist[pos] + 1
				q.put(nex)

	return dist

for i in bfs(1):
    print(i)