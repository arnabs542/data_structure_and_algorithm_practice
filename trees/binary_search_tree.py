from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def in_order_traversal(self):
        self.in_order_traversal_rec(self.root)

    def in_order_traversal_rec(self, node):
        if node != None:
            self.in_order_traversal_rec(node.left)
            print(node.data, end=" ")
            self.in_order_traversal_rec(node.right)

    def insert(self, current_node, val):
        if self.root == None:
            self.root = Node(val)
            return
        elif val < current_node.data and current_node.left: # can still go farther
            self.insert(current_node.left, val)
            return
        elif val > current_node.data and current_node.right:
            self.insert(current_node.right, val)
            return

        new_node = Node(val)
        if val <= current_node.data:
            current_node.left = new_node
        else:
            current_node.right = new_node


bt = BinarySearchTree() # actually this is just a binary tree not a BST, but whatevs
bt.root = Node(20)
bt.root.left = Node(10)
bt.root.left.right = Node(17)
bt.insert(bt.root, 15)
bt.in_order_traversal()
