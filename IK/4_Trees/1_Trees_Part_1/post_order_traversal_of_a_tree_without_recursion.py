'''
Post-order Traversal of a Tree Without Recursion
Problem Statement:
Write a function to traverse a binary tree Post-order, without using recursion. As you traverse, please print contents of
 the nodes.
e.g. for a tree that's
https://i.imgur.com/kgjjbOk.png

Print:
4 5 2 6 7 3 1

Input/Output Format For The Function:

Input format:
There is only one argument named root denoting the root of the input tree.

Output format:
Return an array containing the node values in post-order traversal of the tree.

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
5
1 2 3 4 5
0
4
0 1 L
0 2 R
1 3 L
1 4 R
Output Format:
Space separated integer denoting the values in postorder traversal.
Raw output of sample:
4 5 2 3 1
Constraints:
0 <= number of nodes <= 100000
1 <= values stored in the nodes <= 10^9
Sample Test Case:
Sample Input:
https://i.imgur.com/5JayjTc.png

Sample Output:
4 5 2 3 1
Explanation:
There are 5 nodes in the tree. As post-order traversal sequence is left_node -> right_node -> parent_node, so from root
 (1) it goes to left node (2). Left node has two children. So, it goes to left (4) again which is a leaf node. Print the
 content of this node. Go to parent’s right (5) node which is also a leaf node. Print the content and go back to parent
 (2) node, print the content and go back to its parent (1). Repeat this process for right side and print the root node (1)
 at last.
Tree node structure:
Class TreeNode {
    int val;
    TreeNode left_ptr;
    TreeNode right_ptr;
}
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


def printArray(result):
    if result == None:
        print()
        return
    for i in range(0, len(result)):
        if i > 0:
            print(end=' ')
        print(result[i], end='')
    print()

# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def postorderTraversal(root):
    pass

def main():
    root = readBinaryTree()
    result = postorderTraversal(root)
    printArray(result)

main()


'''
We have provided one solution for this problem which is optimal. The problem asked to traverse a tree in post order and
 print the content.
In post-order traversal, traversing sequence is: left node → right node → root node. If left node is not null or leaf node,
 this process continues. Same for right node. So, left most node’s content is printed at first and root node’s content is
 at last.
So the above mentioned process is repetitive and we know the when it will stop ( null or lead nodes ). This can be done
 with a simple recursion. The recursive relationship will be:
If node is null:
Stop
If node is leaf:
Print the content
Stop
Print left subtree
Print right subtree
Print current node’s content
That’s all! But wait! This problem prohibited to use any recursive method. So, we can’t use recursion here. We have to do
 it iteratively. As a recursive method uses a buffered stack, we can use stack data structure as alternative of recursive
 method. So, to print in order left_ptr → right_ptr → root, we have to insert the nodes into stack in order of: root → right_ptr
 → left_ptr and repeating this process until all the nodes are traversed.
Time complexity:
optimal_solution.cpp: O(N)
Auxiliary space:
optimal_solution.cpp: O(N) because of using stack
Space complexity:
optimal_solution.cpp: Including input, O(N)
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

// ============================ Start ============================

void postorderTraversal(TreeNode* root, ofstream &fout){
    // empty or null tree check
    if(root == NULL){
        fout<<endl;
        return;
    }
    stack<TreeNode*> stack;
    stack.push(root);
    while(!stack.empty()){
        TreeNode* top = stack.top();
        // leaf node check
        if(top->left_ptr == NULL && top->right_ptr == NULL) {
            stack.pop();
            fout<<top->val;
            if(stack.empty()){
                fout<<endl;
            }
            else{
                fout<<" ";
            }
        } else{
            if(top->right_ptr != NULL){
                stack.push(top->right_ptr);
                top->right_ptr = NULL;
            }
            if(top->left_ptr != NULL){
                stack.push(top->left_ptr);
                top->left_ptr = NULL;
            }
        }
    }
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
        postorderTraversal(root, fout);
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
