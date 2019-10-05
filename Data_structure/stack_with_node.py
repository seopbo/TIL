class Node:
    def __init__(self, value=None, pointer=None):
        self._value = value
        self._pointer = pointer


class Stack:
    def __init__(self):
        self._head = None
        self._count = 0

    def is_empty(self):
        return not self._count

    def push(self, value):
        self._head = Node(value, self._head)
        self._count += 1

    def pop(self):
        if not self.is_empty() and self._head:
            node = self._head
            self._head = node._pointer
            self._count -= 1
            return node._value
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.is_empty() and self._head:
            return self._head._value
        else:
            print("Stack is empty.")

    def size(self):
        return self._count

    def __repr__(self):
        items = self._print_list()
        return repr(items)

    def _print_list(self):
        items = []

        node = self._head
        while node:
            items.append(node._value)
            node = node._pointer

        items.reverse()

        return items
