class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, None, self.head)
        if self.head is not None:
            self.head.prev = node
        
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, itr, None)

    def remove(self, node):
        if node == self.head:
            node.next = self.head
            self.head.prev = None
        else:
            node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
        return node

    def print_forward(self):
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

    def print_backward(self):
        if self.head is None:
            print('linked list is empty')
            return
        
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        llstr = ''

        while itr:
            llstr += str(itr.data)
            if itr.prev is not None:
                llstr += '<--'
            itr = itr.prev

        print(llstr)

ll = linkedlist()
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_end(3)
ll.print_forward()
ll.print_backward()

#could implement all previous methods form single linked lists code just need to change attributes of nodes.