# Given a sorted linkedlist  , we need to delete all duplicate value node ,such that each element appear only once.
# ex -> 1->1->2 => 1->2
class node :
    def __init__(self,data):
        self.data = data
        self.next = None
    
node1 = node(1)
node2 = node(1)
node3 = node(2)
node4 = node(2)

node1.next = node2
node2.next = node3
node3.next = node4


def deleteduplicates(A):
    if A.next == None :
        return A 
    start_node = A 
    while True :
        if start_node.next == None :
            return A 
        end_node = start_node.next
        while start_node.data == end_node.data :
            if end_node.next == None :
                end_node = end_node.next
                break
            end_node = end_node.next
        if end_node == None:
            start_node.next = None
            return A 
        else:
            start_node.next = end_node
            start_node = end_node
    
# test case
head = deleteduplicates(node1)
while head != None :
    print(head.data,end=' ')
    head = head.next  