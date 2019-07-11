'''
Convert a Binary Tree into a Circular Doubly Linked List
Problem Statement:
Write a function BTtoLL(TreeNode root) that takes a binary tree and rearranges its left_ptr and right_ptr pointers to make
 a circular doubly linked list out of the tree nodes in the in-order traversal order. The head of the list must be the leftmost
 node of the tree (since it is the first one in the in-order traversal) and the tail of the list must be the rightmost node
 of the tree. Tail’s “next” pointer must point to the head and head’s “previous” pointer must point to the tail (as circular
 doubly-linked lists go).
In the resultant data structure we will think of right_ptr as “next” pointer of the list and of left_ptr as the “previous”
 pointer of the list. Note that although the resultant data structure will consist of a bunch of TreeNode instances, it
 will not be a tree (because, as a graph, it will have cycles).
The function must not allocate any new TreeNode instances, it must not change existing TreeNodes’ values either. It must
 change left_ptr and right_ptr pointers of the existing TreeNodes to form the desired data structure.
The function must return a TreeNode instance which is the head of the resultant circular doubly-linked list. The function
 must not print anything to the standard output.
For example, if given TreeNode “4” as pictured on the first image, we must return TreeNode that’s labeled “ROOT” on the
second image:

https://i.imgur.com/GTFsxSI.png

Input format:
There is only one argument named root denoting the root of the input tree.
Output format:
The function must return a TreeNode instance that is the head of the formed circular doubly-linked list.
Constraints:
0 <= number of nodes <= 100000
1 <= values stored in the nodes <= 10^9
Input tree will be a binary tree
Sample Test Case:
Sample Input:
See image in Problem Statement.
Sample Output:
See image in Problem Statement.
Explanation:
Leftmost node will be the head of the resultant circular doubly linked list and rightmost node will be the tail.
'''

import sys
from collections import deque

sys.setrecursionlimit(100000 + 1000)


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


def printCircularList(circularListHead):
    if circularListHead == None:
        print()
        return;
    tmpHead = circularListHead;
    while tmpHead.right_ptr != circularListHead:
        print(tmpHead.val, end=' ')
        tmpHead = tmpHead.right_ptr
    print(tmpHead.val)

# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def BTtoLL(root):
    pass


def main():
    root = readBinaryTree()
    result = BTtoLL(root)
    printCircularList(result)

main()

'''
We have provided two solutions for this problem. Both solutions are optimal. Difference between these solution is the traversal
 approach of a tree. optimal_solution.cpp uses post-order traversal where other_solution.cpp uses in-order traversal.
1.other_solution.cpp:
This solution uses in-order traversal approach of a tree and create a doubly linked list. It also stores head and tail pointer
 of the doubly linked list so that they can be connected to form a circular doubly linked list. Process are:
1. Traverse left subtree and create a doubly linked list. Let’s address it as leftDLL. Left most node is marked as head node.
2. Place root node after the tail of leftDLL and root node becomes the new tail.
3. Traverse right subtree and create a doubly linked list. Let’s address is as rightDLL. Place head of rightDLL after tail 
    and tail of right DLL becomes new tail node.
4. Connect head and tail node to form a circular DLL.

Tricky part of this approach is to update the tail node. The tail node is the last visited node of the tree.

Time complexity:
O(N)
Auxiliary space:
O(N) because of using stack
Space complexity:
Including input, O(N)

2.optimal_solution.cpp:

This solution uses post-order traversal approach of a tree and creates a circular doubly linked list. Process are:
1. Traverse left subtree and create a circular doubly linked list. Let’s address it as leftCDLL
2. Traverse right subtree and create a doubly linked list. Let’s address is as rightCDLL.
3. Created a circular doubly linked list using the root node only. Let’s call it rootCDLL.
4. Connect leftCDLL and rootCDLL. Let’s address it as leftRootCDLL. Head will be head of leftCDLL.

Connect leftRootCDLL and rightCDLL and let’s call it resultCDLL. Head will be the head of leftRootCDLL.
Tricky part of this approach is to connect two CDLL. Approach to connect two CDLL is described below. For convenience, we
 will use leftCDLL as first CDLL and rightCDLL as second CDLL to connect.
If one of them is null return other one.
Find out tail of leftCDLL. Let’s denote it as leftTail.
Find out tail of rightCDLL.
 Let’s denote it as rightTail.
Connect leftTail and head of rightCDLL.
Connect rightTail and head of leftCDLL.
Mark head
 of leftCDLL as the head of resultant CDLL.
Time complexity:
O(N)
Auxiliary space:
O(N) because of using stack
Space complexity:
Including input, O(N)
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

void printCircularList(TreeNode *circularListHead, ofstream &fout){
    if(circularListHead == NULL){
        fout<<endl;
        return;
    }
    TreeNode *tmpHead = circularListHead;
    while(tmpHead->right_ptr != circularListHead){
        fout<<tmpHead->val<<" ";
        tmpHead = tmpHead->right_ptr;
    }
    fout<<tmpHead->val<<endl;
}


// ============================ Start ============================

/*
 * Complete the function below.
 */

void BTToLLHelper(TreeNode *root, TreeNode **head, TreeNode **currentTail){
    if(root == NULL){
        return;
    }
    BTToLLHelper(root->left_ptr, head, currentTail);
    if(*head == NULL){
        *head = root;
    }
    if(*currentTail == NULL){
        *currentTail = root;
    } else{
        (*currentTail)->right_ptr = root;
        root->left_ptr = *currentTail;
    }
    *currentTail = root;
    BTToLLHelper(root->right_ptr, head, currentTail);
}

TreeNode* BTtoLL(TreeNode* root) {
    if(root == NULL){
        return root;
    }
    TreeNode *head = NULL;
    TreeNode *tail = NULL;
    BTToLLHelper(root, &head, &tail);
    tail->right_ptr = head;
    head->left_ptr = tail;
    return head;
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
        TreeNode *CLL = BTtoLL(root);
        printCircularList(CLL, fout);
    }
}

int main(){
    solve("..//test_cases//sample_test_cases_input.txt", "..//test_cases//sample_test_cases_expected_output1.txt");
    solve("..//test_cases//handmade_test_cases_input.txt", "..//test_cases//handmade_test_cases_expected_output1.txt");
    solve("..//test_cases//generated_small_test_cases_input.txt", "..//test_cases//generated_small_test_cases_expected_output1.txt");
    solve("..//test_cases//generated_big_test_cases_input.txt", "..//test_cases//generated_big_test_cases_expected_output1.txt");
    // solve("a.txt", "bb.txt");
    return 0;
}    
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

void printCircularList(TreeNode *circularListHead, ofstream &fout){
    if(circularListHead == NULL){
        fout<<endl;
        return;
    }
    TreeNode *tmpHead = circularListHead;
    while(tmpHead->right_ptr != circularListHead){
        fout<<tmpHead->val<<" ";
        tmpHead = tmpHead->right_ptr;
    }
    fout<<tmpHead->val<<endl;
}

// ============================ Start ============================

/*
 * Complete the function below.
 */

TreeNode* connectTwoCLL(TreeNode *leftCLLHead, TreeNode *rightCLLHead){
    if(leftCLLHead == NULL){
        return rightCLLHead;
    }
    if(rightCLLHead == NULL){
        return leftCLLHead;
    }
    TreeNode *leftCLLTail = leftCLLHead->left_ptr;
    TreeNode *rightCLLTail = rightCLLHead->left_ptr;

    leftCLLTail->right_ptr = rightCLLHead;
    rightCLLHead->left_ptr = leftCLLTail;

    rightCLLTail->right_ptr = leftCLLHead;
    leftCLLHead->left_ptr = rightCLLTail;

    return leftCLLHead;
}

TreeNode* BTtoLL(TreeNode* root) {
    if(root == NULL){
        return root;
    }
    TreeNode *leftCLLHead =  BTtoLL(root->left_ptr);
    TreeNode *rightCLLHead =  BTtoLL(root->right_ptr);

    root->left_ptr = root->right_ptr = root;

    TreeNode *curretCLL = connectTwoCLL(leftCLLHead, root);
    curretCLL = connectTwoCLL(curretCLL, rightCLLHead);

    return curretCLL;
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
        TreeNode *CLL = BTtoLL(root);
        printCircularList(CLL, fout);
    }
}

int main(){
    solve("..//test_cases//sample_test_cases_input.txt", "..//test_cases//sample_test_cases_expected_output.txt");
    solve("..//test_cases//handmade_test_cases_input.txt", "..//test_cases//handmade_test_cases_expected_output.txt");
    solve("..//test_cases//generated_small_test_cases_input.txt", "..//test_cases//generated_small_test_cases_expected_output.txt");
    solve("..//test_cases//generated_big_test_cases_input.txt", "..//test_cases//generated_big_test_cases_expected_output.txt");
    // solve("a.txt", "b.txt");
    return 0;
}    
'''
