from collections import defaultdict


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


def id(y, x, w):
    return y * w + x


def solve():
    w, h = map(int, input().split())
    if w == h == 0:
        return True

    m = [list(input()) for _ in range(h)]
    uf = UnionFind(w * h)
    s = []
    for i in range(h):
        for j in range(w):
            if m[i][j] == "#":
                continue

            if m[i][j] == "@":
                m[i][j] = "."
                s = [i, j]

            k = id(i, j, w)
            if 0 <= i + 1 < h and m[i + 1][j] == m[i][j] == ".":
                l = id(i + 1, j, w)
                uf.union(k, l)

            if 0 <= i - 1 < h and m[i - 1][j] == m[i][j] == ".":
                l = id(i - 1, j, w)
                uf.union(k, l)

            if 0 <= j + 1 < w and m[i][j + 1] == m[i][j] == ".":
                l = id(i, j + 1, w)
                uf.union(k, l)

            if 0 <= j - 1 < w and m[i][j - 1] == m[i][j] == ".":
                l = id(i, j - 1, w)
                uf.union(k, l)

    print(len(uf.members(id(s[0], s[1], w))))


while 1:
    if solve():
        break
