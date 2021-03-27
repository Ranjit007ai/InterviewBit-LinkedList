# given a linked list ,reorder the list such that:
# l0->l1->l2->l3->ln = l0->ln->l1->ln-1....
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 =node(1)
node2 =node(2)
node3 =node(3)
node4 =node(4)
node5 =node(5)

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
    head = prev
    return head

def reorder_list(head):
    if head.next == None :
        return head
    slow = head
    fast = slow.next

    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next
    head1 = head
    head2 = slow.next
    slow.next = None
    head2 = reverse(head2)
    new_node = node(0)
    cur = new_node
    while head1 or head2 :
        if head1:
            cur.next = head1
            cur = cur.next
            head1 = head1.next
        if head2:
            cur.next = head2
            cur = cur.next
            head2 = head2.next

    return new_node.next

h = reorder_list(node1)
while h != None :
    print(h.data,end=' ')
    h = h.next