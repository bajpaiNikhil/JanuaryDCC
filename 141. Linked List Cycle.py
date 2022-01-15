
class Node:
    def __init__(self , value = 0 ,next=None):
        self.next = next
        self.value = value


def findCycleInLl1(root):
    slow = root
    fast = root.next

    while slow is not fast:
        slow = slow.next
        fast = fast.next.next
        return False

    return True


def findCycleInLl2(root):
    slow = root
    fast = root

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    else:
        return False


node = Node(3)
node.next = Node(2)
node.next.next = Node(0)
node.next.next.next = Node(-4)
node.next.next.next.next = Node(2)

print(findCycleInLl1(node))
print(findCycleInLl2(node))
