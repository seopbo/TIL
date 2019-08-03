"""
    Source code from Computer Science Bootcamp
"""


class TreeNode:
    def __init__(self):
        self._data = None
        self._left = None
        self._right = None

    def __del__(self):
        print('TreeNode of {} is deleted'.format(self._data))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def get_root(self):
        return self._root

    def set_root(self, node):
        self._root = node

    def make_node(self):
        new_node = TreeNode()
        return new_node

    def get_node_data(self, node):
        return node.data

    def set_node_data(self, node, data):
        node.data = data

    def get_left_subtree(self, node):
        return node.left

    def get_right_subtree(self, node):
        return node.right

    def make_right_subtree(self, node, right):
        node.right = right

    def make_left_subtree(self, node, left):
        node.left = left

    def preorder_traverse(self, node, func=None):
        if not node:
            return

        if func:
            func(node.data)
        else:
            print(node.data)

        self.preorder_traverse(node.left, func)
        self.preorder_traverse(node.right, func)

    def inorder_traverse(self, node, func=None):
        if not node:
            return

        self.inorder_traverse(node.left, func)

        if func:
            func(node.data)
        else:
            print(node.data)

        self.inorder_traverse(node.right, func)

    def postorder_traverse(self, node, func=None):
        if not node:
            return

        self.postorder_traverse(node.left, func)
        self.postorder_traverse(node.right, func)

        if func:
            func(node.data)
        else:
            print(node.data)


if __name__ == '__main__':
    bt = BinaryTree()
    list_of_nodes = [bt.make_node() for _ in range(7)]

    for idx, node in enumerate(list_of_nodes, start=1):
        bt.set_node_data(node, idx)
    else:
        n1, n2, n3, n4, n5, n6, n7 = list_of_nodes
        bt.set_root(n1)
        bt.make_left_subtree(n1, n2)
        bt.make_right_subtree(n1, n3)
        bt.make_left_subtree(n2, n4)
        bt.make_right_subtree(n2, n5)
        bt.make_left_subtree(n3, n6)
        bt.make_right_subtree(n3, n7)

        # preorder traversal (node -> left subtree -> right subtree)
        bt.preorder_traverse(n1)
        # inorder traversal (left subtree -> node -> right subtree)
        bt.inorder_traverse(n1)
        # postorder traversal (left subtree -> right subtree -> node)
        bt.postorder_traverse(n1)
