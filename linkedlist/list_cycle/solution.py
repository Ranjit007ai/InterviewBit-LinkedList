# Given a linked list, return the node where the cycle begins .
# If there is no cycle, return None.

class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


def detect_cycle(head):
    slow = head
    fast = head
    if head == None or head.next == None :
        return None
    while slow != None and fast != None and fast.next != None :
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            break
    if slow != fast :
        return None
    else:
        slow = head
        while slow != fast :
            slow = slow.next
            fast = fast.next
        return slow

start_node = detect_cycle(node1)
if start_node!= None:
    print(start_node.data)
else:
    print('The linked list is not Cycle')