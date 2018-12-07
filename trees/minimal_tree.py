from trees.binary_search_tree import BinarySearchTree
'''
Given a sorted array, create a BST that has the smallest depth possible.
'''

def minimal_tree(sorted_list):
    bst = BinarySearchTree()
    if len(sorted_list) < 1:
        raise ValueError
    if len(sorted_list) == 1:
        bst.create(sorted_list[0])
        return bst
    add_middle_until_empty(bst, sorted_list)
    return bst

def add_middle_until_empty(tree, sorted_list):
    if len(sorted_list) <= 0:
        return None
    if len(sorted_list) == 1:
        tree.create(sorted_list[0])
        return tree
    else:
        middle_element = sorted_list[len(sorted_list)//2]
        tree.create(middle_element)
        add_middle_until_empty(tree, sorted_list[:len(sorted_list)//2])
        add_middle_until_empty(tree, sorted_list[(len(sorted_list)//2)+1:])
    return tree

# a = []
# a = [1]
# a = [1,2]
# a = [1,2,3]
# a = [1,2,3,4,5]
# a = [1,2,3,4,5,6,7,8,9,10]
a = [1,2,3,4,5,6,7,8,9,10,11]

tree = minimal_tree(a)
tree.in_order_traversal()
