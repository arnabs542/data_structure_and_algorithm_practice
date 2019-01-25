from trees.binary_search_tree import BinarySearchTree,Node

class MaxSum:
    def __int__(self, root):
        self.max = float('-inf')
        self.root = root

    def find_max_path_rec(self, current_node):
        if current_node == None:
            return 0
        left = self.find_max_path_rec(current_node.left)
        right = self.find_max_path_rec(current_node.right)
        self.max = max(self.max, left+current_node.data+right)
        return max(left + current_node.data, right + current_node.data, current_node.data)

    def find_max_path(self):
        self.find_max_path_rec(self.root)
        return self.max

'''
    -20
   /   \
  1     100
MAX = 100
'''
bst = BinarySearchTree(-20)
bst.root.left = Node(1)
bst.root.right = Node(100)
m = MaxSum()
m.__int__(bst.root)
print(m.find_max_path())

'''
    20
   /   \
  1     100
MAX = 121
'''
bst = BinarySearchTree(20)
bst.root.left = Node(1)
bst.root.right = Node(100)
m = MaxSum()
m.__int__(bst.root)
print(m.find_max_path())

'''
    -120
   /   \
  110   100
MAX = 110
'''
bst = BinarySearchTree(-120)
bst.root.left = Node(110)
bst.root.right = Node(100)
m = MaxSum()
m.__int__(bst.root)
print(m.find_max_path())

'''
    -120
   /   \
  110   100
       /   \
      5     6    
MAX = 111
'''
bst = BinarySearchTree(-120)
bst.root.left = Node(110)
bst.root.right = Node(100)
bst.root.right.left = Node(5)
bst.root.right.right = Node(6)
m = MaxSum()
m.__int__(bst.root)
print(m.find_max_path())

'''
    -120
   /   \
  110   100
       /   \
      5     -6
              \
               700   
MAX = 700+5+(-6)+100
'''
bst = BinarySearchTree(-120)
bst.root.left = Node(110)
bst.root.right = Node(100)
bst.root.right.left = Node(5)
bst.root.right.right = Node(-6)
bst.root.right.right.left = Node(700)
m = MaxSum()
m.__int__(bst.root)
print(m.find_max_path())

'''
    -120
   /   \
  110   -1000
       /   \
      5     -6
              \
               700   
MAX = 700
'''
bst = BinarySearchTree(-120)
bst.root.left = Node(110)
bst.root.right = Node(-1000)
bst.root.right.left = Node(5)
bst.root.right.right = Node(-6)
bst.root.right.right.left = Node(700)
m = MaxSum()
m.__int__(bst.root)
print(m.find_max_path())
