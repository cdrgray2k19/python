from os import link


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class linkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_start(self, value) -> None:
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
    def insert_at_end(self, value) -> None:
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def __str__(self) -> None:
        current = self.head
        s = ''
        while current:
            s += str(current.data)
            if current.next:
                s += '->'
            current = current.next
        return s

    def sum(self) -> None:
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total

    def min(self) -> None:
        if not self.head:
            return 'empty'
        min = self.head.data
        current = self.head
        while current:
            if current.data < min:
                min = current.data
            current = current.next
        return min

    def max(self) -> None:
        if not self.head:
            return 'empty'
        max = self.head.data
        current = self.head
        while current:
            if current.data > max:
                max = current.data
            current = current.next
        return max

    def reverse(self) -> None:
        current = self.head
        prev = None
        while current.next:
            next = current.next
            current.next = prev
            prev = current
            current = next
        current.next = prev
        self.head = current

    def fib(self) -> None:
        current = self.head
        while current.next.next:
            if current.data + current.next.data != current.next.next.data:
                return False
            current = current.next
        return True

def partition(head, value) -> Node:
    '''partitions the list around a value, splitting list into left side and right side, left side contains nodes with data smaller than specified value, right side contains all other nodes'''
    firstLeft = None
    lastLeft = None
    firstRight = None
    lastRight = None

    current = head

    while current != None:
        if current.data < value:
            if not firstLeft:
                firstLeft = current
            else:
                lastLeft.next = current
            lastLeft = current
        else:
            if not firstRight:
                firstRight = current

            else:
                lastRight.next = current

            lastRight = current

        current = current.next

    if lastRight:
        lastRight.next = None
    if firstLeft:
        lastLeft.next = firstRight
        return firstLeft

    return firstRight



def sum(first, second) -> Node:
    '''returns the sum of the two reversed linkedlists passed as if they were passed as integers, returns the sum as a reversed linkedlist'''
    node1 = first.head
    node2 = second.head

    carry = 0
    res = linkedList()
    current = None
    while node1 or node2:
        num = carry
        carry = 0
        if node1:
            num += node1.data
            node1 = node1.next
        if node2:
            num += node2.data
            node2 = node2.next
        if num >= 10:
            carry = 1
            num -= 10
        if not current:
            current = Node(num)
            res.head = current
        else:
            current.next = Node(num)
            current = current.next
    
    if carry != 0:
        current.next = Node(carry)
    return res
        


l1 = linkedList()
l2 = linkedList()

l1.insert_at_end(9)
l1.insert_at_end(9)
l1.insert_at_end(9)

l2.insert_at_end(9)
l2.insert_at_end(9)
l2.insert_at_end(9)

h = sum(l1, l2)
print(h)
"""l.insert_at_start(1)
l.insert_at_start(2)
l.insert_at_start(3)
l.insert_at_start(5)
l.insert_at_start(8)
l.insert_at_start(13)
l.insert_at_start(21)
l.insert_at_start(34)
print(l)
l.reverse()
print(l)
print(l.fib())"""
"""l.insert_at_start(3)
l.insert_at_start(5)
l.insert_at_start(8)
l.insert_at_start(5)
l.insert_at_start(10)
l.insert_at_start(2)
l.insert_at_start(1)
l.reverse()
print(l)

l.head = partition(l.head, 5)
print(l)"""