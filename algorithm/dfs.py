"""
g: 隣接リスト
i: 見ているノード
visit: 到達したノードのリスト
"""


def dfs(g, i, visit):
    if visit[i]:
        return

    visit[i] = True
    for v in g[i]:
        dfs(g, v, visit)
