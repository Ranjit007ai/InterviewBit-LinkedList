# Given a linked list ,sort it by using insertion sort.
class node :
    def __init__(self,data):
        self.data = data
        self.next = None
    
node1 = node(2)
node2 = node(15)
node3 = node(5)
node4 = node(7)
node5 = node(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def insertion_sort(head,new_node):
    if head == None or head.data >= new_node.data :
        new_node.next = head
        head = new_node
    else:
        cur = head
        while cur.next != None and cur.next.data < new_node.data :
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node
    return head

def sorting_linkedlist(Head):
    sorted_head = None 
    cur = Head
    while cur != None :
        next_node = cur.next 
        sorted_head = insertion_sort(sorted_head,cur)
        cur = next_node
    Head = sorted_head
    return Head

# test case

sort_head = sorting_linkedlist(node1)
while sort_head != None :
    print(sort_head.data,end=' ')
    sort_head = sort_head.next

