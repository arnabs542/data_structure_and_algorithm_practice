'''
Kth Smallest Element Of BST
Problem Statement:
Given a BST (binary search tree), of size N, containing integer elements, and an integer k, you have to find kth smallest
 element of given BST.
Input/Output Format For The Function:
Input Format:
There are two arguments in the input. First one is the root of the BST and second one is an integer k.
Output Format:
Return an integer kmin, denoting kth smallest element of BST.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer N, denoting size of input array arr. In next N lines, ith line should
 contain an integer arr[i], denoting a value at index i of arr.
Input BST will be constructed by inserting elements of array arr to an empty BST in order arr[0], arr[1], …, arr[N-1].
If n = 3, k = 3 and arr = [1, 2, 3], then input should be:
3
2
3
1
3
Output Format:
There will be one line of output, containing an integer kmin, denoting the result returned by solution function.
For input n = 3, k = 3 and arr = [1, 2, 3], output will be:
3
Constraints:
1 <= N <= 6000
1 <= k <= N
-2 * 10^9 <= value stored in any node <= 2 * 10^9
BST need not to be balanced.
You are not allowed
 to alter the structure or data inside the given BST.
Sample Test Case:
Sample Input:
BST =
2 is the root node.
1 is 2's left child.
3 is 2's right child.
k = 3
Sample Output:
3
Explanation:
3rd smallest element is 3.
Notes:
Maximum time allowed in interview: 20 Minutes.
'''

#!/bin/python

import sys
import os
sys.setrecursionlimit(7000)

class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None

def bst_insert(root, val):
    if (root == None):												# destination.
        return TreeNode(val)
    root_copy = root
    while (1):
        if (val <= root.val and root.left_ptr != None):
            root = root.left_ptr
        elif (val <= root.val):
            root.left_ptr = TreeNode(val)
            return root_copy
        elif (root.right_ptr != None):
            root = root.right_ptr
        else:
            root.right_ptr = TreeNode(val)
            return root_copy
    return root_copy


'''
    For your reference:

    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''


def kth_smallest_element(root, k):
    pass


if __name__ == "__main__":
    f = sys.stdout

    N = int(input())

    root = None

    for i in range(0, N):
        data = int(input())
        root = bst_insert(root, data)
    k = int(input())

    ans = kth_smallest_element(root, k)
    f.write(str(ans) + "\n")

    f.close()

'''
We want to find kth smallest element of given BST. 
If we can get all the elements of BST in sorted order then our answer will be the kth element. We know that inroder traversal
 visites elements in sorted order! But time complexity of the problem is O(N) and auxiliary space used is also O(N).
Note that we need not to store all the elements, we can just keep the count on number of nodes visited till now and when
 counter becomes k it is the node we wanted! 
Your code should look like:
void modified_inorder(root, k)
{
    handle base case;
    modified_inorder(root->l);
    if (answer is not found in left subtree)
    {
        counter++;	// make sure that you are incrementing after left subtree is visited. 
        consider current node;
        modified_inorder(root->r);
    }
}

Now have a look at the code provided by us.
Time complexity:
In terms of N we can write it as O(N).
Using other variables we can write tighter bound for the same solution. In terms of height of the tree and k, we can write
 tighter bound as O(height of tree + k). 
The code first traverses down to the leftmost node which takes O(h) time, then traverses k elements in O(k) time. Therefore
 overall time complexity is O(h + k).
Note that even if k=1 the algorithm has to go all the way down the tree to find the smallest element, visiting all the nodes
 on the way, and visiting one node takes constant time. So far we have used O(h) time where h is the height of the tree
 (worst case is when the left-most leaf of the tree is the longest one).
Having gone all the way down to the smallest element, the algorithm then visits exactly k nodes from there (still constant
 time per node); complexity so far is O(h) + O(k).
Having found and saved the k-th element value, the algorithm still needs to pop out from the recursion depth so that it
 can return the answer in the end. For that it will use constant time per level of recursion, per depth of the tree (worst
 case again is when we have found the k-th element at the leaf of the longest branch of the tree). That takes another O(h)
 time. Therefore the overall time complexity: O(h) + O(k) + O(h) = O(2h + k) = O(h + k).
Auxiliary space used:
O(height of the tree) due to recursive calls. (Assuming that you are already given BST you are not creating it.)
Space complexity:
O(N) due to input array and BST. 
'''
'''
OPTIMAL SOLUTION
#!/bin/python

import sys
import os
sys.setrecursionlimit(7000)

class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None

def bst_insert(root, val):
    # base case
    if (root == None):												
        return TreeNode(val)
    root_copy = root
    while (1):
        # insert in left subtree
        if (val <= root.val and root.left_ptr != None):             
            root = root.left_ptr
        elif (val <= root.val):
            root.left_ptr = TreeNode(val)
            return root_copy
        # insert in right subtree
        elif (root.right_ptr != None):                              
            root = root.right_ptr
        else:
            root.right_ptr = TreeNode(val)
            return root_copy
    return root_copy


#-------------------------------START-----------------------------------

#    For your reference:
#    
#    class TreeNode:
#    def __init__(self, node_value):
#        self.val = node_value
#        self.left_ptr = None
#        self.right_ptr = None

kth_element = 0                                                
counter = 0

def get_k_th_element(root, k):
    # don't forget this
    global counter                                                      
    global kth_element
    # either root is null or we have already found the answer.
    if (root == None or counter >= k):                                  
        return
        
    # first try to find from left subtree, because elements in left suubtree will be smaller than 
    # the root.           
    
    get_k_th_element(root.left_ptr, k)                                  
    # if we have not found the answer till now. 
    if (counter < k):                                                   
        counter += 1
        # if current node is the kth node.
        if (counter == k):                                              
            kth_element = root.val
            return
        # we have explored left subtree and the root now explore right subtree. 
        get_k_th_element(root.right_ptr, k)                             

def kth_smallest_element(root, k):
    get_k_th_element(root, k)                               
    return kth_element

#-------------------------------------STOP---------------------------------

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')
    
    N = int(input())

    root = None
    
    for i in range(0, N):
        data = int(input())
        root = bst_insert(root, data)
    k = int(input())
    
    ans = kth_smallest_element(root, k)
    f.write(str(ans) + "\n")

    f.close()
'''
