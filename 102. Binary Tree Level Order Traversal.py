class Treenode:
    def __init__(self ,  val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderTraversal(root) :

    b = []
    h = height(root)
    for i in range(1 , h+1):
        b.append(traversal(root , i , []))
    return b


def height(root):
    if root is None:
        return 0
    else:
        lHeight = height(root.left)
        rHeight = height(root.right)
        if lHeight > rHeight:
            return 1+lHeight
        else:
            return 1+rHeight

def traversal(root , level , l ):

    if root is None:
        return
    if level == 1:
        l.append(root.val)
    elif level>1 :
        traversal(root.left ,level-1 , l)
        traversal(root.right , level-1 , l)
    return l



root = Treenode(3)
root.left = Treenode(9)
# root.right = Treenode(20)
# root.right.left = Treenode(15)
# root.right.right = Treenode(7)

print(levelOrderTraversal(root))