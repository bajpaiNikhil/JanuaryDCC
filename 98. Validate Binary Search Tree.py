class TreeNode:
    def __init__(self , val = 0 , left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def checkBst(root):
    if root is None:
        return
    k = inorder(root , [])
    return all(x<y for x,y in zip(k , k[1:]))

def inorder(root , l):
    if root is None:
        return
    else:
        inorder(root.left ,l)
        l.append(root.val)
        inorder(root.right , l)
    return l



root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)

print(checkBst(root))