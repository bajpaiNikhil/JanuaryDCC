class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l = []

def inorderTraversal(root):
    if root is None:
        return []
    else:
        inorderTraversal(root.left)
        l.append(root.val)
        inorderTraversal(root.right)
    return l
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorderTraversal(root))