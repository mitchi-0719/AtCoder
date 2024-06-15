class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def search_root(s):
    ls, le = 0, 0
    start, end = None, None

    for i, si in enumerate(s):
        if si == "(":
            ls += 1
        elif si == ")":
            le += 1
        elif ls == le:
            if si == "[":
                start = i
            elif si == "]":
                end = i
                break
    return start, end


def make_tree(s):
    rs, re = search_root(s)
    if not (rs and re):
        return None

    root = Node(s[rs : re + 1])
    root.left = make_tree(s[1 : rs - 1])
    root.right = make_tree(s[re + 2 : -1])

    return root


def merge_tree(root1, root2):
    root = Node(f"[{int(root1.v[1:-1]) + int(root2.v[1:-1])}]")
    if root1.left and root2.left:
        root.left = merge_tree(root1.left, root2.left)

    if root1.right and root2.right:
        root.right = merge_tree(root1.right, root2.right)

    return root


def encode_tree(root):
    if not root:
        return "()"

    return f"({encode_tree(root.left)}{root.v}{encode_tree(root.right)})"


tree_a = make_tree(input())
tree_b = make_tree(input())
merged_tree = merge_tree(tree_a, tree_b)

print(encode_tree(merged_tree)[1:-1])
