from trees.binary_search_tree import BinarySearchTree, Node
'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Example 1:
       1
     /   \
    1     1
  / \    /
 1  1    1

returns true since all nodes are of value 1

Example 2:
       1
     /   \
    1     1
  / \    /
 1  6    1

returns false since one node is a 6 and not a 1
'''

def is_univalued(current, value_it_must_be=None):
    if value_it_must_be == None:
        value_it_must_be = current.data

    if current.data != value_it_must_be:
        return False

    left = True
    right = True
    if current.left:
        left = is_univalued(current.left, value_it_must_be)
    if current.right:
        right = is_univalued(current.right, value_it_must_be)

    return left and right

bt = BinarySearchTree()
bt.root = Node(1)
bt.root.left = Node(1)
bt.root.left.left = Node(1)
bt.root.left.right = Node(1)
bt.root.right = Node(1)
bt.root.right.left = Node(1)
print(is_univalued(bt.root))

bt = BinarySearchTree()
bt.root = Node(1)
bt.root.left = Node(1)
bt.root.left.left = Node(1)
bt.root.left.right = Node(6)
bt.root.right = Node(1)
bt.root.right.left = Node(1)
print(is_univalued(bt.root))
