class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





def pathSum(root, target):

    if root is None:
        return False

    else:
        if root.left is None and root.right is None and root.val == target:
            return True
        else:
            return pathSum(root.left , target-root.val) or pathSum(root.right , target-root.val)



root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print(pathSum(root, 221))
