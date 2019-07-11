'''
Single Value Tree
Problem Statement:
Given a binary tree, find the number of unival subtrees (the unival tree is a tree which has the same
value for every node in it).
Input/Output Format For The Function:
Input Format:
There is only one argument named root denoting the root of the input tree.
Output Format:
Return an integer denoting the number of unival subtrees in a given tree.

Input/Output Format For The Custom Input:
Input Format:
The first line of the input contains an integer noOfNodes, denoting the number of nodes of the tree.
In the second line of the input, it contains noOfNodes integers, denoting the values of the nodes. Please make sure
there are no leading or trailing spaces and between two integers there must be a single space.
In the third line of the input, it contains a single integer rootIndex, denoting the root of the tree. value of
rootIndex must be between 0 to noOfNodes-1.
In the fourth line of the input, it contains a single integer noOfEdges, denoting the number of edges of the tree.
Next noOfNodes-1 lines, each line contains parentNodeIndex, childNodeIndex, leftOrRightFlag separated by space.
Here parentNodeIndex and childNodeIndex are the node indexes ranging from 0 to noOfNodes-1. leftOrRighFlag is either
"L" or "R" (without quotes) denoting the relationship between parent and child, the left or right child where "L"
stands for left child and "R" stands for the right child.

If noOfNodes= 6, values = [5, 5, 5, 5, 5, 5], root_index = 0, noOfEdges=5, tree = [
{Node: 0, LeftChild: 1, RightChild: 2}, {Node: 1, LeftChild: 3, RightChild: 4}, {Node: 2, RightChild: 5}]:

6
5 5 5 5 5 5
0
5
0 1 L
0 2 R
1 3 L
1 4 R
2 5 R

Output Format:
A single integer denoting answer of the problem i.e. the number of unival subtrees in a given tree.

For input, noOfNodes= 6, values = [5, 5, 5, 5, 5, 5], root_index = 0, noOfEdges=5, tree = [
{Node: 0, LeftChild: 1, RightChild: 2}, {Node: 1, LeftChild: 3, RightChild: 4}, {Node: 2, RightChild: 5}],
output will be:
6

Constraints:
0 <= n <= 100000, where n denotes number of nodes of tree.
-1000000000 <= value of node <= 1000000000
0 <= root_index <= n-1 where n denotes number of nodes of tree and root_index denotes root index of tree.
The solution should use only constant extra space.
Sample Test Cases:
Sample Input 1:
6
5 5 5 5 5 5
0
5
0 1 L
0 2 R
1 3 L
1 4 R
2 5 R

Sample Output 1:
6

Explanation 1:
https://i.imgur.com/vSwhEvu.png


See picture above for details. There are 6 nodes i.e. 6 subtrees and for each subtree, value is 5 for each node. Means each subtree of this tree is a
unival tree hence answer will be 6.

Sample Input 2:
7
5 5 5 5 5 4 5
0
6
0 1 L
0 2 R
1 3 L
1 4 R
2 5 L
2 6 R

Sample Output 2:
5

Explanation 2:
https://i.imgur.com/HN5Zopc.png

There are 7 nodes i.e. 7 subtrees. Left subtree has 3 nodes and all nodes values are identical. So, there is 3 single
value tree in the left subtree of the given tree. Right subtree has also 3 nodes. But all values are not identical.
There are two leaves. So, 2 single value tree in the right subtree. As right subtree is not a single value tee, the
whole tree is not a single value tree either.

Tree node structure:
Class TreeNode {
    int val;
    TreeNode left_ptr;
    TreeNode right_ptr;
}
'''

import math
import os
import random
import re
import sys

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
        self.root = None;
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

    def buildFormRawValues(self):
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
    inputBinaryTree.buildFormRawValues()
    return inputBinaryTree.root

# complete the function below

def findSingleValueTrees(root):
    pass


def main():
    root = readBinaryTree()
    result = findSingleValueTrees(root)
    print(result)

main()





'''
We have provided solutions which contain necessary
comments to understand the approach used:
1) other_solution.cpp:
Description:

A tree is unival if all node values are identical. A tree having N nodes have N subtrees. The problem asked to count the
 number of subtrees which are unival. So, for each subtree, we check if it is a unival tree. We iterate through each node
 of the tree and using the isUniValTree function, we check if the subtree rooted at the current node is unival or not. As
 isUniValTree will return 0 and 1 if the tree is not a unival tree and if the tree is unival tree respectively then we will
 add that with count for left subtree and count for the right subtree. For better understanding please have a look at the
 solution.
Time Complexity (assuming that input arguments are already given and excluding time used in the declaration of
 output):
O(n^2) where n denotes the number of nodes.
As we are iterating complete tree and calling function isUniValTree
 function for each node of the tree. As isUniValTree function will take O(n) and we are calling it for each node so, n*O(n)
 → O(n^2). 
Time complexity: 
O(n^2) where n denotes the number of nodes.
As time complexity assuming that input arguments
 are already given and excluding time used in the declaration of output is O(n^2) and to read input arguments it will take
 O(n) as number of nodes are n and there can be n-1 edges, declaration of output will take O(1) hence total complexity will
 be O(n^2) + O(n) + O(1) → O(n^2).
Auxiliary space:
O(n) where n denotes the number of nodes.
As we are calling functions
 in recursion, so in the worst case functional stack can have n number of function calls which is equal to the number of
 nodes of the given tree.
Hence auxiliary space for that is O(n).
Space complexity:
O(n) where n denotes the number of nodes.
As to store given tree it will take O(n) space and auxiliary
 space used is O(n). Hence O(n) + O(n) → O(n).
2) optimal_solution.cpp:
This solution is an optimized version of other_solution.
 In this solution, rather than checking all nodes of a tree, we can decide whether it’s a unival tree or not by checking
 only a few parameters.
These are:
Left subtree is unival subtree.
Right subtree is unival subtree.
Left node value and
 right node value is equal to parent node value.
And there are some predefined definitions:
Null node is unival.
A leaf node is unival.
So, to count the number of unival subtrees, we have to iterate through all the nodes and check if the subtree rooted at
 the current node is unival or not. We can check this using a few conditional statements described above which discard another
 method call used in other_solution.cpp. For better understanding please have a look at the solution.
Time Complexity (assuming that input arguments are already given and excluding time used in the declaration of output):

O(n) where n denotes the number of nodes.
As we are not checking every subtree that whether that tree is a unival tree or not but we are using information already
 calculated for left subtree and right subtree to decide whether subtree represented by a node is a unival tree or not.
 Hence it will just iterate tree once and so time complexity will be O(n).
Time complexity:
O(n) where n denotes the number of nodes.
As time complexity assuming that input arguments are already given and excluding
 time used in the declaration of output is O(n) and to read input arguments it will take O(n) as number of nodes are n and
 there can be n-1 edges, declaration of output will take O(1) hence total complexity will be O(n) + O(n) + O(1) → O(n).

Auxiliary space:
O(n) where n denotes the number of nodes.
As we are calling functions in recursion, so in the worst case functional stack can have n number of function calls which
 is equal to the number of nodes of the given tree.
Hence auxiliary space for that is O(n).
Space complexity:
O(n) where n denotes the number of nodes.
As to store given tree it will take O(n) space and auxiliary space used is O(n). Hence O(n) + O(n) → O(n).
'''

'''
OPTIMAL

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
        int indegree[noOfNodes], outDegree[noOfEdges], leftChild[noOfNodes], rightChild[noOfNodes];
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
            if(indegree[i]>1){
                cerr<<"Here "<<i<<" "<<indegree[i]<<" "<<rootIndex<<endl;
            }
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
};

TreeNode* readBinaryTree(ifstream &fin){
    BinaryTree input_binary_tree;
    input_binary_tree.readRawValues(fin);
    input_binary_tree.validateInput();
    input_binary_tree.buildFromRawValues();
    return input_binary_tree.root;
}

// ============================ Start ============================

int findSingleValueTreesHelper(TreeNode *root, bool &isUniVal){
    if(root == NULL){
        isUniVal = true; // null tree is unival
        return 0;
    }
    // leaf node
    if(root->left_ptr == NULL && root->right_ptr == NULL){
        isUniVal = true; // single noded tree is unival
        return 1;
    }
    // true if left subtree is unival. Initially assumed it is not
    bool isLeftSubTreeUnival = false;
    // count unival subtree in left subtree
    int leftSubTreeUnivalCount = findSingleValueTreesHelper(root->left_ptr, isLeftSubTreeUnival);
    // true if right subtree is unival. Initially assumed it is not
    bool isRightSubTreeUnival = false;
    // count unival subtree in left subtree
    int rightSubTreeUnivalCount = findSingleValueTreesHelper(root->right_ptr, isRightSubTreeUnival);

    // One of the subtree is not unival
    if(!isLeftSubTreeUnival || !isRightSubTreeUnival) {
        return leftSubTreeUnivalCount + rightSubTreeUnivalCount;
    } 
    else {
        // left node value is not equal to parent node value
        if(root->left_ptr!= NULL && root->left_ptr->val != root->val) {
            return leftSubTreeUnivalCount + rightSubTreeUnivalCount;
        }// left node value is not equal to parent node value
        else if(root->right_ptr != NULL && root->right_ptr->val != root->val) {
            return leftSubTreeUnivalCount + rightSubTreeUnivalCount;
        }
        // both node value is equal to parent node value if not null
        else{
            isUniVal = true;
            return 1 + leftSubTreeUnivalCount + rightSubTreeUnivalCount;
        }
    }
}

int findSingleValueTrees(TreeNode* root){
    // empty or null tree check
    if(root==NULL){
        return 0;
    }
    bool isUniVal = false;
    return findSingleValueTreesHelper(root, isUniVal);
}

// ============================ End ============================

void solve(string inputFile, string outputFile){
    ifstream fin(inputFile);
    ofstream fout(outputFile);
    cerr<<"Running "<<inputFile<<endl;
    int testCase;
    fin>>testCase;
    for(int i=0;i<testCase;i++){
        cerr<<"Running "<<i<<"th test"<<endl;
        TreeNode *root = readBinaryTree(fin);
        int result = findSingleValueTrees(root);
        fout<<result<<endl;
    }
}

int main(){
    solve("..//test_cases//sample_test_cases_input.txt", "..//test_cases//sample_test_cases_expected_output.txt");
    solve("..//test_cases//handmade_test_cases_input.txt", "..//test_cases//handmade_test_cases_expected_output.txt");
    solve("..//test_cases//generated_big_test_cases_input.txt", "..//test_cases//generated_big_test_cases_expected_output.txt");
    return 0;
}
'''
