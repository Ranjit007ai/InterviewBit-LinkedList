# Given a single linked list , we need to reverse it.
# 1 -> 2 -> 3 ->4       ==>>   4 -> 3 -> 2 -> 1

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
    

node1 = Node(5)
node2 = Node(6)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4


def reverse(head):

    prev_node = None 
    curr_node = head

    while curr_node != None :

        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    head = prev_node

    return prev_node


# test case 
head = node1
print('Original linked list before reversing')
while head != None:
    print(head.data,end=' ')
    head = head.next 
head = node1
new_head = reverse(head)
print('\nlinked list after reversing')
while new_head != None:
    print(new_head.data,end=' ')
    new_head = new_head.next 

