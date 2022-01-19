class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isLeaf(node):
    return node.left is None and node.right is None


def pathSum(root, target):
    if root is None:
        return

    return allPath(root, [], target)


def allPath(node, l, target):

    if node is None:
        return

    l.append(node.val)

    if isLeaf(node):
        #print(l)
        l+=l
        return l
        # if sum(l) == target:
        #     return True
        # return True
    allPath(node.left, l, target , )
    allPath(node.right, l, target , )
    l.pop()



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

print(pathSum(root, 22))
