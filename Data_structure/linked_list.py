class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def empty(self):
        return True if not self._size else False

    def size(self):
        return self._size

    def append(self, data):
        node = Node(data)

        if self.empty():
            self._head = node
            self._tail = node
            self._size += 1
        else:
            self._tail.next = node
            self._tail = node
            self._size += 1

    def search_target(self, target, start=0):
        if self.empty():
            return None

        position = 0
        current = self._head

        if position >= start and target == current.data:
            return current.data, position

        while current.next:
            position += 1
            current = current.next

            if position >= start and target == current.data:
                return current.data, position
        return None, None

    def search_position(self, position):
        if position > self.size() - 1:
            return None

        cnt = 0
        current = self._head
        if cnt == position:
            return current.data

        while cnt < position:
            current = current.next
            cnt += 1
        return current.data

    def remove(self, target):
        if self.empty():
            return None

        before = self._head
        current = self._head

        if target == current.data:
            if self.size() == 1:
                self._head = None
                self._tail = None
            else:
                self._head = self._head.next
            self._size -= 1
            return current.data

        while current.next:
            before = current
            current = current.next
            if target == current.data:

                if current is self._tail:
                    self._tail = before

                before.next = current.next
                self._size -= 1
                return current.data

        return None
