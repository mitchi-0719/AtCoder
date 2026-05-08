import heapq

"""
辞書順最小となっている結果を返すトポロジカルソート
"""


# 入力gは隣接リスト（0-index、長さn）
def topological_sort(g):
    n = len(g)
    in_degree = [0] * n

    # 各ノードの入次数を計算
    for node in range(n):
        for neighbor in g[node]:
            in_degree[neighbor] += 1

    # 入次数0のノードをheapqに入れる
    queue = [i for i in range(n) if in_degree[i] == 0]
    heapq.heapify(queue)

    result = []

    # トポロジカルソートの実行
    while queue:

        # 常に入次数が0のノードの中で最も番号が小さいノードをポップする
        node = heapq.heappop(queue)
        result.append(node)

        for neighbor in g[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(queue, neighbor)

    # 閉路（サイクル）が検出された場合は空配列を返す
    if len(result) < n:
        return []

    return result
