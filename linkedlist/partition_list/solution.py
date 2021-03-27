# Given a linked list and value x,partition it such that all nodes less than x comes before nodes greater than or equal to x. 
# You should preserve the original relative order of nodes in each of two partitions.
# ex: 1->4->3->2->5->2 ,x=3
# o/p: 1->2->2->4->3->5

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
node1 = Node(1)
node2 = Node(4)
node3 = Node(3)
node4 = Node(2)
node5 = Node(5)
node6 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


def partition(head,x):
    before_head = before = Node(0)
    after_head = after = Node(0)
    while head != None :
        if head.data < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    before.next = after_head.next
    after.next = None
    return before_head.next


# test case
head = node1
x = 3
new_head = partition(head,x)
while new_head != None :
    print(new_head.data,end=' ')
    new_head = new_head.next
