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

l = linkedList()
l.insert_at_start(1)
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
print(l.fib())