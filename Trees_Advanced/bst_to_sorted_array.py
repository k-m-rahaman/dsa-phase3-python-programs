def inorder(root, res):
    if not root:
        return

    inorder(root.left, res)
    res.append(root.data)
    inorder(root.right, res)


def bstToArray(root):
    res = []
    inorder(root, res)
    return res