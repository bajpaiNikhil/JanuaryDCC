class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l = []
def postOrderTraversal(root):

    if root is None:
        return []
    else:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        l.append(root.val)
    return l



root = Treenode(1)
root.right = Treenode(2)
root.right.left = Treenode(3)

print(postOrderTraversal(root))