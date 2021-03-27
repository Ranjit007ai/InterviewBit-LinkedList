# Given a list,rotate list to right by k places, where k is non - negative.
# ex : 1->2->3->4->5->NULL , k =2 => 4->5->1->2->3->NULL
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)


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


def rotate_right(head,k):
    l = length(head)
    k = k % l 
    if k == 0:
        return head
    cur = head
    temp = l - k 
    count = 1
    while cur != None and count < temp :
        cur = cur.next
        count += 1
    if cur == None :
        return head
    k_node = cur
    while cur.next != None:
        cur = cur.next
    cur.next = head
    head = k_node.next
    k_node.next = None 
    return head


# test case
head_after_rotation = rotate_right(node1,2)
while head_after_rotation != None:
    print(head_after_rotation.data,end=' ')
    head_after_rotation = head_after_rotation.next
