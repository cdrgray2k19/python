class QueueNode:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

class Queue:

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def add(self, value):
        if not self.first:
            self.first = QueueNode(value)
            self.last = self.first
        else:
            t = QueueNode(value)
            self.last.next = t
            self.last = t

    def peek(self):
        if not self.first:
            return False
        return self.first

    def remove(self):
        if not self.first:
            return False
        t = self.first
        self.first = self.first.next
        return t

    def isEmpty(self):
        return not self.first