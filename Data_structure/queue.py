"""
    Source code from Computer Science Bootcamp
"""


class Queue:
    def __init__(self):
        self._container = []

    def enqueue(self, data):
        self._container.append(data)

    def dequeue(self):
        return self._container.pop(0)

    def empty(self):
        if not self._container:
            return True
        else:
            return False

    def peek(self):
        return self._container[0]
