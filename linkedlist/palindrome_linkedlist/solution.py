# Given a linked list ,we need to return Boolean value (True) if the linked list is Palindrom , False if not.
# Approach is quite simple , we are going to divide the linked list into half part each.
# Then we are going to reverse the right part of the linked list 
# Then compare the left part and reversed right part ,if both are same then it means they are palindrome.
# Else they are not palindrome.
        #ex = 1->2->3->2->1
#  left_part<-|--|  |  |--| ->right_part
#                  mid
# After Reversing the rightPart
#             1->2->3->1->2
# Now the left part (1->2) and right part (1->2) , hence they are palindrome.

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None 

node1 = Node(1)
node2 = Node(1)
node3 = Node(1)
node4 = Node(2)
node5 = Node(2)
node6 = Node(1)
node7 = Node(1)
node8 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next= node5
node5.next = node6
node6.next = node7
node7.next = node8
def length(Head): # function return the length of linkedlist
    cur = Head
    count = 1 
    while cur != None :
        cur = cur.next
        count += 1
    return count

def find_mid_node(mid_pos,head): # function return the mid node of the linked list
    cur_node = head
    count = 1
    while count < mid_pos :
        cur_node = cur_node.next
        count += 1
    return cur_node

def reverse(right_part_head): # function return the head after Reversing the linkedlist
    curr = right_part_head
    prev = None
    while curr != None :
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    right_part_head = prev
    return right_part_head

def ispalindrome(head): # function return boolean value whether the ispalindrome is True or False.
    length_of_linklist = length(head)
    mid_pos = ( length_of_linklist + 1 ) // 2
    mid_node = find_mid_node(mid_pos,head)
    if length_of_linklist % 2 == 0: # if the length of the linkedlist is even
        left_end = mid_node.next
        right_start = mid_node.next
    else:   # if the length of the linkedlist is odd
        left_end = mid_node
        right_start = mid_node.next
    
    # reversing the right_part of the linkedlist
    right_start = reverse(right_start)
    # Now comparing the left part and the right part of the linked list
    while head != left_end and right_start != None :
        if head.data == right_start.data :  # if both the node has same value
            head = head.next
            right_start = right_start.next
        else:
            return False
    return True


# testcase
ans = ispalindrome(node1)
print(ans)
        