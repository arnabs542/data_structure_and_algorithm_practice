from trees.binary_search_tree import BinarySearchTree


def lca(root, v1, v2):
    # Enter your code here
    if root == None:
        return None

    if root.info == v1 or root.info == v2:
        return root

    left = lca(root.left, v1, v2)
    right = lca(root.right, v1, v2)

    if left and right:
        return root

    if left != None:
        return left
    return right

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)

'''
SAMPLE INPUT
6
4 2 3 1 7 6
4 2
EXPECTED OUTPUT
4
'''

