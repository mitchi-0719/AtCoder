from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


class UnionFind:
    # 各要素の親要素の番号を格納するリスト
    # 要素が根（ルート）の場合は-(そのグループの要素数)を格納する
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 要素xが属するグループの根を返す
    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    # 要素xが属するグループと要素yが属するグループとを併合する
    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 要素xが属するグループのサイズ（要素数）を返す
    def size(self, x):
        return -self.parents[self.root(x)]

    # 要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.root(x) == self.root(y)

    # 要素xが属するグループに属する要素をリストで返す
    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    # すべての根の要素をリストで返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    # グループの数を返す
    def group_count(self):
        return len(self.roots())

    # {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members


def id(x, y):
    return y * w + x


def solve2(s, visited, before, w, h, uf):
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for m in move:
        x = before[0] + m[0]
        y = before[1] + m[1]
        if 0 <= x < w and 0 <= y < h and s[y][x] == "." and not visited[id(x, y)]:
            uf.union(id(before[0], before[1]), id(x, y))
            visited[id(x, y)] = True
            solve2(s, visited, [x, y], w, h, uf)


def solve(w, h):
    uf = UnionFind(w * h)
    s = []
    start = []
    for i in range(h):
        s.append(list(input()))
        if "@" in s[i]:
            start = [s[i].index("@"), i]

    visited = [False for _ in range(w * h)]

    solve2(s, visited, start, w, h, uf)
    print(uf.size(id(start[0], start[1])))


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        exit()
    solve(w, h)
