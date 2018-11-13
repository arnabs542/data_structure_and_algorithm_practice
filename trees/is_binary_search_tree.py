from trees.binary_search_tree import BinarySearchTree, Node

# Given the root node of a binary search tree, determine if the tree is a valid binary search tree
#
# For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:
#     The  value of every node in a node's left subtree is less than the data value of that node.
#     The  value of every node in a node's right subtree is greater than the data value of that node.
#     The  value of every node is distinct.

def is_subtree_lesser(node, value):
    if node == None:
        return True
    else:
        if node.data < value and is_subtree_lesser(node.left, value) and is_subtree_lesser(node.right, value):
            return True
        else:
            return False

def is_subtree_greater(node, value):
    if node == None:
        return True
    else:
        if node.data > value and is_subtree_greater(node.left, value) and is_subtree_greater(node.right, value):
            return True
        else:
            return False

def checkBST(root):
    if root == None:
        return True
    if is_subtree_lesser(root.left, root.data) and is_subtree_greater(root.right, root.data) and checkBST(root.left) and checkBST(root.right):
        return True
    else:
        return False

def checkBST_better(root, min=float('inf'), max=float('-inf')):
    if root == None:
        return True
    if (root.data < min and root.data > max
            and checkBST_better(root.right, min, root.data)
            and checkBST_better(root.left, root.data, max)):
        return True
    else:
        return False


tree = BinarySearchTree()
tree.create(1)
tree.root.right = Node(2)
tree.root.right.right = Node(3)
tree.root.right.right.right = Node(4)
tree.root.right.right.right.right = Node(5)
tree.root.right.right.right.right.right = Node(6)
tree.root.right.right.right.right.right.right = Node(7)


# print('Should be True: ' + str(checkBST(tree.root)))
print('Should be True: ' + str(checkBST_better(tree.root)))

tree = BinarySearchTree()
tree.create(1)
tree.root.right = Node(2)
tree.root.right.right = Node(4)
tree.root.right.right.right = Node(3)
tree.root.right.right.right.right = Node(5)
tree.root.right.right.right.right.right = Node(6)
tree.root.right.right.right.right.right.right = Node(7)


# print('Should be False: ' + str(checkBST(tree.root)))
print('Should be False: ' + str(checkBST_better(tree.root)))


tree = BinarySearchTree()
tree.create(8)
tree.root.left = Node(6)
tree.root.left.left = Node(3)
tree.root.left.right = Node(7)
tree.root.left.left.left = Node(1)
tree.root.left.left.right = Node(7)
tree.root.left.left.right.left = Node(4)
#         8
#      6
#   3    7
#1   7
#   4
# print('Should be False: ' + str(checkBST(tree.root)))
print('Should be False: ' + str(checkBST_better(tree.root)))

tree = BinarySearchTree()
tree.create(8)
tree.root.left = Node(6)
tree.root.left.left = Node(3)
tree.root.left.right = Node(7)
tree.root.left.left.left = Node(1)
tree.root.left.left.right = Node(4)
tree.root.right = Node(27)
tree.root.right.right = Node(37)
tree.root.right.right.left = Node(4)

#       8
#    6    27
#  3  7     37
#1 4      4

# print('Should be False: ' + str(checkBST(tree.root)))
print('Should be False: ' + str(checkBST_better(tree.root)))

'''
SAMPLE INPUT
6
3 2 4 1 5 6

EXPECTED OUTPUT
True
----------------
SAMPLE INPUT
7
8 6 7 3 1 5 4

EXPECTED OUTPUT
True
'''
