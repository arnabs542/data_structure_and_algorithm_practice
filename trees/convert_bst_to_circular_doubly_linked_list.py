class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self, val):
        self.head = None
        self.current = None

    def in_order(self, node):
        if node == None:
            return

        self.in_order(node.left)

        if self.head == None:
            self.head = node
        else:
            self.current.right = node
            self.node.left = self.current

        self.current = node

        self.in_order(node.right)

        self.in_order(self.root)

    def convert(self, root):
        """
        Parameters
        ----------
        root: Node
            The root node

        Returns
        -------
        Node:
            The head
        """
        self.in_order(root)
        self.head.left= self.head
        return self.head

