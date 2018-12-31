from trees.binary_search_tree import BinarySearchTree,Node
from collections import deque

bst = BinarySearchTree()
bst.root = Node(1)
bst.root.left = Node(2)
bst.root.right = Node(3)
bst.root.left.left = Node(4)
bst.root.left.right = Node(5)
bst.root.right.left = Node(6)
bst.root.right.right = Node(7)

def pre_order_dfs_rec(node):
    if node == None:
        return
    print(node.data, end=" ")
    pre_order_dfs_rec(node.left)
    pre_order_dfs_rec(node.right)

print('DFS')
print('Recursive - Pre-Order: ', end='')
pre_order_dfs_rec(bst.root)
print()
def dfs_iterative(node):
    if node:
        stack = deque()
        stack.append(node)
        while len(stack) > 0:
            current = stack.pop()
            print(current, end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

print('Iterative - Pre-Order: ', end='')
dfs_iterative(bst.root)
print()

def in_order_dfs_rec(node):
    if node:
        if node.left:
            in_order_dfs_rec(node.left)
        print(node.data, end=" ")
        if node.right:
            in_order_dfs_rec(node.right)

print('Recursive - In-Order: ', end='')
in_order_dfs_rec(bst.root)
print()

def post_order_dfs_rec(node):
    if node:
        if node.left:
            post_order_dfs_rec(node.left)
        if node.right:
            post_order_dfs_rec(node.right)
        print(node.data, end=" ")

print('Recursive - Post-Order: ', end='')
post_order_dfs_rec(bst.root)
print()
print()

def bfs_iterative(node):
    if node:
        queue = deque()
        queue.appendleft(node)
        while len(queue) > 0:
            current = queue.pop()
            print(current.data, end=" ")
            if current.left:
                queue.appendleft(current.left)
            if current.right:
                queue.appendleft(current.right)

print('BFS')
print('Iterative: ', end='')
bfs_iterative(bst.root)
print()

