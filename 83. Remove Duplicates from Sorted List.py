class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeDuplicates(node):

    head = node

    while head is not None and head.next is not None:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return node.next.val


node = Node(1)
node.next = Node(1)
node.next.next = Node(2)
node.next.next.next = Node(3)
node.next.next.next.next = Node(3)

print(removeDuplicates(node))
