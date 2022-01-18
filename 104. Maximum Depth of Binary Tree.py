class Treenode:
    def __init__(self ,  val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    return 0 if root is None else 1+(max(height(root.right) , height(root.left)))

root = Treenode(3)
root.left = Treenode(9)
root.right = Treenode(20)
root.right.left = Treenode(15)
root.right.right = Treenode(7)

print(height(root))