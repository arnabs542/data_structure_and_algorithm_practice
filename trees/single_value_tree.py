from trees.binary_search_tree import BinarySearchTree,Node

def is_same_value(current_node, val):
    if current_node == None:
        return 0

    if current_node.data == val:
        return 1 + is_same_value(current_node.left, val) + is_same_value(current_node.right, val)
    return is_same_value(current_node.left, val) + is_same_value(current_node.right, val)

def num_single_value_trees(root):
    return is_same_value(root, root.data)

bt = BinarySearchTree()
bt.create(1)
bt.root.left = Node(1)
bt.root.right = Node(1)

print(num_single_value_trees(bt.root))

bt = BinarySearchTree()
bt.create(1)
bt.root.left = Node(2)
bt.root.right = Node(3)

print(num_single_value_trees(bt.root))
