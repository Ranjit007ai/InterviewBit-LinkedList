# given two linklist , we need to find that node such that both linklist merge at that point.
# 1 -> 2 ->3 
#            \
#             4 -> 5 ->6            * 4 is the merge point of both linked list
#            /
# 10->11->12

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,new_node):
        if self.head == None :
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next != None :
                cur_node = cur_node.next
            cur_node.next = new_node
        
# creating multiple nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
temp1 = [node1,node2,node3,node4,node5,node6]
# creating the first linkedlist
l1 = Linkedlist()
# inserting all nodes in the linklist 1
for i in temp1:
    l1.insert(i)

# creating the second linkedlist
l2 = Linkedlist()
# inserting all nodes in the linklist2


node2_1 = Node(11)
node2_2 = Node(12)
temp2 = [node2_1,node2_2,node4]
for i in temp2:
    l2.insert(i)


# defining the function ,to return the merge point 


# This approach takes the time complexity of O( m * n ),if m is the size of linkedlist1 and n is the size of linkedlist2

def merge_point(head1,head2):
    # head1 is the head of the first linklist
    # head2 is the head of the second linklist

    curr_node_2 = head2 # the current node of linklist 2 

    while curr_node_2.next != None :
        curr_node_1 = head1

        while curr_node_1.next != None :
            if curr_node_1.next == curr_node_2.next:
                return curr_node_1.next.data
            curr_node_1 = curr_node_1.next

        curr_node_2 = curr_node_2.next
    return False

# test case
head1 = node1
head2 = node2_1
merging_point = merge_point(head1,head2)
print(merging_point)
