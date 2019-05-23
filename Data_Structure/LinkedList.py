# https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
# https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/

class Node:
    def __init__(self, data: int) -> None:
        self._data = data
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def push(self, data):
        _node = Node(data)
        _node._next = self._head
        self._head = _node

    def insert_after_node(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return

        _node = Node(data)
        _node._next = prev_node._next
        prev_node._next = _node

    def append(self, data):

        if self._head is None:
            self.push(data)
        else:
            footprint = self._head
            while footprint._next:
                footprint = footprint._next

            footprint._next = Node(data)

    def delete_node_with_key(self, key):

        footprint = self._head

        if footprint._data == key:
            self._head = footprint._next
            # footprint = None
            return

        while footprint._next:
            if footprint._next._data == key:
                if footprint._next._next:
                    footprint._next = footprint._next._next
                    break
                else:
                    footprint._next = None
                    break
            else:
                footprint = footprint._next

        # footprint = None

    def delete_node_with_position(self, position):

        footprint = self._head
        node_index = 0

        if node_index == position:
            self._head = footprint._next
            # footprint = None
            return

        while footprint._next:
            if (node_index + 1) == position:
                footprint._next = footprint._next._next
                break
            else:
                node_index += 1
                footprint = footprint._next

        # footprint = None

    def traverse(self):
        footprint = self._head

        while footprint:
            print(footprint._data)
            footprint = footprint._next


li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.traverse()


li.delete_node_with_position(1)
li.traverse()