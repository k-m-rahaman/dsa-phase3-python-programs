def printLeft(root, res):
    if root:
        if root.left:
            res.append(root.data)
            printLeft(root.left, res)

def printLeaves(root, res):
    if root:
        printLeaves(root.left, res)
        if not root.left and not root.right:
            res.append(root.data)
        printLeaves(root.right, res)

def printRight(root, res):
    if root:
        if root.right:
            printRight(root.right, res)
            res.append(root.data)

def boundary(root):
    res = []
    if not root:
        return res

    res.append(root.data)
    printLeft(root.left, res)
    printLeaves(root, res)
    printRight(root.right, res)

    return res