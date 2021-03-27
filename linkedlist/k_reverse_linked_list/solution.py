# given linked list , integer k ,reverse node of list k at a time and return modified linked list.
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 =node(1)
node2 =node(2)
node3 =node(3)
node4 =node(4)
node5 =node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def reverse(head,k):
    cur = head
    prev = None
    count = 0
    # reverse first k node of linked list
    while cur is not None and count < k :
        next_node = cur.next 
        cur.next = prev
        prev = cur
        cur = next_node
        count += 1
    if next_node is not None :
        head.next = reverse(next_node,k)
    return prev

# test case
h = reverse(node1,2)
while h != None:
    print(h.data,end=' ')
    h = h.next
