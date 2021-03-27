# given a linked list, swap every 2 adjacent node and return head

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

def pairwiseswap(head):
    temp = head
    if temp is None :
        return head
    while temp is not None and temp.next is not None :
        if temp.data == temp.next.data:
            temp = temp.next.next
        else:
            temp.data,temp.next.data = temp.next.data,temp.data
            temp = temp.next.next
    return head

h = pairwiseswap(node1)
while h != None :
    print(h.data,end=' ')
    h = h.next
