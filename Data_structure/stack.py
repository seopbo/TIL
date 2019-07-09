class Stack:
    def __init__(self):
        self._container = []

    def push(self, data):
        self._container.append(data)

    def pop(self):
        return self._container.pop()

    def empty(self):
        if not self._container:
            return True
        else:
            return False

    def peek(self):
        return self._container[-1]
