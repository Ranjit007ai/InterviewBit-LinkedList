# Reverse the linked list from position m to n ,Do it in place and in one pass.
class node :
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

def reverse(head):
    cur = head
    prev = None
    while cur != None :
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev

def reverse_between(head,m,n):
    if m == n :
        return head
    rev_prev = None
    rev_s = None
    rev_e = None 
    rev_next = None
    count = 1
    cur = head

    while cur != None and count <= n:
        if count < m: rev_prev = cur
        if count == m: rev_s = cur
        if count == n:
            rev_e = cur
            rev_next = cur.next 
    rev_e.next = None
    new_head = reverse(res_s)
    if m == 1:
        head = new_head
    else:
        rev_prev.next = new_head
    rev_s.next = rev_next
    return head 

# test case
new_head = reverse_between(node1,2,4)
while new_head != None:
    print(new_head.data)
    new_head = new_head.next
