class Node:
    def __init__(self , val = 0 , next = None):
        self.val = val
        self.next = None

def removeValue(root , target):
    if not root:
        return []

    head = root

    while root:
        if head.val  == target:
            head.next = root.next








root = Node(1)
root.next = Node(2)
root.next.next = Node(6)
root.next.next.next = Node(3)
root.next.next.next.next = Node(4)
root.next.next.next.next.next = Node(5)
root.next.next.next.next.next.next = Node(6)

print(removeValue(root, target=6))
