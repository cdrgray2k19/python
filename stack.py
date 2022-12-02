class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self) -> None:
        self.top = None

    def push(self, value) -> None:
        if not self.top:
            self.top = StackNode(value)
        else:
            t = StackNode(value)
            t.next = self.top
            self.top = t

    def peek(self):
        if not self.top:
            return False
        return self.top

    def pop(self):
        if not self.top:
            return False
        t = self.top
        self.top = self.top.next
        return t

    def isEmpty(self):
        return not self.top

