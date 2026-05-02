def height(root):
    if not root:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    if lh == -1 or rh == -1 or abs(lh - rh) > 1:
        return -1

    return 1 + max(lh, rh)

def isBalanced(root):
    return height(root) != -1