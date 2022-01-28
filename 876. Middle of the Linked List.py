
class Node:
    def __init__(self , val = 0 , next  = None):
        self.val = val
        self.next = next


def middleLinkedList(root):
    first = root
    second = root
    while second and second.next is not None:
        first = first.next
        second = second.next.next
    return first.val


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next =Node(4)
head.next.next.next.next  = Node(5)

print(middleLinkedList(head))
