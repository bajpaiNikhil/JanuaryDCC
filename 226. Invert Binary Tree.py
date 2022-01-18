

class TreeNode:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

def invert(root):
    if root is None :
        return

    left = invert(root.left)
    right = invert(root.right)

    root.right = left
    root.left = right

    return root

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(invert(root))