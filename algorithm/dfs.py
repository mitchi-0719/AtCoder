"""
g: 隣接リスト
i: 見ているノード
visited: 到達したノードのリスト
"""


def dfs(g, i, visited):
    if visited[i]:
        return

    visited[i] = True
    for v in g[i]:
        dfs(g, v, visited)
