class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def lca(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)

    if left and right:
        return root

    return left if left else right


# Driver
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("LCA:", lca(root, 2, 3).data)