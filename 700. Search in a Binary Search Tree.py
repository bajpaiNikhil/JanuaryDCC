class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBst(root, value):
    if root is None:
        return None
    if root.val == value:
        return root
    if value > root.val:
        return searchBst(root.right, value)
    else:
        return searchBst(root.left, value)


root = TreeNode(4)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)
root.right = TreeNode(7)

print(searchBst(root, 2))
