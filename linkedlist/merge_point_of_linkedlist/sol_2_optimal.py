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

# defining the function to return the length of the given linkedlist
def length(head):
    cur = head
    count = 1
    while cur.next != None :
        cur = cur.next
        count += 1
    return count
#  defining the function to return the merging point of both linkedlist
def merge_point(head1,head2):

    # finding the length of both the linked list

    length_1 = length(head1) # length of first linkedlist
    length_2 = length(head2) # length of second linkedlist

    difference = length_1 - length_2
    if length_2 > length_1 : # if second list is greater than first list 
        head1, head2 = head2, head1 # swapping the header
    
    for i in range(0,difference):
        head1 = head1.next

    while head1 != None and head2 != None:
        if head1.next == head2.next :
            return head1.next.data
        head1 = head1.next
        head2 = head2.next
    return False # in case if there is no merging point 

# test case
head1 = node1
head2 = node2_1
merging_point = merge_point(head1,head2)
print(merging_point)