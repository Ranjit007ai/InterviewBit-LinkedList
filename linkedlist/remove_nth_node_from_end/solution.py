# Given a linked list ,remove the nth node from the end of the list ,return its head.
# If the 'n' is greater then length of the list ,delete first node of list.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(11)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def length(head):
    cur = head
    count = 1
    while cur != None :
        cur = cur.next
        count += 1
    return count

def remove_nth_node_from_end(head,n):
    l = length(head)
    if l <= n :
        head = head.next
    else:
        i = head
        j = head
        for k in range(0,n-1):
            j = j.next
        while j.next.next != None:
            i = i.next
            j = j.next
        i.next = i.next.next
    return head

# test case
new_head = remove_nth_node_from_end(node1,2)
while new_head != None :
    print(new_head.data,end=' ')
    new_head = new_head.next
