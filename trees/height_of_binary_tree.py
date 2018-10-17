from trees.binary_search_tree import BinarySearchTree

def height(root):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 0

    left = right = 0
    if root.left:
        left = 1 + height(root.left)
    if root.right:
        right = 1 + height(root.right)

    if left > right:
        return left
    return right

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print('The height of the given tree is ' + str(height(tree.root)))

'''
SAMPLE INPUT
7
3 5 2 1 4 6 7

EXPECTED OUTPUT
3
'''
