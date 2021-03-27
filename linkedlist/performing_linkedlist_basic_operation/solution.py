# In this program we are going to create a simple node ,and a linklist and perform some basic operations like insertion,finding length,etc.
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None
    
    def insert(self,new_node): # insert the new node at end of the linklist
        # if there is no node in the linklist yet,then our new_node will be the head(First node )
        if self.head == None :
            self.head = new_node
        # if the linklist is not empty ,then we need to traverse till the last node(Tail) and then insert the new node.
        else:
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
        return self.head
    
    def length(self,Head): # function to return the length of the linklist
        cur_node = Head
        count = 1
        while cur_node.next != None :
            count += 1
            cur_node = cur_node.next
        return count


# main program

# creating multiple node object
node1 = Node(5)
node2 = Node(7)
node3 = Node(7)

# creating a object for the linklist class
l1 = Linklist()

# inserting node1 in the linklist

new_head = l1.insert(node1)
print('linked list after inserting',node1.data)
while new_head != None :
    if new_head.next == None :
        print(new_head.data,end = '\n')
    else:
        print(new_head.data,end='->')

    new_head = new_head.next


# Now inserting node2 in the list

new_head = l1.insert(node2)
print('linked list after inserting',node2.data)
while new_head != None :
    if new_head.next == None :
        print(new_head.data,end = '\n')
    else:
        print(new_head.data,end='->')
    new_head = new_head.next

# Now inserting node3 in the list
new_head = l1.insert(node3)
print('linked list after inserting',node3.data)
while new_head != None :
    if new_head.next == None :
        print(new_head.data,end = '\n')
    else:
        print(new_head.data,end='->')
    new_head = new_head.next

# Now find the length of the linklist
length_of_linkist = l1.length(node1)
print('The length of the link list is ',length_of_linkist)
