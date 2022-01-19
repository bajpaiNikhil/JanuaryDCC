class TreeNode:
    def __init__(self, val =  0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right =  right

def lowestCommonAncestorBst(root, p ,q):
    if root is None:
        return
    # while root is not None:
    #     if p.val < root.val > q.val:
    #         root= root.left
    #     elif p.val > root.val < q.val :
    #         root =root.right
    #     else:
    #         return root.val
    else:
        if p.val <root.val > q.val:
            return lowestCommonAncestorBst(root.left , p ,q)
        if p.val > root.val < q.val:
            return lowestCommonAncestorBst(root.right, p ,q)
        return root.val

root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = TreeNode(2)
q = TreeNode(4)

print(lowestCommonAncestorBst(root, p, q))