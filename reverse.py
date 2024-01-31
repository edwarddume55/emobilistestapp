def reverse_Llist(Llist):  
    if Llist.head == Node:  
        return None  
  
    previous = None  
    current = Llist.head  
    after = current.next   
  
    while current:  
        # Reverse the link  
        current.next = previous  
        # Moving previous element to one ahead  
        previous = current  
        # Moving current one element ahead  
        current = after  
        # Moving one element ahead  
        if after:  
            after = after.next  
  
    Llist.head = previous  
  
n = LinkedList()  
n.head = Node(1)  
n1 = Node(2)  
n.head.next = n1  
n2 = Node(3)  
n1.next = n2  
n3 = Node(4)  
n2.next = n3  
print("The reverse linked list is: ")  
reverse_Llist(n)  
n.print_list()  