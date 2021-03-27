# Given a sorted linkedlist ,delete all the element which are occurence more than once, and leaving those element which occured once.
#ex: 1->1->1->2->3  = > 2->3
class node :
    def __init__(self,data):
        self.data =data
        self.next = None

node1 = node(1)
node2 = node(1)
node3 = node(2)
node4 = node(3)

node1.next = node2
node2.next = node3
node3.next = node4

def remove_all_duplicates(header):
    curr = header
    head = prev = node(None)
    head.next = curr

    while curr and curr.next :
        if curr.data == curr.next.data :
            while curr and curr.next and curr.data == curr.next.data:
                curr = curr.next
            curr = curr.next
            prev.next = curr
        else:
            prev = prev.next
            curr = curr.next
    return head.next

# test case
head = remove_all_duplicates(node1)
while head != None :
    print(head.data,end = ' ')
    head = head.next