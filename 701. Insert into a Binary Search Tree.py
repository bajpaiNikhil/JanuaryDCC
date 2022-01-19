class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertBst(root, node):
    if root is None:
        return node
    else:
        if node.val > root.val:
            root.right =  insertBst(root.right, node)
        elif node.val < root.val:
            root.left =  insertBst(root.left, node)
        else:
            root = node

    h = inorder(root , [])
    print(h , "1")
    return root

def inorder(root, l):
    if root is None:
        return
    else:
        inorder( root.left , l)
        l.append(root.val)
        inorder(root.right , l)
    return l

root = TreeNode(4)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(1)
root.right = TreeNode(7)

node = TreeNode(5)

print(insertBst(root, node))
