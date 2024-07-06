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


def id(i, j):
    return i * w + j


def judge(i, j):
    related_set = set()
    dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for x, y in dire:
        if 0 <= i + y < h and 0 <= j + x < w and s[i + y][j + x] == "#":
            related_set.add(uf.root(id(i + y, j + x)))

    return len(related_set)


h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
red = 0
for si in s:
    red += si.count(".")
uf = UnionFind(h * w)


for i in range(h):
    for j in range(w - 1):
        if s[i][j] == s[i][j + 1] == "#":
            uf.union(id(i, j), id(i, j + 1))

for i in range(h - 1):
    for j in range(w):
        if s[i][j] == s[i + 1][j] == "#":
            uf.union(id(i, j), id(i + 1, j))

base_cnt = uf.group_count() - red

cnt = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            cnt += base_cnt - judge(i, j) + 1

mod = 998244353
q_inv = pow(red, mod - 2, mod)
r = (cnt * q_inv) % mod
print(r)
