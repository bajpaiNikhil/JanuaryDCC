
class TreeNode:
    def __init__(self, val = 0, left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

def twoSumBst(root , target):
    if root is None:
        return
    k = inorderBst(root , [])

    left = 0
    right = len(k)-1

    while left<right:
        if k[left]+k[right] >target:
            right-=1
        elif k[left]+k[right] < target:
            left+=1
        else:
            return True
    return False

def inorderBst(root , l):
    if root is None:
        return
    else:
        inorderBst(root.left , l)
        l.append(root.val)
        inorderBst(root.right , l)
    return l


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.right =  TreeNode(4)
root.left.left = TreeNode(2)
root.right.right = TreeNode(7)

print(twoSumBst(root , 1000))