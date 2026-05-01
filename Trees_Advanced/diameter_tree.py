class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if not root:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    ld = diameter(root.left)
    rd = diameter(root.right)

    return max(lh + rh + 1, max(ld, rd))