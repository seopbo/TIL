class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        else:
            print("Stack is empty.")

    def size(self):
        return len(self._items)

    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        else:
            print("Stack is empty.")

    def __repr__(self):
        return repr(self._items)
