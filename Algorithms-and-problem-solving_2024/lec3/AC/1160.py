class UnionFind:
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x  # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x])  # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False  # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]:  # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx  # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]:  # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]  # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


while True:
    w, h = map(int, input().split())
    if h == w == 0:
        exit()

    cnt = 1
    c = []
    for i in range(h):
        ci = list(map(int, input().split()))
        for j in range(len(ci)):
            if ci[j] != 0:
                ci[j] = cnt
                cnt += 1
        c.append(ci)

    uf = UnionFind(cnt - 1)
    dif = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if not (i == j == 0)]

    for i in range(h):
        for j in range(w):
            if c[i][j] != 0:
                for x, y in dif:
                    if 0 <= i + y < h and 0 <= j + x < w and c[i + y][j + x] != 0:
                        uf.unite(c[i][j] - 1, c[i + y][j + x] - 1)

    print(uf.par.count(-1))
