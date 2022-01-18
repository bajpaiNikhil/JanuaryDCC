class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def checkSymmetric(root):
    if root is None:
        return True
    else:
        return symmetric(root.left, root.right)


def symmetric(leftL, rightR):

    if leftL is None or rightR is None:
        return leftL == rightR

    if leftL.val != rightR.val:
        return False

    else:
        return symmetric(leftL.left, rightR.right) and symmetric(leftL.right, rightR.left)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(3)
print(checkSymmetric(root))