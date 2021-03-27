# Given two number in the form of linked list , add them and return the result in the form of linked list
# ex : (2->4->3) +  (5->6->4) = (7->0->8) = 342+465=807
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

# first linked list
node1_1 = Node(2)
node1_2 =  Node(4)
node1_3 =  Node(3)

node1_1.next = node1_2
node1_2.next = node1_3

# second linked list

node2_1 = Node(5)
node2_2 = Node(6)
node2_3 = Node(4)

node2_1.next = node2_2
node2_2.next = node2_3

def add_two_number(head1,head2):
    temp_head = Node(-1)
    ptr = temp_head
    carry = 0
    while head1 is not None and head2 is not None :
        first_data = 0 if head1 is None else head1.data
        second_data = 0 if head2 is None else head2.data 
        val = carry + first_data + second_data 
        sum_val = val % 10
        carry = val // 10 
        new_node = Node(sum_val)
        ptr.next = new_node
        ptr = ptr.next

        if head1 is not None :
            head1 = head1.next
        if head2 is not None :
            head2 = head2.next
    if carry > 0 :
        new_node = Node(carry)
        ptr.next = new_node
        ptr = ptr.next
    return temp_head.next


# test case
h = add_two_number(node1_1,node2_1)
while h != None :
    print(h.data,end=' ')
    h = h.next
