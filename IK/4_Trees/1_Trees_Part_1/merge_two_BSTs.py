'''
Merge Two BSTs
Problem Statement:
Given two BSTs (Binary Search Trees), one with N1 number of nodes and other one with N2 number of nodes.
Your task is to merge them such that:
- Resultant tree is height balanced.
- Resultant tree is a BST.
- Resultant tree contains all values from given BST-1.
- Resultant tree contains all values from given BST-2.
- Size of the resultant tree is N1 + N2.
- For any value, no of occurrences in resultant tree = no of occurrences in BST-1 + no of occurrences in BST-2. (If BST-1
 contains 3 nodes with value 50 and BST-2 contains 4 nodes with value 50, then resultant tree should contain exactly 7 nodes
 with value 50.)
Any resultant tree, satisfying all the above conditions will be considered as valid answer.
Input/Output Format For The Function:
Input Format:
There are two arguments, first one is the root of the first BST with N1 number of nodes and second one is the root of the
 second BST with N2 number of nodes.
Output Format:
Return root of the resultant BST.
Input/Output Format For The Custom Input:
Input Format:
The first line of the input contains N1, the size of the first BST.
The next N1 lines contain the parent index array of BST-1, where the ith element is the parent index (0-based) of the ith
 node (parent of the root is -1).
Example for N1 = 3:
1
-1
1
parent of the 0th node is 1st node, 1st node is root and parent of the 2nd node is also 1st node.
The next N1 lines contain the child array of BST-1, where the ith element is 0 if it is the left child, 1 if it is the right
 child or -1 if it is the root.
Example of N1 = 3:
0
-1
1
0th node is left child of 1st node, 1st node is root and 2nd node is right child of 1st node.
The next N1 lines contain the key array of BST-1, where the ith element is the key of the ith node.
Example of N1 = 3:
1
2
3
The following lines describe the BST-2 in the similar way.
Output Format:
If the returned tree is height balanced then:
Inorder traversal of the returned tree will be printed where each value is on a new line.
else:
Note "Returned tree is not height balanced" will be printed.
Constraints:
1 <= N1, N2 <= 100000
Node value of the BSTs: 1 <= key1, key2 <= 1000000000
You are not allowed to modify the structure of the given BSTs.
Sample Test Case:
Sample Input:
Tree-1:
    2
   /  \
 1   3

Tree-2:
   7
  /  \
 6   8

Sample Output:
(one possible resultant tree)
    6
   /  \
  2   7
 /  \   \
1   3   8

Tree node structure:
class Node {
  public:
    int key;
    Node* left;
    Node* right;
    Node(int k) {
      key = k;
      left = NULL;
      right = NULL;
    }
};
'''
#!/bin/python

import os
import sys

sys.setrecursionlimit(101000)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Complete this function and return root of the BST
def mergeTwoBSTs(root1, root2):
    pass


def buildTree(idx, key, tree):
    root = Node(key[idx])

    if tree[idx][0] != -1:
        root.left = buildTree(tree[idx][0], key, tree)
    if tree[idx][1] != -1:
        root.right = buildTree(tree[idx][1], key, tree)

    return root


class Height:
    def __init__(self):
        self.height = 0


def isBalanced(temp, height):
    if temp is None:
        return True

    lh = Height()
    rh = Height()

    l = isBalanced(temp.left, lh)
    r = isBalanced(temp.right, rh)

    height.height = max(lh.height, rh.height) + 1

    if abs(lh.height - rh.height) <= 1 and l and r:
        return True
    return False


def inOrderTraversal(temp, f):
    if temp is None:
        return
    inOrderTraversal(temp.left, f)
    f.write(str(temp.key) + '\n')
    inOrderTraversal(temp.right, f)


if __name__ == "__main__":
    f = sys.stdout

    N1 = int(input())

    parent1 = []
    for _ in range(N1):
        operations_item = int(input())
        parent1.append(operations_item)

    child1 = []
    for _ in range(N1):
        operations_item = int(input())
        child1.append(operations_item)

    key1 = []
    for _ in range(N1):
        operations_item = int(input())
        key1.append(operations_item)

    N2 = int(input())

    parent2 = []
    for _ in range(N2):
        operations_item = int(input())
        parent2.append(operations_item)

    child2 = []
    for _ in range(N2):
        operations_item = int(input())
        child2.append(operations_item)

    key2 = []
    for _ in range(N2):
        operations_item = int(input())
        key2.append(operations_item)

    tree1 = []
    tree2 = []

    for i in range(N1):
        tree1.append([-1, -1])

    for i in range(N2):
        tree2.append([-1, -1])

    r1 = -1
    for i in range(N1):
        if parent1[i] == -1:
            r1 = i
        else:
            if child1[i] == 0:
                tree1[parent1[i]][0] = i
            elif child1[i] == 1:
                tree1[parent1[i]][1] = i

    r2 = -1
    for i in range(N2):
        if parent2[i] == -1:
            r2 = i
        else:
            if child2[i] == 0:
                tree2[parent2[i]][0] = i
            elif child2[i] == 1:
                tree2[parent2[i]][1] = i

    root1 = buildTree(r1, key1, tree1)
    root2 = buildTree(r2, key2, tree2)

    root = mergeTwoBSTs(root1, root2)
    height = Height()

    if isBalanced(root, height):
        inOrderTraversal(root, f)
    else:
        f.write('Returned tree is not height balanced\n')

    f.close()

'''
OTHER SOLUTION
import java.util.*;
import java.io.*;

/*
Solution with O(NlogN) time complexity
*/

public class other_solution {

    /**
     * Node class of the BST
     */
    static class Node{

        Node left;
        Node right;
        int key;
        
        Node(int key) {
            this.left = null;
            this.right = null;
            this.key = key;
        }
        
    }
    
    
//  =========================================== start ==================================================
    /**
     * Function to merge two BSTs
     * @param root1 root node of the 1st BST
     * @param root2 root node of the 2nd BST
     * @return merged BST
     */
    static Node mergeTwoBSTs(Node root1, Node root2) {
        
        AVLTree tree = new AVLTree();
        
        addNodes(root1, tree);
        addNodes(root2, tree);
        
        return getFromAVLNode(tree.root);
    }
    
    /**
     * Add nodes from BST to AVL tree by in-order traversal of the tree
     * @param temp current node of the BST
     * @param tree AVL tree 
     */
    static void addNodes(Node temp, AVLTree tree) {
        if(temp == null)
            return;
        addNodes(temp.left, tree);
        tree.root = tree.insert(tree.root, temp.key);
        addNodes(temp.right, tree);
    }
    
    /**
     * AVL tree is self height balancing BST but it contains height in its node,
     * so need to convert it into node without height
     * @param root current node of the AVL tree
     * @return 
     */
    static Node getFromAVLNode(AVLTree.Node root) {
        if(root == null)
            return null;
        Node temp = new Node(root.key);
        temp.left = getFromAVLNode(root.left);
        temp.right = getFromAVLNode(root.right);
        
        return temp;
    }
    
    /**
     * self height balancing BST - AVLTREE
     */
    static class AVLTree {
        
        class Node { 
            int key, height; 
            Node left, right; 

            Node(int d) { 
                key = d; 
                height = 1; 
            } 
        } 
        
        Node root; 
        int height(Node N) { 
            if (N == null) 
                return 0; 

            return N.height; 
        } 

        /**
         * Function to right rotate subtree rooted with y
         * @param y
         * @return balanced subtree
         */
        Node rightRotate(Node y) { 
            
            Node x = y.left; 
            Node T2 = x.right; 

            x.right = y; 
            y.left = T2; 

            y.height = Math.max(height(y.left), height(y.right)) + 1; 
            x.height = Math.max(height(x.left), height(x.right)) + 1; 

            return x; 
        }

        /**
         * Function to left rotate subtree rooted with x
         * @param x
         * @return 
         */
        Node leftRotate(Node x) {
            Node y = x.right; 
            Node T2 = y.left; 

            y.left = x; 
            x.right = T2; 

            x.height = Math.max(height(x.left), height(x.right)) + 1; 
            y.height = Math.max(height(y.left), height(y.right)) + 1; 

            return y; 
        }
        
        int getBalance(Node N) {
            if (N == null) 
                return 0; 

            return height(N.left) - height(N.right); 
        }

        Node insert(Node node, int key) { 

            if (node == null) 
                return (new Node(key)); 

            if (key <= node.key) 
                node.left = insert(node.left, key); 
            else
                node.right = insert(node.right, key);

            node.height = 1 + Math.max(height(node.left), 
                                  height(node.right)); 

            int balance = getBalance(node); 

            // If this node becomes unbalanced, then there 4 cases
            // Left Left Case 
            if (balance > 1 && key <= node.left.key) 
                return rightRotate(node); 

            // Right Right Case 
            if (balance < -1 && key > node.right.key) 
                return leftRotate(node); 

            // Left Right Case 
            if (balance > 1 && key >= node.left.key) { 
                node.left = leftRotate(node.left); 
                return rightRotate(node); 
            }

            // Right Left Case 
            if (balance < -1 && key < node.right.key) { 
                node.right = rightRotate(node.right); 
                return leftRotate(node); 
            }

            return node; 
        }
    }
    
//  =========================================== end ==================================================
    
    static class Height {
        int height;
    }
    /**
     * Check whether tree rooted at temp node is balanced or not
     * @param temp current node
     * @param height current node height
     * @return tree is balanced or not
     */
    static boolean isBalanced(Node temp, Height height) {
        if(temp == null) 
            return true;
        
        Height lh = new Height();
        Height rh = new Height();
        
        boolean l = isBalanced(temp.left, lh);
        boolean r = isBalanced(temp.right, rh);
        
        height.height = Math.max(lh.height, rh.height) + 1;
        
        if(Math.abs(lh.height - rh.height) <= 1 && l && r)
            return true;
        return false;
    }
    
    static Node buildTree(int idx, int[] key, int[][] tree) {
        Node root = new Node(key[idx]);
        if(tree[idx][0] != -1) {
            root.left = buildTree(tree[idx][0], key, tree);
        }
        if(tree[idx][1] != -1) {
            root.right = buildTree(tree[idx][1], key, tree);
        }
        return root;
    }
    
    /**
     * It stores Inorder traversal in the list
     * @param temp current node for traversal
     * @param list list to keep traversal
     */
    static void inOrderTraversal(Node temp, ArrayList<Integer> list) {
        if(temp == null)
            return;
        inOrderTraversal(temp.left, list);
        list.add(temp.key);
        inOrderTraversal(temp.right, list);
    }
    
    static void solve() throws FileNotFoundException{
        
        InputReader in;
        PrintWriter out;

//        in = new InputReader(new FileInputStream("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\sample_test_cases_input.txt"));
//        out = new PrintWriter("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\sample_test_cases_expected_output.txt");
        
        in = new InputReader(new FileInputStream("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\handmade_test_cases_input.txt"));
//        out = new PrintWriter("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\handmade_test_cases_expected_output.txt");
        
//        in = new InputReader(new FileInputStream("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\generated_medium_test_cases_input.txt"));
//        out = new PrintWriter("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\generated_medium_test_cases_expected_output.txt");
        
//        in = new InputReader(new FileInputStream("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\generated_big_test_cases_input.txt"));
//        out = new PrintWriter("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\generated_big_test_cases_expected_output.txt");

        out = new PrintWriter(System.out);
        
        int t = in.nextInt();
        int maxn = 100001;
        int[] parent1 = new int[maxn];
        int[] child1 = new int[maxn];
        int[] key1 = new int[maxn];
        int[] parent2 = new int[maxn];
        int[] child2 = new int[maxn];
        int[] key2 = new int[maxn];
        
        while(t-- > 0) {
            int N1 = in.nextInt();
            for(int i = 0; i < N1; i++)
                parent1[i] = in.nextInt();
            for(int i = 0; i < N1; i++)
                child1[i] = in.nextInt();
            for(int i = 0; i < N1; i++)
                key1[i] = in.nextInt();
            
            int N2 = in.nextInt();
            for(int i = 0; i < N2; i++)
                parent2[i] = in.nextInt();
            for(int i = 0; i < N2; i++)
                child2[i] = in.nextInt();
            for(int i = 0; i < N2; i++)
                key2[i] = in.nextInt();
            
            int[][] tree1 = new int[N1][2];
            int[][] tree2 = new int[N2][2];
            
            for(int i = 0; i < N1; i++)
                tree1[i][0] = tree1[i][1] = -1;
            
            for(int i = 0; i < N2; i++)
                tree2[i][0] = tree2[i][1] = -1;

            int r1 = -1;
            for(int i = 0; i < N1; i++) {
                if(parent1[i] == -1)
                    r1 = i;
                else{
                    if(child1[i] == 0) {
                        tree1[parent1[i]][0] = i;
                    }
                    else if(child1[i] == 1) {
                        tree1[parent1[i]][1] = i;
                    }
                }
            }
            
            int r2 = -1;
            for(int i = 0; i < N2; i++) {
                if(parent2[i] == -1)
                    r2 = i;
                else{
                    if(child2[i] == 0) {
                        tree2[parent2[i]][0] = i;
                    }
                    else if(child2[i] == 1) {
                        tree2[parent2[i]][1] = i;
                    }
                }
            }
            
            Node root1 = buildTree(r1, key1, tree1);
            Node root2 = buildTree(r2, key2, tree2);
            
            Node root = mergeTwoBSTs(root1, root2);

            if(isBalanced(root, new Height())) {
                ArrayList<Integer> list = new ArrayList<>();
                inOrderTraversal(root, list);
                for(int ele: list)
                    out.println(ele);
            }
            else {
                out.println("Returned tree is not height balanced");
            }
        }
            
        out.close();
    }
    
    public static void main(String[] args) {
        
        new Thread(null ,new Runnable(){
            public void run()
            {
                try{
                    solve();
                } catch(Exception e){
                    e.printStackTrace();
                }
            }
        },"1",1<<26).start();
        
    }
    
    static void debug(Object... o) {
        System.out.println(Arrays.deepToString(o));
    }

    /**
     * InputReader class for fast-IO
     */
    static class InputReader
    {

        private final InputStream stream;
        private final byte[] buf = new byte[8192];
        private int curChar, snumChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream)
        {
                this.stream = stream;
        }

        public int snext()
        {
                if (snumChars == -1)
                        throw new InputMismatchException();
                if (curChar >= snumChars)
                {
                        curChar = 0;
                        try
                        {
                                snumChars = stream.read(buf);
                        } catch (IOException e)
                        {
                                throw new InputMismatchException();
                        }
                        if (snumChars <= 0)
                                return -1;
                }
                return buf[curChar++];
        }

        public int nextInt()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                int sgn = 1;
                if (c == '-')
                {
                        sgn = -1;
                        c = snext();
                }
                int res = 0;
                do
                {
                        if (c < '0' || c > '9')
                                throw new InputMismatchException();
                        res *= 10;
                        res += c - '0';
                        c = snext();
                } while (!isSpaceChar(c));
                return res * sgn;
        }

        public long nextLong()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                int sgn = 1;
                if (c == '-')
                {
                        sgn = -1;
                        c = snext();
                }
                long res = 0;
                do
                {
                        if (c < '0' || c > '9')
                                throw new InputMismatchException();
                        res *= 10;
                        res += c - '0';
                        c = snext();
                } while (!isSpaceChar(c));
                return res * sgn;
        }

        public int[] nextIntArray(int n)
        {
                int a[] = new int[n];
                for (int i = 0; i < n; i++)
                {
                        a[i] = nextInt();
                }
                return a;
        }

        public long[] nextLongArray(int n)
        {
                long a[] = new long[n];
                for (int i = 0; i < n; i++)
                {
                        a[i] = nextLong();
                }
                return a;
        }

        public String readString()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                StringBuilder res = new StringBuilder();
                do
                {
                        res.appendCodePoint(c);
                        c = snext();
                } while (!isSpaceChar(c));
                return res.toString();
        }

        public String nextLine()
        {
                int c = snext();
                while (isSpaceChar(c))
                        c = snext();
                StringBuilder res = new StringBuilder();
                do
                {
                        res.appendCodePoint(c);
                        c = snext();
                } while (!isEndOfLine(c));
                return res.toString();
        }

        public boolean isSpaceChar(int c)
        {
                if (filter != null)
                        return filter.isSpaceChar(c);
                return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private boolean isEndOfLine(int c)
        {
                return c == '\n' || c == '\r' || c == -1;
        }

        public interface SpaceCharFilter
        {
                public boolean isSpaceChar(int ch);
        }

    }
}
'''
'''
OPTIMAL SOLUTION
import java.util.*;
import java.io.*;

/*
Solution with O(N1 + N2) time complexity
*/

public class optimal_solution {

    /**
     * Node class of the BST
     */
    static class Node{

        Node left;
        Node right;
        int key;
        
        Node(int key) {
            this.left = null;
            this.right = null;
            this.key = key;
        }
        
    }
    
    static class Height {
        int height;
    }
    
//  =========================================== start ==================================================
    /**
     * Function to merge two BSTs
     * @param root1 root node of the 1st BST
     * @param root2 root node of the 2nd BST
     * @return merged BST
     */
    static Node mergeTwoBSTs(Node root1, Node root2) {

        ArrayList<Integer> list1 = new ArrayList<>();
        inOrderTraversal(root1, list1); // in-opder traversal for 1st tree

        ArrayList<Integer> list2 = new ArrayList<>();
        inOrderTraversal(root2, list2); // in-opder traversal for 2nd tree
        
        ArrayList<Integer> list = mergeLists(list1, list2); // merge two sorted lists
        
        Node root = build(list, 0, list.size() - 1); // build balanced BST using sorted list
        
        return root;
    }
    
    /**
     * Merge two sorted list
     * @param list1 1st sorted list
     * @param list2 2nd sorted list
     * @return merged sorted list
     */
    static ArrayList<Integer> mergeLists(ArrayList<Integer> list1, ArrayList<Integer> list2) {
        ArrayList<Integer> list = new ArrayList<>();
        int i = 0;
        int j = 0;
        
        // append smallest integer from the given list untill one list is finished
        while(i < list1.size() && j < list2.size()) {
            if(list1.get(i) <= list2.get(j) + 0)
                list.add(list1.get(i++));
            else
                list.add(list2.get(j++));
        }
        // append rest of the integeres
        while(i < list1.size())
            list.add(list1.get(i++));
        while(j < list2.size())
            list.add(list2.get(j++));

        return list;
    }
    
    /**
     * It stores Inorder traversal in the list
     * @param temp current node for traversal
     * @param list list to keep traversal
     */
    static void inOrderTraversal(Node temp, ArrayList<Integer> list) {
        if(temp == null)
            return;
        inOrderTraversal(temp.left, list);
        list.add(temp.key);
        inOrderTraversal(temp.right, list);
    }
    
    /**
     * It builds balanced BST from the keys between index l and r
     * @param list it is sorted list
     * @param l left index of the list
     * @param r right index of the list
     * @return Balanced BST
     */
    static Node build(ArrayList<Integer> list, int l, int r) {
        
        if(l > r)
            return null;
        if(l == r)
            return new Node(list.get(l));
        
        /* Keep middle element from l to r as current root node and find left subtree in (l to mid - 1)
            and right subtree in (mid + 1 to r)
        */
        int mid = (l + r) >> 1;
        Node temp  = new Node(list.get(mid));
        temp.left = build(list, l, mid - 1);
        temp.right = build(list, mid + 1, r);
        return temp;
    }
    
//  =========================================== end ==================================================
    
    /**
     * Check whether tree rooted at temp node is balanced or not
     * @param temp current node
     * @param height current node height
     * @return tree is balanced or not
     */
    static boolean isBalanced(Node temp, Height height) {
        if(temp == null) 
            return true;
        
        Height lh = new Height();
        Height rh = new Height();
        
        boolean l = isBalanced(temp.left, lh);
        boolean r = isBalanced(temp.right, rh);
        
        height.height = Math.max(lh.height, rh.height) + 1;
        
        if(Math.abs(lh.height - rh.height) <= 1 && l && r)
            return true;
        return false;
    }
    
    static Node buildTree(int idx, int[] key, int[][] tree) {
        Node root = new Node(key[idx]);
        if(tree[idx][0] != -1) {
            root.left = buildTree(tree[idx][0], key, tree);
        }
        if(tree[idx][1] != -1) {
            root.right = buildTree(tree[idx][1], key, tree);
        }
        return root;
    }
    
    static void solve() throws FileNotFoundException{
        
        InputReader in;
        PrintWriter out;
//        in = new InputReader(new FileInputStream("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\sample_test_cases_input.txt"));
//        out = new PrintWriter("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\sample_test_cases_expected_output.txt");
        
        in = new InputReader(new FileInputStream("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\handmade_test_cases_input.txt"));
        out = new PrintWriter("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\handmade_test_cases_expected_output.txt");
        
//        in = new InputReader(new FileInputStream("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\generated_medium_test_cases_input.txt"));
//        out = new PrintWriter("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\generated_medium_test_cases_expected_output.txt");
        
//        in = new InputReader(new FileInputStream("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\generated_big_test_cases_input.txt"));
//        out = new PrintWriter("Z:\\Project\\ProblemSettingUmangU\\Merge_Two_BSTs\\test_cases\\generated_big_test_cases_expected_output.txt");

//        out = new PrintWriter(System.out);

        int t = in.nextInt();
        int maxn = 100001;
        int[] parent1 = new int[maxn];
        int[] child1 = new int[maxn];
        int[] key1 = new int[maxn];
        int[] parent2 = new int[maxn];
        int[] child2 = new int[maxn];
        int[] key2 = new int[maxn];
        
        while(t-- > 0) {
            int N1 = in.nextInt();
            for(int i = 0; i < N1; i++)
                parent1[i] = in.nextInt();
            for(int i = 0; i < N1; i++)
                child1[i] = in.nextInt();
            for(int i = 0; i < N1; i++)
                key1[i] = in.nextInt();
            
            int N2 = in.nextInt();
            for(int i = 0; i < N2; i++)
                parent2[i] = in.nextInt();
            for(int i = 0; i < N2; i++)
                child2[i] = in.nextInt();
            for(int i = 0; i < N2; i++)
                key2[i] = in.nextInt();
            
            int[][] tree1 = new int[N1][2];
            int[][] tree2 = new int[N2][2];
            
            for(int i = 0; i < N1; i++)
                tree1[i][0] = tree1[i][1] = -1;
            
            for(int i = 0; i < N2; i++)
                tree2[i][0] = tree2[i][1] = -1;

            int r1 = -1;
            for(int i = 0; i < N1; i++) {
                if(parent1[i] == -1)
                    r1 = i;
                else{
                    if(child1[i] == 0) {
                        tree1[parent1[i]][0] = i;
                    }
                    else if(child1[i] == 1) {
                        tree1[parent1[i]][1] = i;
                    }
                }
            }
            
            int r2 = -1;
            for(int i = 0; i < N2; i++) {
                if(parent2[i] == -1)
                    r2 = i;
                else{
                    if(child2[i] == 0) {
                        tree2[parent2[i]][0] = i;
                    }
                    else if(child2[i] == 1) {
                        tree2[parent2[i]][1] = i;
                    }
                }
            }
            
            Node root1 = buildTree(r1, key1, tree1);
            Node root2 = buildTree(r2, key2, tree2);
            
            Node root = mergeTwoBSTs(root1, root2);

            if(isBalanced(root, new Height())) {
                ArrayList<Integer> list = new ArrayList<>();
                inOrderTraversal(root, list);
                for(int ele: list)
                    out.println(ele);
            }
            else {
                out.println("Returned tree is not height balanced");
            }
        }
            
        out.close();
    }
    
    public static void main(String[] args) {
        
        new Thread(null ,new Runnable(){
            public void run()
            {
                try{
                    solve();
                } catch(Exception e){
                    e.printStackTrace();
                }
            }
        },"1",1<<26).start();
        
    }
    
    static void debug(Object... o) {
        System.out.println(Arrays.deepToString(o));
    }

    /**
     * InputReader class for fast-IO
     */
    static class InputReader
    {

        private final InputStream stream;
        private final byte[] buf = new byte[8192];
        private int curChar, snumChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream)
        {
                this.stream = stream;
        }

        public int snext()
        {
                if (snumChars == -1)
                        throw new InputMismatchException();
                if (curChar >= snumChars)
                {
                        curChar = 0;
                        try
                        {
                                snumChars = stream.read(buf);
                        } catch (IOException e)
                        {
                                throw new InputMismatchException();
                        }
                        if (snumChars <= 0)
                                return -1;
                }
                return buf[curChar++];
        }

        public int nextInt()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                int sgn = 1;
                if (c == '-')
                {
                        sgn = -1;
                        c = snext();
                }
                int res = 0;
                do
                {
                        if (c < '0' || c > '9')
                                throw new InputMismatchException();
                        res *= 10;
                        res += c - '0';
                        c = snext();
                } while (!isSpaceChar(c));
                return res * sgn;
        }

        public long nextLong()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                int sgn = 1;
                if (c == '-')
                {
                        sgn = -1;
                        c = snext();
                }
                long res = 0;
                do
                {
                        if (c < '0' || c > '9')
                                throw new InputMismatchException();
                        res *= 10;
                        res += c - '0';
                        c = snext();
                } while (!isSpaceChar(c));
                return res * sgn;
        }

        public int[] nextIntArray(int n)
        {
                int a[] = new int[n];
                for (int i = 0; i < n; i++)
                {
                        a[i] = nextInt();
                }
                return a;
        }

        public long[] nextLongArray(int n)
        {
                long a[] = new long[n];
                for (int i = 0; i < n; i++)
                {
                        a[i] = nextLong();
                }
                return a;
        }

        public String readString()
        {
                int c = snext();
                while (isSpaceChar(c))
                {
                        c = snext();
                }
                StringBuilder res = new StringBuilder();
                do
                {
                        res.appendCodePoint(c);
                        c = snext();
                } while (!isSpaceChar(c));
                return res.toString();
        }

        public String nextLine()
        {
                int c = snext();
                while (isSpaceChar(c))
                        c = snext();
                StringBuilder res = new StringBuilder();
                do
                {
                        res.appendCodePoint(c);
                        c = snext();
                } while (!isEndOfLine(c));
                return res.toString();
        }

        public boolean isSpaceChar(int c)
        {
                if (filter != null)
                        return filter.isSpaceChar(c);
                return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private boolean isEndOfLine(int c)
        {
                return c == '\n' || c == '\r' || c == -1;
        }

        public interface SpaceCharFilter
        {
                public boolean isSpaceChar(int ch);
        }

    }
}
'''
