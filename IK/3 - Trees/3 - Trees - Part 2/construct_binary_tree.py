'''
Construct_Binary_Tree
Problem Statement:
Inorder traversal - Process all nodes of a binary tree by recursively processing the left subtree, then processing the root,
 and finally the right subtree.
Preorder traversal - Process all nodes of a binary tree by recursively processing the root, then processing the left subtree,
 and finally the right subtree.
Given the inorder and preorder traversal of a valid binary tree, you have to construct the binary tree.
[Interesting article to read: http://www.geeksforgeeks.org/if-you-are-given-two-traversal-sequences-can-you-construct-the-binary-tree/]

Input Format:
You are given two integer array named inorder and preorder of size n, containing positive values <= 10^5
Output Format:
Return root pointer of the constructed binary tree.
Constraints:
0 <= n <= 10^5
1 <= inorder[i], preorder[i] <= 10^5
Values stored in the binary tree are unique.
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
inorder = [2, 1, 3] and preorder = [1, 2, 3]
Sample Output 1:
  1
 / \
2  3



Explanation 1:
In this case, Binary tree will be look like as given above.
Return the pointer of root node of constructed binary tree. In this case root treenode has value '1'.

Sample Test Case 2:
Sample Input 2:
inorder = [3, 2, 1, 5, 4, 6] and preorder = [1, 2, 3, 4, 5, 6]

Sample Output 2:

     1
    / \
  2   4
 /   / \
3   5  6
'''
#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(100007)

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


#
# Complete the 'constructBinaryTree' function below.
#
# The function accepts INTEGER_ARRAY inorder and preorder as parameter and returns Root pointer of constructed binary tree.
# class TreeNode:
#    def __init__(self, x):
#        self.value = x
#        self.left = None
#        self.right = None
#

def constructBinaryTree(inorder, preorder):
    # Write your code here
    pass


def printPreOrder(root):
    if (root == None):
        print('#', end=''),
        return

    st = []
    st.append(root)

    while (len(st) > 0):

        node = st.pop()

        if (node == None):
            print('#', end=''),
            continue

        print(str(node.value), end=''),
        st.append(node.right)
        st.append(node.left)


if __name__ == '__main__':
    arr_len = int(input().strip())

    inorder = []
    preorder = []

    for _ in range(arr_len):
        arr_item = int(input().strip())
        inorder.append(arr_item)

    arr_len = int(input().strip())

    for _ in range(arr_len):
        arr_item = int(input().strip())
        preorder.append(arr_item)

    Node = constructBinaryTree(inorder, preorder)
    printPreOrder(Node)
    print('\n')


'''
EDITORIAL
We will learn recursive approach by taking an example:

Let's take example from sample input:

inorder[] = [3, 2, 1, 5, 4, 6]
preorder[] = [1, 2, 3, 4, 5, 6]

Here, as per preorder traversal definition it traverse the tree recursively by travesing the root first, then left subtree and then right subtree.
	• So, we can say that first value of preorder[] is root node value of binary tree, here its 1.
	• Now, search the index of that value in inorder[]. Say you find it at position i, once you find it, make note of elements which are left to i (This will construct the left subtree) and elements which are right to i (This will construct the right subtree).

See the above steps and recursively build left subtree and link it root.left and recursively build right subtree and link it root.right.

Let's have a look how recursion will happen in our case,

Root:

(1's position confirmed)

           1
          / \
     [3,2]  [5,4,6]


In the left subtree of the root:

(2's position confirmed)

           1
          / \
        2 [5,4,6]
        |
       [3]


(3's position confirmed)

           1
          / \
        2 [5,4,6]
       /
     3


In the right subtree of the root:

(4's position confirmed)

           1
          / \
        2   4
       / |
     3 [5,6]


(5's position confirmed)

           1
          / \
        2   4
       /   / |
     3    5 [6]


(6's position confirmed)

           1
          / \
        2   4
       /   / \
     3    5   6


So, the above tree will be our binary tree for given test case. Return the root treenode which is 1 in this case.

1) brute_solution.java

Time Complexity:

O(n^2), here n is length of given inorder[] or preorder[] array, in other words count of total treenodes of binary tree.

Suppose you are given tree in which all nodes have only left child, there is no right child of any treenode, then for every preorder[] value it will take O(n) to search in inorder[].

So, In worst case time complexity will be O(n^2).

Auxiliary Space Used:

O(n).

As we are constructing the binary tree and storing values in treenodes. Every node will take constant space to store value and addresses for left and right treenode. So, it will be O(n).

Space Complexity:

O(n).

As input is O(n) and auxiliary space used is also O(n).

So, O(n) + O(n) -> O(n).


2) optimal_solution.java

Time Complexity:

O(n).

We are using hashmap to search index of value in inorder[], and hashmap takes O(1) time (search in hash map can be upto O(n) in worst case, when values are in wide range and carefullly chosen) to search value. So, in every case time complexity will be O(n).

Auxiliary Space Used:

O(n).

As we are constructing binary tree and storing value in treenode, so every node will take constant space to store value and addresses for left and right treenode. Here, we are using hashmap to store inorder[] values with index and it will take O(n) space to store <value,index> pair. So, Auxiliary space will be O(n) + O(n) -> O(n).

Space Compelxity:

O(n).

As input is O(n) and auxiliary space used is also O(n).

So, O(n) + O(n) -> O(n).
'''
'''
BRUTE FORCE
import java.io.*;
import java.util.*;
class Solution {

    public static void main(String[] args) throws IOException{
        // TODO Auto-generated method stub
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int arr_len = Integer.parseInt(sc.readLine());

        int inorder [] = new int[arr_len];
        int preorder [] = new int[arr_len];

        for(int i = 0 ; i < arr_len ; i++) {
            inorder[i] = Integer.parseInt(sc.readLine());
        }

        for(int i = 0 ; i < arr_len ; i++) {
            preorder[i] = Integer.parseInt(sc.readLine());
        }

        TreeNode root = constructBinaryTree(inorder, preorder);
        
    }
    
    // ---------------------- Start --------------------------

    static int current_index;
    
    public static TreeNode constructBinaryTree(int inorder[], int preorder[]) {
        
        int arr_len = inorder.length;
        
        current_index = 0;
        
        return utilConstructBinaryTree(inorder, preorder, 0, arr_len - 1);
        
    }
    
        /* Recursive function to construct a binary tree using Inorder traversal 'inorder[]'
        and Preorder traversal 'preorder[]'. Initial value of 'start' and 'end' should be '0' 
        and 'arr_len-1'*/
    
       // Initially 'current_index' should be '0'.

    /* Here, 'start' and 'end' values indicate search range in 'inorder[]' for value at index 
          'current_index' of 'preorder[]'.*/

    // Create 'root' node of value at index 'current_index' of 'preorder[]'.

    /* If value found at index 'x' in 'inorder[]', it means values of range [start, x] of 'inorder[]' will 
        lie in left subtree of root node and values of range [x, end] of 'inorder[]' will lie 
        in right subtree of root node.*/


    public static TreeNode utilConstructBinaryTree(int inorder[], int preorder[], int start, int end) {


        if(start>end)
            return null;
        
        /* Pick current node from Preorder traversal using current_index 
            and increment current_index */
        
        TreeNode root = new TreeNode(preorder[current_index++]);

        /* If above node has no children then return */
        
        if(start == end) {
            return root;
        }
        
        /* Else find the index of this node in Inorder traversal */
        
        int index_of_inorder = findIndex(inorder, root.value, start, end);
        
        /* Using index in Inorder traversal, construct left and 
            right subtrees */
        
        root.left = utilConstructBinaryTree(inorder, preorder, start, index_of_inorder - 1);
        root.right = utilConstructBinaryTree(inorder, preorder, index_of_inorder + 1, end);
        
        return root;
    }
    
    /* This function is to search 'value' in 'inorder' in the range [start, end] and 
       returns index of that 'value'. */
    
    public static int findIndex(int inorder[], int value, int start, int end) {
        
        while(start<=end) {
            
            if(inorder[start] == value) {
                return start;
            }
            
            start++;
        }
        
        return -1;
        
    }
    
    // ---------------------- End --------------------------

}

class TreeNode {
    
    int value;
    TreeNode left,right;
    
    TreeNode(int value) {
        this.value = value;
        left = null;
        right = null;
    }

}
'''
'''
OPTIMAL SOLUTION
import java.io.*;
import java.util.*;

class Solution {

    public static void main(String[] args) throws IOException{
        // TODO Auto-generated method stub
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int arr_len = Integer.parseInt(sc.readLine());

        int inorder [] = new int[arr_len];
        int preorder [] = new int[arr_len];

        for(int i = 0 ; i < arr_len ; i++) {
            inorder[i] = Integer.parseInt(sc.readLine());
        }

        for(int i = 0 ; i < arr_len ; i++) {
            preorder[i] = Integer.parseInt(sc.readLine());
        }

        TreeNode root = constructBinaryTree(inorder, preorder);
    }


    // ---------------------------- Start -------------------------------
    
    static int current_index;

    
    public static TreeNode constructBinaryTree(int inorder[], int preorder[]) {

        int arr_len = inorder.length;
        
        /* HashMap to store values of 'inorder[]' with index. So, here key and value pair 
            of hashmap will be value and index pair of 'inorder[]'. */
        
        HashMap<Integer, Integer> value_hash_inorder = new HashMap();
        
        // Storing value and index pair of 'inorder[]' in hashmap.

        for(int i = 0 ; i<arr_len ; i++) {
            value_hash_inorder.put(inorder[i], i);
        }

        current_index = 0;

        return utilConstructBinaryTree(inorder, preorder, 0, arr_len - 1, value_hash_inorder);

    }
    
    /* Recursive function to construct a binary tree using Inorder traversal 'inorder[]'
       and Preorder traversal 'preorder[]'. Initial value of 'start' and 'end' should be '0' 
       and 'arr_len-1'*/

    // Initially 'current_index' should be '0'.

    /* Here, 'start' and 'end' values indicate search range in 'inorder[]' for value at index 
       'current_index' of 'preorder[]'.*/

    // Create 'root' node of value at index 'current_index' of 'preorder[]'.

    /* If value found at index 'x' in 'inorder[]', it means values of range [start, x] of 'inorder[]' will 
       lie in left subtree of root node and values of range [x, end] of 'inorder[]' will lie 
       in right subtree of root node.*/

    public static TreeNode utilConstructBinaryTree(
            int inorder[], int preorder[], int start, 
            int end, HashMap<Integer,Integer> value_hash_inorder) {

        if(start>end)
            return null;

        /* Pick current node from Preorder traversal using current_index 
        and increment current_index */
        
        TreeNode root = new TreeNode(preorder[current_index++]);
        
        /* If above node has no children then return */

        if(start == end) {
            return root;
        }

        /* Else find the index of this node in Inorder traversal */
        int index_of_inorder = value_hash_inorder.get(root.value);
        
        root.left = utilConstructBinaryTree(
                inorder, preorder, start, index_of_inorder - 1, value_hash_inorder);
        root.right = utilConstructBinaryTree(
                inorder, preorder, index_of_inorder + 1, end, value_hash_inorder);

        return root;
    }
    
    // ---------------------------- End -------------------------------

}

class TreeNode {
    
    int value;
    TreeNode left,right;
    
    TreeNode(int value) {
        this.value = value;
        left = null;
        right = null;
    }

}
'''
