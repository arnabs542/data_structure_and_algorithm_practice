'''
Tree Iterator
Problem Statement:
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

1. Calling next() will return the next smallest number in the BST.
2. Calling hasNext() should return whether the next element exists.

Both functions should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

[Iterator is a concept in higher level languages like C++ or Java. You probably can tell what it is. If you want to know more, please feel free to Google for the concept.]

Input/Output Format For The Function:
Input format:
There is only one argument named root denoting the root of the input tree.
Output format:

There is nothing to return as a whole. What the given method will do is described below:
Constructor/initializer: Initialize the iterator.
next(): Returns an integer denoting the next node value.
hasNext(): Returns a boolean denoting the next nodes presence.

Input/Output Format For The Custom Input:
Input Format:
line number 1: <noOfNodes> denoting number of nodes of the tree.
line number 2: <noOfNdoes space seprated integers> denoting the values of the nodes. Please make sure there are not leading or trailing spaces and between two integers there must be a single space.
line number 3: <rootIndex> denoting the root of the tree. value of rootIndex must be between -1 to noOfNodes-1
line number 4: <noOfEdges> denoting the number of edges of the tree
next noOfEdges line: <parentNodeIndex><space><childNodeIndex><space><leftOrRightFlag>
Here <parentNodeIndex> and <childNodeIndex> are the node indexes ranging from 0 to noOfNodes-1. <leftOrRighFlag> is either "L" or "R" (without quotes) denoting the left or right child where "L" stands for left child and "R" stands for right child.

Raw input of sample:
3
2 1 3
0
2
0 1 L
0 2 R

Output Format:

Space separated integer denoting the values in iterator order

Raw output of sample:
1 2 3

Constraints:
0 <= number of nodes <= 100000
1 <= values stored in the nodes <= 10^9

Sample Test Case:
Sample Input:
https://i.imgur.com/Pn9jNrO.png

Sample Output:
1 2 3

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

class BSTIterator():
    def __init__(self, root = None):
        # initialize here
        pass

    def hasNext(self):
        pass

    def next(self):
        pass


def printIterator(root):
    iterator = BSTIterator(root)
    if iterator.hasNext() == False:
        print()
        return

    while iterator.hasNext():
        val = iterator.next()
        if iterator.hasNext():
            print(val, end=' ')
        else:
            print(val)

def main():
    root = readBinaryTree()
    printIterator(root)

main()

'''
We have provided only the optimal solution for this problem.
The problem asks to implement an iterator over a binary search tree so that hasNext() method of the iterator returns a true
 of false flag denoting the next nodes presence. And another method next() which return next node’s value. Iterator must
 iterate from the left most node to right most node so that nodes are in ascending order. The idea is that, the iterator
 should traverse the tree in in-order traversal approach. So, while initializing, we pushed root, root’s left child, root’s
 left child’s left child untile reach a null node into the stack. After initialization, left most node is at the top of
 stack. When next() method is invoked, top element from the stack is popped. As all left nodes are pushed from current top
 node, we push all left nodes starting from top node’s right child. This process continues until all nodes are traversed
 and popped from the stack.
Time complexity:
O(N)
Auxiliary space:
O(N) because of using stack
Space complexity:
Including input, O(N)
'''
'''
OPTIMAL SOLUTION
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
};

TreeNode* readBinaryTree(ifstream &fin){
    BinaryTree input_binary_tree;
    input_binary_tree.readRawValues(fin);
    input_binary_tree.validateInput();
    input_binary_tree.buildFromRawValues();
    return input_binary_tree.root;
}

// ============================ Start ============================
/*
    Complete the following methods
*/

class BSTIterator{
private:
    stack<TreeNode*> iteratorStack;
    void insertLeftNodes(TreeNode *root){
        while(root != NULL){
            iteratorStack.push(root);
            root = root->left_ptr;
        }
    }

public:
    BSTIterator(TreeNode *root){
        insertLeftNodes(root);
    }
    bool hasNext(){
        return (!iteratorStack.empty());
    }
    int next(){
        TreeNode *currentRoot = iteratorStack.top();
        iteratorStack.pop();
        insertLeftNodes(currentRoot->right_ptr);
        return currentRoot->val;
    }
};

// ============================ End ============================

void printIterator(TreeNode *root, ofstream &fout){
    BSTIterator iterator = BSTIterator(root);
    int isFirst = 1;
    while(iterator.hasNext()){
        if(!isFirst){
            fout<<" ";
        }
        fout<<iterator.next();
        isFirst = 0;
    }
    fout<<endl;
}

void solve(string inputFile, string outputFile){
    ifstream fin(inputFile);
    ofstream fout(outputFile);
    cerr<<"Running "<<inputFile<<endl;
    int testCase;
    fin>>testCase;
    for(int i=0;i<testCase;i++){
        cerr<<"Running case number "<<i<<endl;
        TreeNode *root = readBinaryTree(fin);
        printIterator(root, fout);
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



