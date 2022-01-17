

class Node:
    def __init__(self , val = 0 , next = None):
        self.val =  val
        self.next = next

def reverseLL(root):

    return reverse(root)
def reverse(root , prev = None):
    if not root:
        return prev
    n = root.next
    root.next = prev
    return reverse(n , prev)


root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next = Node(4)
root.next.next.next.next = Node(5)


print(reverseLL(root))