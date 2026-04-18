"""
開始のノードからのそれぞれのノードの距離を求める場合。
存在を確認するだけの場合、distじゃなくてvisitにしてbooleanでも可

g: 連結リスト
n: グラフの頂点の数
m: グラフの辺の数
start: 経路探索のスタート位置
pos: 現在の位置
nex: posと連結している頂点
dist: startから各頂点の距離
"""

from collections import deque


def bfs(g, n, start):

    # 初期化などなど
    dist = [-1] * (n + 1)
    q = deque()
    dist[start] = 0
    q.append(start)

    # 幅優先探索
    while len(q) != 0:
        pos = q.popleft()
        for nex in g[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                q.append(nex)

    return dist
