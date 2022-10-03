#a singularly linked list is an dynamic data structure which allows each data value (node) to be linked to the one after it
#this has several advantages in terms of memory and speed efficiency of storing and retreiving data

class Node:
    
    #allows us to track each data value.
    #allows us to referene each node by the previous one using self.next
    #allows us to retreive the data value stored within each node using self.data
    def __init__(self, data, next):
        self.data = data
        self.next = next

class linkedlist: 

    #linked list is the data structure where we will be keeping nodes
    def __init__(self):
        #gives us the beginning of our linked list which will be very useful later on
        self.head = None

    def insert_at_beginning(self, data):
        #insert nodes at the beginning of our node
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        #prints the linked list with all our nodes inside of it
        if self.head is None:
            print('linked list is empty')
            return
    
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)
            if itr.next is not None:
                llstr += '-->'
            itr = itr.next
    
        print(llstr)

    def insert_at_end(self, data):
        #allows us to insert a node at the end of the linked list
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        #allows us to insert numerous values at the end of the linked list
        for data in data_list:
            self.insert_at_end(data)
    
    def get_len(self):
        #returns length of the linked list depending on how many nodes it contains
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def remove_at_index(self, index):
        #removes a node at the index referenced
        #index starts at 0
        if index < 0 or index >= self.get_len():
            print('index not valid')
            return   
        if index == 0:
            self.head = self.head.next
            return 
        count = 0
        itr = self.head
       
        while count < index - 1:
            count += 1
            itr = itr.next
       
        itr.next = itr.next.next
    
    def insert_at_index(self, index, data):
        #inserts a node at the index referenced
        if index < 0 or index >= self.get_len():
            print('index not valid')
            return
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        
        while count < index - 1:
            count += 1
            itr = itr.next
        node = Node(data, itr.next)
        itr.next = node

    def insert_after_value(self, value, data):
        #inserts a node directly after a certain value
        
        itr = self.head

        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next
        
        print('no such value in linked list')

    def remove_by_value(self, value):
        #removes a node according to its value
        itr = self.head
        count = 0 
        while itr:
            if itr.data == value:
                self.remove_at_index(count)
                return
            itr = itr.next
            count += 1

        print('no such value in linked list')






#here we will make a linked list and call the functions we have just made
ll = linkedlist()
ll.insert_at_beginning(1)
ll.print()
ll.insert_at_end(2)
ll.print()
ll.insert_values([3,4,5])
ll.print()
ll.remove_at_index(2)
ll.print()
ll.insert_at_index(2,3)
ll.print()
ll.insert_after_value(5,6)
ll.print()
ll.remove_by_value(6)
length = ll.get_len()
print('length of list =', length)