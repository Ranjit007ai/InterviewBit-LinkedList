# Given two sorted linked list, we have to merge them such that new linkedlist is also sorted .

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#First  linkedlist
node1_1 = Node(1)
node1_2 = Node(4)
node1_3 = Node(12)
node1_4 = Node(14)

node1_1.next = node1_2
node1_2.next = node1_3
node1_3.next = node1_4

#First linkedlist
node2_1 = Node(5)
node2_2 = Node(7)
node2_3 = Node(24)


node2_1.next = node2_2
node2_2.next =node2_3



def merge_linked_list(Head1,Head2):
    temp_node = Node(0) # creating temp_node for the new linked list 
    ptr = temp_node

    while True:
        if Head1 == None and Head2 == None:     # if both the linkedlist are ended 
            break
        elif Head1 == None :    # if first linkedlist is ended
            ptr.next = Head2
            break
        elif Head2 == None :    # if the second linkedlist is empty
            ptr.next = Head1
            break
        elif Head1.data < Head2.data :
            value = Head1.data
            Head1 = Head1.next
        elif Head2.data < Head1.data: 
            value = Head2.data
            Head2 = Head2.next
        # creating a new node to store the 'value' in the the new linked list
        new_node = Node(value)
        ptr.next = new_node
        ptr = ptr.next


    return temp_node.next


# testcase
head1 = node1_1
head2 = node2_1
new_head = merge_linked_list(head1,head2)
while new_head != None :
    print(new_head.data,end=' ')
    new_head = new_head.next
