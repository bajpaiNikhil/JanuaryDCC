class Node:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val



def mergeTwoList(root , root1):

    if not root or not root1:
        return  root or root1

    if root.val <root1.val :
        root.next  = mergeTwoList(root.next , root1)
        return root
    else:
        root1.next = mergeTwoList(root , root1.next)
        return root1
root = Node(1)
root.next = Node(2)
root.next.next = Node(4)

root1 = Node(1)
root1.next = Node(3)
root1.next.next = Node(4)


print(mergeTwoList(root, root1))