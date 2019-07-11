'''
Mirror Image Of Binary Tree
Problem Statement:
You are given root node of a binary tree T. You need to modify that tree in place, transform it into the mirror image of
 the initial tree T.
Input Format:
The function has one parameter of type TreeNode: the root node of binary tree T.
Output Format:
The function doesn’t need to return anything. The tree needs to be modified in place.
Constraints:
1 <= number of nodes <= 100000
Nodes will have unique values between 0 and (number of nodes-1).
Sample Test Case:
Sample Input:
        0
      /   \
    1	  2
   /  \   / \
 3    4 5   6


Sample Output:
        0
      /  \
    2	  1
   /  \   / \
 6    5 4   3


Explanation:
As we can easily visualise that input binary tree and output binary tree are mirror images of each other. So if A and B
 are two binary trees which are mirror images of each other then taking mirror image of A would generate B and vice versa.

Input/Output Format For The Custom Input:
Input Format:
The first line will have integer n denoting the number of nodes of the binary tree.
The second line will have integer root_index denoting root node index of the binary tree.
Next, n lines will have three space separated integers v l r denoting node index v's left child is l and right child is
 r (l and r can be -1 means that child is null for node index v).
Output Format:
1. If the modified root node is representing the mirror image of the given binary tree T, then binary tree represented by the
 returned mirrored root node will be printed in the below mentioned tree format.
2. If the modified root node is not representing
 the mirror image of given binary tree T, then the message “Not a mirror image” along with the binary tree represented by
 the returned mirrored root node will be printed in the below mentioned tree format.

Tree Format:
There will be n lines. Each line will have three space separated integers v l r denoting node index v's left child is l
 and right child is r (l and r can be -1 means that child is null for node index v).
'''

#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(100007)


#
# Complete the 'mirror_image' function below.
#
# The function accepts root node of binary tree as parameter.
#
# Structure of TreeNode will be:
# class TreeNode(object):
#     data = -1
#     left = None
#     right = None
#
#     def __init__(self, item):
#         self.data = item
#         self.left = None
#         self.right = None
#

def mirror_image(root):
    pass


class TreeNode(object):
    data = -1
    left = None
    right = None

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def build_tree(n, root_index, edges):
    if (n == 0):
        return None

    nodes = [None for _ in range(n)]
    nodes[root_index] = TreeNode(root_index)

    for i in range(n):
        vertex = edges[i][0]
        left = edges[i][1]
        right = edges[i][2]

        cur_node = nodes[vertex]

        if cur_node == None:
            cur_node = TreeNode(vertex)

        if left != -1:
            if nodes[left] == None:
                nodes[left] = TreeNode(left)
            cur_node.left = nodes[left]

        if right != -1:
            if nodes[right] == None:
                nodes[right] = TreeNode(right)
            cur_node.right = nodes[right]
        nodes[vertex] = cur_node
    return nodes[root_index]


def is_mirror_image(root, mirror_root, fptr):
    if not root and not mirror_root:
        return True

    if not root or not mirror_root:
        fptr.write("Returned tree is not properly mirrored. In mirror tree returned by you, at one place, instead of ")
        if not root:
            fptr.write("null node we found other node with data " + str(mirror_root.data) + ".\n")
        if not mirror_root:
            fptr.write("node with data " + str(root.data) + " we found null node.\n")
        return False

    if root.data != mirror_root.data:
        fptr.write(
            "Returned tree is not properly mirrored. In mirror tree returned by you, at one place, mirror tree node data " + str(
                mirror_root.data) + " is not matching with expected data " + str(root.data) + ".\n")
        return False

    left_result = is_mirror_image(root.left, mirror_root.right, fptr)
    right_result = is_mirror_image(root.right, mirror_root.left, fptr)

    return left_result and right_result


def print_level_order(n, root, fptr):
    if not root:
        return

    visited = set()
    queue = []
    queue.append(root)

    visited.add(root)

    while len(queue) > 0:
        cur_node = queue.pop(0)
        left_data = -1
        right_data = -1

        if cur_node.left:
            if cur_node.left not in visited:
                queue.append(cur_node.left)
                visited.add(cur_node.left)
            left_data = cur_node.left.data

        if cur_node.right:
            if cur_node.right not in visited:
                queue.append(cur_node.right)
                visited.add(cur_node.right)
            right_data = cur_node.right.data

        fptr.write(str(cur_node.data) + " " + str(left_data) + " " + str(right_data) + "\n")


if __name__ == '__main__':
    n = int(input().strip())
    root_index = int(input().strip())

    edges = []

    for _ in range(n):
        edges.append(list(map(int, input().rstrip().split())))

    fptr = sys.stdout

    root = build_tree(n, root_index, edges)
    mirror_root = build_tree(n, root_index, edges)
    mirror_image(mirror_root)

    if (not is_mirror_image(root, mirror_root, fptr)):
        fptr.write("Not a mirror image\n")

    print_level_order(n, mirror_root, fptr)

    fptr.close()


'''
We have provided two solutions: a recursive one and and an iterative one.
1) optimal_solution1.java
This is a recursive solution. The main task is to swap left and right children for every node of the tree. We are calling
 function recursively and making sure that leaf nodes are handled first then their parents and it goes up to the root node.

Time Complexity:
O(n) where n is the number of tree nodes.
Auxiliary Space Used:
O(n) where n is the number of tree nodes. That extra space is used for the call stack.
Space Complexity:
O(n).
Input is O(n) because we are storing n nodes relationships and each relationship occupies O(1) space and auxiliary space
 used is O(n). So, O(n) + O(n) -> O(n).
 
 
2) optimal_solution2.java
This solution traverses the tree breadth first using a loop and a queue, without making use of recursion.
We initialize the queue with the root node. Then we do the following until the queue is empty:
Get next node from the queue
Swap its left and right child nodes
Push its left and right children into the queue
Time Complexity:
O(n) where n is the number of nodes.
Auxiliary Space Used:
O(n) where n is the number of nodes.
We are using queue for storing nodes to do BFS traversal over tree. In the worst case scenario, queue size will be n.
Space Complexity:
O(n) where n is the number of nodes.
Input is O(n) because we are storing n nodes relationships and each relationship occupies O(1) space and auxiliary space
 used is O(n). So, O(n) + O(n) -> O(n).
'''
'''
OPTIMIAL SOLUTION 1
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


class Result {

    /*
    * Complete the 'mirror_image' function below.
    *
    * The function accepts root node of binary tree as parameter.
    */
    // ============================ Start ============================
    public static void mirror_image(TreeNode root) {
        root = mirror_image_util(root);
    }

    public static TreeNode mirror_image_util(TreeNode root){
        if (root == null)
            return root;
        
        /* do the subtrees */
        TreeNode left = mirror_image_util(root.left);
        TreeNode right = mirror_image_util(root.right);
        
        /* swap the left and right pointers */
        root.left = right;
        root.right = left;
        return root; 
    }
    // ============================= End ==============================
}

class TreeNode{
    int data;
    TreeNode left, right;
 
    public TreeNode(int item){
        data = item;
        left = right = null;
    }
}

class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());// n = Number of vertices
        int root_index = Integer.parseInt(bufferedReader.readLine().trim());// root_index = index of root vertex
        List<List<Integer>> edges = new ArrayList<>();// To store edges
        
        IntStream.range(0, n).forEach(i -> {
            try {
                edges.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(Collectors.toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });
        bufferedReader.close();
        
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        TreeNode root = build_tree(n, root_index, edges);
        TreeNode mirror_root = build_tree(n, root_index, edges);
        Result.mirror_image(mirror_root);
        if(!is_mirror_image(root, mirror_root)) {
            bufferedWriter.write("Not a mirror image");
            bufferedWriter.newLine();
        }
        print_level_order(n, mirror_root, bufferedWriter);
        bufferedWriter.close();
    }
    
    public static TreeNode build_tree(int n, int root_index, List<List<Integer>> edges){
        if(n==0) {
            return null;
        }
        TreeNode nodes[] = new TreeNode[n];
        for(int i=0;i<n;i++) {
            nodes[i] = null;
        }
        nodes[root_index] = new TreeNode(root_index);
        for(int i=0;i<n;i++) {
            List<Integer> edge = edges.get(i);
            int vertex = edge.get(0);
            int left = edge.get(1);
            int right = edge.get(2);
            TreeNode cur_node = nodes[vertex];
            
            if(cur_node==null) {
                cur_node = new TreeNode(vertex);
            }
            if(left!=-1) {
                if(nodes[left]==null){
                    nodes[left] = new TreeNode(left);
                }
                cur_node.left = nodes[left];
            }
            if(right!=-1) {
                if(nodes[right]==null){
                    nodes[right] = new TreeNode(right);
                }
                cur_node.right = nodes[right];
            }
            nodes[vertex] = cur_node;
        }
        return nodes[root_index];
    }
    
    public static boolean is_mirror_image(TreeNode root, TreeNode mirror_root){
        if(root==null && mirror_root==null) {
            return true;
        }
        if(root==null || mirror_root==null) {
            return false;
        }
        if(root.data!=mirror_root.data) {
            return false;
        }
        boolean left_result = is_mirror_image(root.left, mirror_root.right);
        boolean right_result = is_mirror_image(root.right, mirror_root.left);
        
        return left_result && right_result;
    }
   
    public static void print_level_order(int n, TreeNode root, BufferedWriter bufferedWriter) throws IOException{
        if(root==null) {
            return;
        }
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        
        int left_data = -1;
        int right_data = -1;
        
        while(!queue.isEmpty()) {
            TreeNode cur_node = queue.poll();
            left_data = -1;
            right_data = -1;

            if(cur_node.left!=null) {
                queue.add(cur_node.left);
                left_data = cur_node.left.data;
            }
            if(cur_node.right!=null) {
                queue.add(cur_node.right);
                right_data = cur_node.right.data;
            }
            bufferedWriter.write(cur_node.data+" "+left_data+" "+right_data+"\n");
        }
    }
}
'''
'''
OPTIMAL SOLTUION 2
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


class Result {

    /*
    * Complete the 'mirror_image' function below.
    *
    * The function accepts root node of binary tree as parameter.
    */
    // ============================ Start ============================
    public static void mirror_image(TreeNode root) {
        if (root == null)
            return;
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        // Do BFS. While doing BFS, keep swapping
        // left and right children
        while(!queue.isEmpty()) { 
            // pop top node from queue 
            TreeNode cur_node = queue.poll();
            
            // swap left child with right child
            TreeNode temp = cur_node.left;
            cur_node.left = cur_node.right;
            cur_node.right = temp;
            
            // push left and right children
            if (cur_node.left!=null) 
                queue.add(cur_node.left); 
            if (cur_node.right!=null) 
                queue.add(cur_node.right); 
        } 
    } 
    // ============================= End ==============================
}

class TreeNode{
    int data;
    TreeNode left, right;
 
    public TreeNode(int item){
        data = item;
        left = right = null;
    }
}

class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());// n = Number of vertices
        int root_index = Integer.parseInt(bufferedReader.readLine().trim());// root_index = index of root vertex
        List<List<Integer>> edges = new ArrayList<>();// To store edges
        
        IntStream.range(0, n).forEach(i -> {
            try {
                edges.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(Collectors.toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });
        bufferedReader.close();
        
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        TreeNode root = build_tree(n, root_index, edges);
        TreeNode mirror_root = build_tree(n, root_index, edges);
        Result.mirror_image(mirror_root);
        if(!is_mirror_image(root, mirror_root)) {
            bufferedWriter.write("Not a mirror image");
            bufferedWriter.newLine();
        }
        print_level_order(n, mirror_root, bufferedWriter);
        bufferedWriter.close();
    }
    
    public static TreeNode build_tree(int n, int root_index, List<List<Integer>> edges){
        if(n==0) {
            return null;
        }
        TreeNode nodes[] = new TreeNode[n];
        for(int i=0;i<n;i++) {
            nodes[i] = null;
        }
        nodes[root_index] = new TreeNode(root_index);
        for(int i=0;i<n;i++) {
            List<Integer> edge = edges.get(i);
            int vertex = edge.get(0);
            int left = edge.get(1);
            int right = edge.get(2);
            TreeNode cur_node = nodes[vertex];
            
            if(cur_node==null) {
                cur_node = new TreeNode(vertex);
            }
            if(left!=-1) {
                if(nodes[left]==null){
                    nodes[left] = new TreeNode(left);
                }
                cur_node.left = nodes[left];
            }
            if(right!=-1) {
                if(nodes[right]==null){
                    nodes[right] = new TreeNode(right);
                }
                cur_node.right = nodes[right];
            }
            nodes[vertex] = cur_node;
        }
        return nodes[root_index];
    }
    
    public static boolean is_mirror_image(TreeNode root, TreeNode mirror_root){
        if(root==null && mirror_root==null) {
            return true;
        }
        if(root==null || mirror_root==null) {
            return false;
        }
        if(root.data!=mirror_root.data) {
            return false;
        }
        boolean left_result = is_mirror_image(root.left, mirror_root.right);
        boolean right_result = is_mirror_image(root.right, mirror_root.left);
        
        return left_result && right_result;
    }
   
    public static void print_level_order(int n, TreeNode root, BufferedWriter bufferedWriter) throws IOException{
        if(root==null) {
            return;
        }
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        
        int left_data = -1;
        int right_data = -1;
        
        while(!queue.isEmpty()) {
            TreeNode cur_node = queue.poll();
            left_data = -1;
            right_data = -1;

            if(cur_node.left!=null) {
                queue.add(cur_node.left);
                left_data = cur_node.left.data;
            }
            if(cur_node.right!=null) {
                queue.add(cur_node.right);
                right_data = cur_node.right.data;
            }
            bufferedWriter.write(cur_node.data+" "+left_data+" "+right_data+"\n");
        }
    }
}
'''
