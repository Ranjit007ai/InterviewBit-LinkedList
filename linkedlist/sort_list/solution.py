# Given a linked list ,sort the linked list it O(nlogn) time complexity (Merge sorting)
class node :
    def __init__(self,data):
        self.data = data
        self.next = None 

node1 = node(5)
node2 = node(2)
node3 = node(11)
node4 = node(7)
node5 = node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def merge_sort(header1,header2):
    temp_node = node(-1)
    ptr = temp_node
    while header1 != None and header2 != None :
        if header1.data < header2.data :
            ptr.next = header1
            header1 = header1.next
        else:
            ptr.next = header2
            header2 = header2.next
        ptr = ptr.next
    if header1 != None :
        ptr.next = header1
    if header2 != None :
        ptr.next = header2
    return temp_node.next


def sorting_the_linkedlist(head):
    if head == None and head.next == None :
        return head
    prev_slow = None 
    slow = head
    fast = head
    while fast != None and fast.next != None :
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    prev_slow.next = None 
    return merge_sort(sorting_the_linkedlist(head),sorting_the_linkedlist(slow))

# test case
sorted_head  = sorting_the_linkedlist(node1)
while sorted_head != None :
    print(sorted_head.data)
    sorted_head = sorted_head.next
