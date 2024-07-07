import sys

sys.setrecursionlimit(10**8)


def count_leaves(tree, r, p):
    if len(tree[r]) == 1 and tree[r] == p:
        return 1

    s = 1
    for ti in tree[r]:
        if ti != p:
            s += count_leaves(tree, ti, r)

    return s


n = int(input())
tree = [[] for _ in range(n + 1)]

for i in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

leaves = 0
m = 0
for ti in tree[1]:
    leave = count_leaves(tree, ti, 1)
    m = max(m, leave)
    leaves += leave

print(leaves - m + 1)
