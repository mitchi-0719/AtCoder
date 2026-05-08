"""
g: 連結リスト
color: 状態(0: 未処理, 1: 処理中, 2: 処理済み) [0]*n
parent: 親ノード記録配列 [-1]*n
u: 現在のノード
"""


def color_dfs(g, color, parent, u):  # 閉路検索&閉路復元
    color[u] = 1  # 処理中にする

    for v in g[u]:
        if color[v] == 1:  # 閉路発見
            # 閉路復元処理
            cycle = []
            cur = u
            cycle.append(v)
            while cur != v:
                cycle.append(cur)
                cur = parent[cur]
            cycle.append(v)
            cycle.reverse()  # 順方向に直す
            return cycle

        # 処理完了（黒）は無視
        elif color[v] == 2:
            continue

        # 未訪問（白）の場合は再帰的に探索
        parent[v] = u
        result = color_dfs(g, color, parent, v)
        if result:
            return result
        parent[v] = -1

    # 処理完了（黒）にする
    color[u] = 2
    return []


def color_dfs(g, color, u):  # 閉路検索
    color[u] = 1  # 処理中にする

    for v in g[u]:
        if color[v] == 1:  # 閉路発見
            return True

        # 処理完了（黒）は無視
        elif color[v] == 2:
            continue

        # 未訪問（白）の場合は再帰的に探索
        if color_dfs(g, color, v):
            return True

    # 処理完了（黒）にする
    color[u] = 2
    return False
