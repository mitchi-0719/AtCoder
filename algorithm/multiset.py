# https://tsubo.hatenablog.jp/entry/2020/06/15/124657
import heapq
from sys import exit


class HeapDict:
    def __init__(self):
        self.h = []
        self.d = dict()

    # 値の挿入
    def insert(self, x):
        heapq.heappush(self.h, x)
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    # 値の削除
    def erase(self, x):
        if x not in self.d or self.d[x] == 0:
            print(x, "is not in HeapDict")
            exit()
        else:
            self.d[x] -= 1

        while len(self.h) != 0:
            if self.d[self.h[0]] == 0:
                heapq.heappop(self.h)
            else:
                break

    # 値の存在
    def is_exist(self, x):
        if x in self.d and self.d[x] != 0:
            return True
        else:
            return False

    # 最小値の取得
    def get_min(self):
        return self.h[0]
