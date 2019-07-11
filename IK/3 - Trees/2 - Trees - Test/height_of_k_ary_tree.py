'''
Height Of K-Ary Tree
Problem Statement:
Given a k-ary tree T, containing N nodes. You have to find height of the tree. (Length of the longest path from root to
 any node.)
(We are looking for number of edges on longest path from root to any node, not number of nodes on longest path from root
 to any node.)
Definition from Wikipedia: A k-ary tree is a rooted tree in which each node has no more than k children. A binary tree is
 the special case where k=2.
Input/Output Format For The Function:
Input Format:
There is only one argument denoting the root of the k-ary tree.
From any node, you can access all its children using node's property named children, which is an array of nodes.
For 3-ary tree:
1 is the root of the tree.
2's parent is 1.
3's parent is 1.
5's parent is 1.
4's parent is 5.
children of node 1 = [node 2, node 3, node 5].
children of node 2 = [].
children of node 3 = [].
children of node 4 = [].
children of node 5 = [node 4].
Look at the comment in the code editor, to know implementation details of the node, in your preferred language.
Output Format:
Return an integer hmax, denoting height of the k-ary tree.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer k, denoting that input tree is an k-ary tree T.
In next line, there should be an integer (N-1), denoting no of edges in T. In next (N-1) lines, ith line should contain
 an integer from[i], denoting value at one endpoint of an edge.
In next line, there should be an integer (N-1), denoting no of edges in T. In next (N-1) lines, ith line should contain
 an integer to[i], denoting value at other endpoint of an edge.
If k = 3, N = 5, from = [1, 1, 1, 5] and to = [3, 2, 5, 4], then input should be:
3
4
1
1
1
5
4
3
2
5
4
Output Format:
There will be one line of output, containing an integer hmax, denoting the result returned by solution function.
For input k = 3, N = 5, from = [1, 1, 1, 5] and to = [3, 2, 5, 4], output will be:
2
Constraints:
1 <= N <= 10^5
0 <= k <= N - 1

Sample Test Case:
Sample Input:
3-ary tree:
1 is the root of the tree.
2's parent is 1.
3's parent is 1.
5's parent is 1.
4's parent is 5.

Sample Output:
2

Explanation:
Given a 3-ary tree with 5 nodes. Node 1 has 3 children 2, 3 and 5, and node 5 has one child 4.
Longest path from root is 1 -> 5 -> 4 and it's length is 2.
'''

#!/bin/python3

import sys
import os

sys.setrecursionlimit(101000)

class TreeNode:
    def __init__(self):
        # No values stored in nodes because values don't matter.
        self.children = []


    # For your reference:
    #
    # class TreeNode:
    #     def __init__(self):
    #         self.children = []



# Complete the function below.

def find_height(root):
    pass


address = {}

def build_tree(frm, to):
    N = len(frm) + 1
    # Clear the global variable.
    address = {}
    for i in range(1, N + 1):
        # Create N nodes.
        address[i] = TreeNode()
    for i in range(0, N - 1):
        # Link the nodes. (Build the k-ary tree.)
        address[frm[i]].children.append(address[to[i]])
    return address[1]

if __name__ == "__main__":
    f = sys.stdout

    k = int(input())

    from_cnt = 0
    from_cnt = int(input())
    from_i = 0
    frm = []
    while from_i < from_cnt:
        from_item = int(input())
        frm.append(from_item)
        from_i += 1


    to_cnt = 0
    to_cnt = int(input())
    to_i = 0
    to = []
    while to_i < to_cnt:
        to_item = int(input())
        to.append(to_item)
        to_i += 1

    root = build_tree(frm, to)

    res = find_height(root)
    f.write(str(res) + "\n")


    f.close()



'''
When we are dealing with binary tree, our node structure looks like:
struct node
{
    int val;
    node *left_child;
    node *right_child;
};
But when we are given k-ary tree then it is not a good idea to manage each pointer separately. (when k = 500 should we define
 500 pointers?) 
When we are dealing with k-ary tree, our node structure should look like:
struct node
{
    int val;
    vector<node*> children;
};
Here we only need to find the height hence what value each node is storing does not matter, only thing that matters is how
 nodes are connected to each other. So in input also we are just given how nodes are connected to each other. 
Height of the tree = Number of edges in longest path from root to any node = Number of nodes in longest path from root to
 any node - 1.
We can find height of tree using height of its subtrees. 
More specifically,
height(parent) = max(height(children)) + 1 : when parent is not a leaf node. 
0 : when parent is a leaf node. 
We can use algorithm similar to dfs to do all these calculations. 
Now have a look at the code provided by us.
Time complexity of the solution is O(N) because our solution is similar to dfs. (Here we have assumed that addition and
 lookup on random data in unordered_map is O(1))
Auxiliary space used and space complexity of our programme is O(N) because we have used unordered_map to store N addresses
 and created the k-ary tree of size N. 
As mentioned in the problem statement, some languages like javascript and python might not pass one testcase. The reason
 is given tree in that testcase is degenerate tree and we are using algorithm similar to dfs. Hence there will be ~10^5
 recursive calls to reach the base case and some languages don't allow that many recursive calls.  
'''
'''
#!/bin/python3

import sys
import os

sys.setrecursionlimit(101000)

class TreeNode:
    def __init__(self):
        # No values stored in nodes because values don't matter.
        self.children = []

#	--------------------------------START------------------------------------

    # For your reference:
    # 
    # class TreeNode:
    #     def __init__(self):
    #         self.children = []


# Complete the function below.

def find_height(root):
    # Handle base case when root is a leaf node.
    if not root.children:
        return 0
    h = 0
    for child in root.children:
        # Find height of each child, update max height if needed.
        h = max(h, find_height(child))
    return h + 1 # Current node is one edge taller than its tallest child, so "+1".

#
#	--------------------------------STOP------------------------------------
#

address = {}

def build_tree(frm, to):
    N = len(frm) + 1
    # Clear the global variable.
    address = {}
    for i in range(1, N + 1):
        # Create N nodes.
        address[i] = TreeNode()
    for i in range(0, N - 1):
        # Link the nodes. (Build the k-ary tree.)
        address[frm[i]].children.append(address[to[i]])
    return address[1]

if __name__ == "__main__":
    f = sys.stdout

    k = int(input())

    from_cnt = 0
    from_cnt = int(input())
    from_i = 0
    frm = []
    while from_i < from_cnt:
        from_item = int(input())
        frm.append(from_item)
        from_i += 1


    to_cnt = 0
    to_cnt = int(input())
    to_i = 0
    to = []
    while to_i < to_cnt:
        to_item = int(input())
        to.append(to_item)
        to_i += 1

    root = build_tree(frm, to)

    res = find_height(root)
    f.write(str(res) + "\n")


    f.close()
'''
