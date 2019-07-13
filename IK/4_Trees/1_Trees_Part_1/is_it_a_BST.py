'''
Is It A BST
Problem Statement:
This is a very well-known interview problem: Given a Binary Tree, check if it is a Binary Search Tree (BST). A valid BST
 doesn't have to be complete or balanced.
Input/Output Format For The Function:
Input format:
There is only one argument named root denoting the root of the input tree.
Output format:
You have to return true if the input tree is a BST or false otherwise.
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

Raw input of sample 1:
3
1 2 3
0
2
0 1 L
0 2 R
Output Format:
line number 1: 1 or 0 based on whether it's a BST or not.
Raw output of sample 1:
0
Constraints:
0 <= number of nodes <= 100000
1 <= values stored in the nodes <= 10^9
Return value must be boolean
Sample Test Case:
Sample Input 1:
https://i.imgur.com/HSfRJk9.png

Sample Output 1:
0

Explanation 1:
In the input tree, left child value(2) is greater than parent node value(1) which is a violation of BST definition.

Sample Input 2:
https://i.imgur.com/YoYYmum.png

Sample Output 2:
1

Explanation 2:
In the input tree, left child value is less than parent node value and right child value is greater than parent node value.

 Also both left subtree(node having value 1) and right subtree(node having value 3) is valid BST as they are leaf nodes.
 So, this is a BST.
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

# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def isBST(root):
    pass


def main():
    root = readBinaryTree()
    result = isBST(root)
    if result:
        print(1)
    else:
        print(0)

main()



'''
We have provided two solutions for this problem. optimal_solution.cpp is the optimal solution considering both time complexity
 and space complexity. On the other hand, other_solution.cpp is optimal considering time complexity, but not space complexity.

1)other_solution.cpp:
Description:
Definition of a BST goes like this:
All nodes values of left subtree are lesser than or equal to parent node value
All nodes values of right subtree are greater
 than or equal to parent node value
Both left subtree and right subtree must be a BST
By definition, NULL tree is a BST

By definition, tree having a single node or leaf nodes are BST
In the following tree examples, tree A and B is a BST, where tree C is not:
 https://i.imgur.com/lkiRIvM.png

In other_solution.cpp solution we have used in-order traversal property of a BST to validate whether it is a BST or not.
 In-order traversal of a tree returns an array where left most node is at 0th index where right most node is at (N-1)th
 index. As left most node in a BST is the node having smallest value and right most node is the node having largest value,
 so we can conclude that in-order traversal of a BST returns a sorted array in strict ascending order. In other_solution.cpp
 solutions, we have used this theory. We have traversed the input tree in in-order and stored the values in an array. Later
 we checked if the returned array is sorted in strict ascending order.
Time Complexity:
O(N) where N is the number of nodes
Auxiliary Space Used:
In other solution: O(2*N) because of recursion stack and an array
Space Complexity:
Including input, O(2*N) in other_solution.cpp
2)optimal_solution.cpp:
Description:
Definition of a BST goes like this:
All nodes values of left subtree are lesser than or equal to parent node value
All nodes values of right subtree are greater
 than or equal to parent node value
Both left subtree and right subtree must be a BST
By definition, NULL tree is a BST

By definition, tree having a single node or leaf nodes are BST
In the following tree examples, tree A and B is a BST, where tree C is not:
https://i.imgur.com/pXMggSP.png

In optimal_solution.cpp we followed the definition. We first checked if current node value is in a valid range or not. If
 in valid range and both left and right subtrees are BST too, then subtree rooted at current node forms a BST too.
Time complexity:
optimal_solution.cpp: O(N)
other_solution.cpp: O(N)
Auxiliary space:
In optimal solution: O(N) because of recursion stack
Space complexity:
Including input, O(N) in optimal_solution.cpp
'''

'''
OTHER SOLUTION
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

void isBSTHelper(TreeNode *root, vector<int>&inorder){
    // NULL node check
    if(root == NULL){
        return;
    }
    isBSTHelper(root->left_ptr, inorder);
    inorder.push_back(root->val);
    isBSTHelper(root->right_ptr, inorder);
}

bool isBST(TreeNode* root){
    // empty or null tree check
    if(root==NULL){
        return true;
    }
    vector<int>inorder;
    isBSTHelper(root, inorder);
    for(int i=1; i<inorder.size();i++){
        if(inorder[i]<inorder[i-1]){
            return false;
        }
    }
    return true;
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
        int result = isBST(root);
        if(result == true){
            fout<<1<<endl;
        } else {
            fout<<0<<endl;
        }
    }
}

int main(){
    solve("..//test_cases//sample_test_cases_input.txt", "..//test_cases//sample_test_cases_expected_output_1.txt");
    solve("..//test_cases//handmade_test_cases_input.txt", "..//test_cases//handmade_test_cases_expected_output_1.txt");
    solve("..//test_cases//generated_small_test_cases_input.txt", "..//test_cases//generated_small_test_cases_expected_output_1.txt");
    // solve("..//test_cases//generated_big_test_cases_input.txt", "..//test_cases//generated_big_test_cases_expected_output.txt");
    return 0;
}
'''
'''
OPTMIAL SOLUTION
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

bool isBSTHelper(TreeNode *root, int min, int max){
    // NULL node check
    if(root == NULL){
        return true;
    }
    // current node value is not within valid range
    if(root->val>max || root->val<min){
        return false;
    }
    // true when both left and right subtrees are valid BST
    return isBSTHelper(root->left_ptr, min, root->val) && isBSTHelper(root->right_ptr, root->val, max);
}

bool isBST(TreeNode* root){
    // empty or null tree check
    if(root==NULL){
        return true;
    }
    int min = INT_MIN;
    int max = INT_MAX;
    return isBSTHelper(root, min, max);
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
        bool result = isBST(root);
        if(result == true){
            fout<<1<<endl;
        } else {
            fout<<0<<endl;
        }
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
