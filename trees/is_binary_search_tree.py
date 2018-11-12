from trees.binary_search_tree import BinarySearchTree, Node

# Given the root node of a binary search tree, determine if the tree is a valid binary search tree
#
# For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:
#     The  value of every node in a node's left subtree is less than the data value of that node.
#     The  value of every node in a node's right subtree is greater than the data value of that node.
#     The  value of every node is distinct.

def checkBST(root):
    return checkBST_rec(root)

def checkBST_rec(node, parent_max=None, parent_min=None):
    left = right = False

    if node.left == None and node.right == None:
        return True

    if node.left:
        if node.left.data < node.data and (parent_max == None or node.left.data < parent_max ):
            parent_max = node.data
            left = checkBST_rec(node.left, parent_max, parent_min)
    if node.right:
        if node.right.data > node.data and (parent_min == None or node.right.data > parent_min):
            parent_min = node.data
            right = checkBST_rec(node.right, parent_max, parent_min)

    if left and right:
        return True
    return False

def is_bst(root, last=float('-inf')):
    if root != None:
        if root.left:
            return is_bst(root.left, last)
        if last < root.data:
            last = root.data
        else:
            return False
        if root.right:
            return is_bst(root.right, last)
        return True

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(str(is_bst(tree.root)))

# tree = BinarySearchTree()
# tree.create(8)
# tree.root.left = Node(6)
# tree.root.left.left = Node(3)
# tree.root.left.right = Node(7)
# tree.root.left.left.left = Node(1)
# tree.root.left.left.right = Node(5)
# tree.root.left.left.right.left = Node(4)
#
# print(str(checkBST(tree.root)))


tree = BinarySearchTree()
tree.create(1)
tree.root.right = Node(2)
tree.root.right.right = Node(4)
tree.root.right.right.right = Node(3)
tree.root.right.right.right.right = Node(5)
tree.root.right.right.right.right.right = Node(6)
tree.root.right.right.right.right.right.right = Node(7)


print(str(is_bst(tree.root)))


# tree = BinarySearchTree()
# tree.create(8)
# tree.root.left = Node(6)
# tree.root.left.left = Node(3)
# tree.root.left.right = Node(7)
# tree.root.left.left.left = Node(1)
# tree.root.left.left.right = Node(7)
# tree.root.left.left.right.left = Node(4)

print(str(is_bst(tree.root)))

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

print(str(is_bst(tree.root)))

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
