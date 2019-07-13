'''
Largest BST
Problem Statement:
Given a binary tree, find the largest Binary Search Tree (BST), where largest means BST with largest number of nodes in
 it. The largest BST must include all of its descendants.
Input/Output Format For The Function:
Input format:
There is only one argument named root denoting the root of the input tree.
Output format:
Return an integer denoting the size of the largest BST.
Input/Output Format For The Custom Input:
Input Format:
line number 1: <noOfNodes> denoting number of nodes of the tree.
line number 2: <noOfNdoes space seprated integers> denoting the values of the nodes. Please make sure there are not leading
 or trailing spaces and between two integers there must be a single space.
line number 3: <rootIndex> denoting the root of the tree. value of rootIndex must be between -1 to noOfNodes-1
line number 4: <noOfEdges> denoting the number of edges of the tree
next noOfEdges line: <parentNodeIndex><space><childNodeIndex><space><leftOrRightFlag>
Here <parentNodeIndex> and <childNodeIndex> are the node indexes ranging from 0 to noOfNodes-1. <leftOrRighFlag> is either
 "L" or "R" (without quotes) denoting the left or right child where "L" stands for left child and "R" stands for right child.

Raw input of sample:
7
1 3 5 2 4 6 7
0
6
0 1 L
0 2 R
1 3 L
1 4 R
2 5 L
2 6 R

Output Format:
An integer denoting the size of the largest BST.
Raw output of sample:
3

Constraints:
0 <= number of nodes <= 100000
1 <= values stored in the nodes <= 10^9

Sample Test Case:
Sample Input:
https://i.imgur.com/1xINvv4.png

Sample Output:
3

Explanation:
In the input tree, left subtree of node 1 is a BST. It has 3 nodes and this is the largest BST. So, result is 3.
Tree node structure:
Class TreeNode {
    int val;
    TreeNode left_ptr;
    TreeNode right_ptr;
}
'''
import sys
from collections import deque

sys.setrecursionlimit(101000)


class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr


class BinaryTree():
    class Edge():
        def __init__(self, parentNodeIndex=None, childNodeIndex=None, leftRightFlag=None):
            self.BinaryTree = BinaryTree
            self.parentNodeIndex = parentNodeIndex
            self.childNodeIndex = childNodeIndex
            self.leftRightFlag = leftRightFlag

    def __init__(self):
        self.root = None
        self.noOfNodes = 0
        self.noOfEdges = 0
        self.rootIndex = -1
        self.nodeValues = []
        self.edges = []

    def readRawValues(self):
        self.noOfNodes = int(input())
        if self.noOfNodes > 0:
            nodeValueString = input().split(' ')
            for val in nodeValueString:
                self.nodeValues.append(int(val))

        self.rootIndex = int(input())
        self.noOfEdges = int(input())
        for i in range(self.noOfEdges):
            edgeInput = input().split(' ')
            self.edges.append(self.Edge(int(edgeInput[0]), int(edgeInput[1]), edgeInput[2]))

    def buildFromRawValues(self):
        if self.noOfNodes == 0:
            root = None
            return
        nodes = []
        for i in range(self.noOfNodes):
            nodes.append(TreeNode(self.nodeValues[i]))

        for i in range(self.noOfEdges):
            if self.edges[i].leftRightFlag == "L":
                nodes[self.edges[i].parentNodeIndex].left_ptr = nodes[self.edges[i].childNodeIndex]
            else:
                nodes[self.edges[i].parentNodeIndex].right_ptr = nodes[self.edges[i].childNodeIndex]

        self.root = nodes[self.rootIndex]


def readBinaryTree():
    inputBinaryTree = BinaryTree()
    inputBinaryTree.readRawValues()
    inputBinaryTree.buildFromRawValues()
    return inputBinaryTree.root


# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def findLargestBST(root):
    pass


def main():
    root = readBinaryTree()
    result = findLargestBST(root)
    print(result)

main()

'''
We have provided two solution for this problem. other_solution.cpp is the brute force solution and optimal_solution.cpp
 is the optimal solution.
1.other_solution.cpp:
The problem asked to find out the largest BST from the given tree. As we know, in a tree having N nodes there are N subtrees,
 so there can be N BST. We have to find out the size of the largest one. In this solution we check if a subtree is a BST
 or not. If it is a BST, counted the number of nodes in the subtree. Let’s say there are K subtree which are BST also. We
 know size of the K BST. Maximum of those size is our desired result.
Time complexity:
O(N^2)
Auxiliary space:
O(N^2) because of using two recursion.
Space complexity:
Including input, O(N^2)



2.optimal_solution.cpp:
In this solution we first checked if the left subtree and right subtrees are BST or not. There are few cases. Cases are
 described below:
    1. Leaf node: Leaf node is a valid BST
    2. Both subtrees are valid BST:
If root’s value is between left child value and right child
 value, then subtree rooted at current tree is a valid, otherwise not.
    1. One of the subtree is not a valid BST:
Subtree rooted at current tree is not a valid BST.
In each case, we few parameters of current subtree. To make this process easier, we used a class which held 5 values. These
 are:
    1. mn: Minimum node value of current subtree
    2. mx: Maximum node value of current subtree
    3. isBST: true or false to denote whether current subtree is a valid BST or not
    4. size: Number of nodes in current subtree
    5. mxSize: Size of the largest BST in current subtree
    
Please note that, when isBST is false, variables mn, mx and size are insignificant. The mxSize variables stores
 the result we are expecting.
Time complexity:
O(N)
Auxiliary space:
O(N) because of using two recursion.
Space complexity:
Including input, O(N)
'''
'''
#include <bits/stdc++.h>

using namespace std;

class TreeNode{
public:
    int val;
    TreeNode* left_ptr;
    TreeNode* right_ptr;

    TreeNode(int _val){
        val = _val;
        left_ptr = NULL;
        right_ptr = NULL;
    }
};

class BinaryTree{
public:
    class Edge{
    public:
        int parentNodeIndex;
        int childNodeIndex;
        string leftRightFlag;

        Edge(){}

        Edge(int _parentNodeIndex, int _childNodeIndex, string _leftRightFlag){
            parentNodeIndex = _parentNodeIndex;
            childNodeIndex = _childNodeIndex;
            leftRightFlag = _leftRightFlag;
        }
    };

    int noOfNodes;
    vector<int> nodeValues;
    vector<TreeNode*> nextRightNodes;
    int rootIndex;
    int noOfEdges;
    vector<Edge> edges;
    TreeNode* root;

    BinaryTree(){
        noOfNodes = 0;
        nodeValues.clear();
        rootIndex = -1;
        noOfEdges = 0;
        edges.clear();
        nextRightNodes.clear();
        root = NULL;
    }

    void readRawValues(ifstream &cin){
        cin >> noOfNodes;
        nodeValues.assign(noOfNodes, 0);
        for(int i = 0; i < noOfNodes; i++){
            cin >> nodeValues[i];
        }

        cin >> rootIndex;

        Edge tempEdge;
        cin >> noOfEdges;
        edges.assign(noOfEdges, tempEdge);
        for(int i = 0; i < noOfEdges; i++){
            cin >> edges[i].parentNodeIndex
                >> edges[i].childNodeIndex 
                >> edges[i].leftRightFlag;
        }
    }

    void buildFromRawValues(){
        if(noOfNodes == 0){
            root = NULL;
            return;
        }

        vector<TreeNode*> nodes(noOfNodes);
        for(int i = 0; i < noOfNodes; i++){
            nodes[i] = new TreeNode(nodeValues[i]);
        }

        for(int i = 0; i < noOfEdges; i++){
            if(edges[i].leftRightFlag == "L"){
                nodes[edges[i].parentNodeIndex]->left_ptr = nodes[edges[i].childNodeIndex];
            }else{
                nodes[edges[i].parentNodeIndex]->right_ptr = nodes[edges[i].childNodeIndex];
            }
        }

        root = nodes[rootIndex];
        return;
    }

    void validateInput(){
        if(noOfNodes == 0){
            assert(noOfEdges == 0);
            return;
        }
        assert(noOfNodes == noOfEdges+1);
        int indegree[noOfNodes], outDegree[noOfNodes], leftChild[noOfNodes], rightChild[noOfNodes];
        for(int i=0;i<noOfNodes;i++){
            indegree[i] = 0;
            outDegree[i] = 0;
            leftChild[i] = 0;
            rightChild[i] = 0;
        }
        for(int i=0;i<noOfEdges;i++){
            outDegree[edges[i].parentNodeIndex]++;
            indegree[edges[i].childNodeIndex]++;
            
            if(edges[i].leftRightFlag == "L"){
                leftChild[edges[i].parentNodeIndex]++;
            }
            else{
                rightChild[edges[i].parentNodeIndex]++;
            }
        }
        int rootCount = 0;
        int root = -1;
        for(int i=0;i<noOfNodes;i++){
            assert(indegree[i]<=1);
            assert(outDegree[i]<=2);
            assert(leftChild[i]<=1);
            assert(rightChild[i]<=1);
            if(indegree[i]==0){
                rootCount++;
                root = i;
            }
        }
        assert(rootCount == 1);
        assert(root == rootIndex);
    }

    void considerEdge(
        string lOrR, TreeNode* parent, TreeNode* child, 
        unordered_map<TreeNode*, int>& nodeToId, int& id, bool& edge_creates_cycle
    ){
        if (child){
            if (nodeToId.find(child) == nodeToId.end()){
                nodeToId[child] = id++;
                nodeValues.push_back(child->val);
            } else {
                edge_creates_cycle = true;
                cerr << "Cycle detected in the tree. Cycle contains the edge: " 
                     << nodeToId[parent] << " " << nodeToId[child] 
                     << " " << lOrR << endl;
            }
            edges.push_back(Edge(nodeToId[parent], nodeToId[child], lOrR));
        }
    }

    void getNodeValuesAndEdges(
        TreeNode* root, unordered_map<TreeNode*, int>& nodeToId, int& id
    ){
        if(root == NULL){
            return;
        }

        bool left_edge_creates_cycle = false;
        bool right_edge_creates_cycle = false;

        considerEdge(
            "L", root, root->left_ptr, 
            nodeToId, id, left_edge_creates_cycle
        );
        considerEdge(
            "R", root, root->right_ptr,
            nodeToId, id, right_edge_creates_cycle
        );

        if (left_edge_creates_cycle == false){
            getNodeValuesAndEdges(root->left_ptr, nodeToId, id);
        }
        if (right_edge_creates_cycle == false){
            getNodeValuesAndEdges(root->right_ptr, nodeToId, id);
        }
    }

    void populateRawValuesFromTree(){
        noOfNodes = 0;
        nodeValues.clear();
        rootIndex = -1;
        noOfEdges = 0;
        edges.clear();
        nextRightNodes.clear();

        if (root != NULL){
            int id = 0;
            unordered_map<TreeNode*, int> nodeToId;

            rootIndex = id;  // That is 0.
            nodeToId[root] = id++;
            nodeValues.push_back(root->val);

            getNodeValuesAndEdges(root, nodeToId, id);
            noOfNodes = nodeValues.size();
            noOfEdges = edges.size();
        }
    }

    void writeRawValues(ofstream &cout){
        cout << noOfNodes << endl;
        for(int i = 0; i < noOfNodes; i++){
            if(i){
                cout << " ";
            }
            cout << nodeValues[i];
        }

        if (noOfNodes > 0){
            cout << endl;
        }

        cout << rootIndex << endl;

        cout << noOfEdges << endl;
        for(int i = 0; i < noOfEdges; i++){
            cout << edges[i].parentNodeIndex 
                 << " " << edges[i].childNodeIndex
                 << " " << edges[i].leftRightFlag
                 << endl;
        }
    }
};

TreeNode* readBinaryTree(ifstream &fin){
    BinaryTree input_binary_tree;
    input_binary_tree.readRawValues(fin);
    input_binary_tree.validateInput();
    input_binary_tree.buildFromRawValues();
    return input_binary_tree.root;
}

void printBinaryTree(TreeNode* resultRoot, ofstream &fout){
    BinaryTree output_binary_tree;
    output_binary_tree.root = resultRoot;
    output_binary_tree.populateRawValuesFromTree();
    output_binary_tree.writeRawValues(fout);
}

// ============================ Start ============================

/*
 * Complete the function below.
 */

class BSTInfo{
public:
    int mn;
    int mx;
    bool isBST;
    int size;
    int mxSize;

    BSTInfo(){
        mn = -1000000009;
        mx = 1000000009;
        isBST = true;
        size = 0;
        mxSize = 0;
    }
};

BSTInfo findLargestBSTHelper(TreeNode *root){
    BSTInfo currentTreeInfo;
    if(root == NULL) {
        return currentTreeInfo;
    }
    // Leaf node check
    if(root->left_ptr == NULL && root->right_ptr == NULL){
        currentTreeInfo.mn = root->val;
        currentTreeInfo.mx = root->val;
        currentTreeInfo.size = 1;
        currentTreeInfo.isBST = true;
        currentTreeInfo.mxSize = 1;
    } 
    // Left child is null
    else if(root->left_ptr == NULL){
        BSTInfo rightTreeInfo = findLargestBSTHelper(root->right_ptr);
        if(rightTreeInfo.isBST && root->val<= rightTreeInfo.mn){
            currentTreeInfo.mn = root->val;
            currentTreeInfo.mx = rightTreeInfo.mx;
            currentTreeInfo.size = 1 + rightTreeInfo.size;
            currentTreeInfo.isBST = true;
            currentTreeInfo.mxSize = max(currentTreeInfo.size, rightTreeInfo.mxSize);
        } else {
            currentTreeInfo.isBST = false;
            currentTreeInfo.mxSize = max(1, rightTreeInfo.mxSize);
        }
    } 
    // Right child is null
    else if(root->right_ptr == NULL){
        BSTInfo leftTreeInfo = findLargestBSTHelper(root->left_ptr);
        if(leftTreeInfo.isBST && leftTreeInfo.mx <= root->val){
            currentTreeInfo.mn = leftTreeInfo.mn;
            currentTreeInfo.mx = root->val;
            currentTreeInfo.size = 1 + leftTreeInfo.size;
            currentTreeInfo.isBST = true;
            currentTreeInfo.mxSize = max(currentTreeInfo.size, leftTreeInfo.mxSize);
        } else {
            currentTreeInfo.isBST = false;
            currentTreeInfo.mxSize = max(1, leftTreeInfo.mxSize);
        }
    } 
    // Both child present
    else {
        BSTInfo leftTreeInfo = findLargestBSTHelper(root->left_ptr);
        BSTInfo rightTreeInfo = findLargestBSTHelper(root->right_ptr);
        if(leftTreeInfo.isBST == true && rightTreeInfo.isBST == true && leftTreeInfo.mx <= root->val && root->val <= rightTreeInfo.mn){
            currentTreeInfo.mn = leftTreeInfo.mn;
            currentTreeInfo.mx = rightTreeInfo.mx;
            currentTreeInfo.size = 1 + leftTreeInfo.size + rightTreeInfo.size;
            currentTreeInfo.isBST = true;
            currentTreeInfo.mxSize = max(currentTreeInfo.size, max(leftTreeInfo.mxSize, rightTreeInfo.mxSize));
        } else {
            currentTreeInfo.isBST = false;
            currentTreeInfo.mxSize = max(1,max(leftTreeInfo.mxSize, rightTreeInfo.mxSize));
        }
    }
    return currentTreeInfo;
}

int findLargestBST(TreeNode *root) {
    if(root == NULL){
        return 0;
    }
    BSTInfo result = findLargestBSTHelper(root);
    return result.mxSize;
}

// ============================ End ============================

void solve(string inputFile, string outputFile){
    ifstream fin(inputFile);
    ofstream fout(outputFile);
    cerr<<"Running "<<inputFile<<endl;
    int testCase;
    fin>>testCase;
    for(int i=0;i<testCase;i++){
        cerr<<"Running case number "<<i<<endl;
        TreeNode *root = readBinaryTree(fin);
        int result = findLargestBST(root);
        fout<<result<<endl;
    }
}

int main(){
    solve("..//test_cases//sample_test_cases_input.txt", "..//test_cases//sample_test_cases_expected_output.txt");
    solve("..//test_cases//handmade_test_cases_input.txt", "..//test_cases//handmade_test_cases_expected_output.txt");
    solve("..//test_cases//generated_small_test_cases_input.txt", "..//test_cases//generated_small_test_cases_expected_output.txt");
    solve("..//test_cases//generated_big_test_cases_input.txt", "..//test_cases//generated_big_test_cases_expected_output.txt");
    return 0;
}    
'''



