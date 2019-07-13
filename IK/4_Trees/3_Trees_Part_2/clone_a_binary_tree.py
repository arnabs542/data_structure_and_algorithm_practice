'''
Clone a Binary Tree
Problem Statement:
Given a binary tree (represented by its root node, like usual), clone it. Return the root node of the cloned tree.
Remember: Cloning or copying a tree is best done recursively. Notice how clean and succinct the code is. Some of you may
 be tempted to do it breadth-first. But that's more complicated to handle in implementation.
Input/Output Format For The Function:
Input format:
There is only one argument named root denoting the root of the input tree.
Output format:
Return the root of cloned tree.
Input/Output Format For The Custom Input:
Input Format:
line number 1: <noOfNodes> denoting number of nodes of the tree.
line number 2: <noOfNdoes space seprated integers> denoting
 the values of the nodes. Please make sure there are not leading or trailing spaces and between two integers there must
 be a single space.
line number 3: <rootIndex> denoting the root of the tree. value of rootIndex must be between -1 to noOfNodes-1

line number 4: <noOfEdges> denoting the number of edges of the tree
next noOfEdges line: <parentNodeIndex><space><childNodeIndex><space><leftOrRightFlag>.
 Here <parentNodeIndex> and <childNodeIndex> are the node indexes ranging from 0 to noOfNodes-1. <leftOrRighFlag> is either
 "L" or "R" (without quotes) denoting the left or right child where "L" stands for left child and "R" stands for right child.

For the below tree:
https://i.imgur.com/DAvplOf.png

Raw input will be:
5
1 2 3 4 5
0
4
0 1 L
0 2 R
1 3 L
1 4 R

Output Format:
It is exactly same as raw input format.
For the below tree:
https://i.imgur.com/XI4Dlkx.png

Raw output will be:
5
1 2 3 4 5
0
4
0 1 L
0 2 R
1 3 L
1 4 R

Constraints:
0 <= number of nodes <= 100000
1 <= values stored in the nodes <= 10^9
Sample Test Case:
Sample Input:
https://i.imgur.com/PZKOtQb.png

Sample Output:
https://i.imgur.com/nn9j7IA.png

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

    def considerEdge(self, lOrR, parent, child, nodeToId, id, edgeCreateCycle):
        if child != None:
            if child in nodeToId:
                edgeCreateCycle[0] = True
                sys.stderr.write("Cycle detected in the tree. Cycle contains the edge: ",
                                 nodeToId[parent], nodeToId[child], lOrR)
            else:
                nodeToId[child] = id[0]
                id[0] += 1
                self.nodeValues.append(child.val)
            self.edges.append(self.Edge(nodeToId[parent], nodeToId[child], lOrR))

    def getNodeValuesAndEdges(self, root, nodeToId, id):
        if root == None:
            return
        leftEdgeCreateCycle = [False]
        rightEdgeCreateCycle = [False]

        self.considerEdge("L", root, root.left_ptr, nodeToId, id, leftEdgeCreateCycle)
        self.considerEdge("R", root, root.right_ptr, nodeToId, id, rightEdgeCreateCycle)

        if leftEdgeCreateCycle[0] == False:
            self.getNodeValuesAndEdges(root.left_ptr, nodeToId, id)
        if rightEdgeCreateCycle[0] == False:
            self.getNodeValuesAndEdges(root.right_ptr, nodeToId, id)

    def populateRawValuesFromTree(self):
        self.noOfNodes = 0
        self.noOfEdges = 0;
        self.rootIndex = -1
        self.nodeValues = []
        self.edges = []

        if self.root != None:
            id = [0]
            nodeToId = {}
            self.rootIndex = 0
            nodeToId[self.root] = id[0]
            id[0] += 1
            self.nodeValues.append(self.root.val)

            self.getNodeValuesAndEdges(self.root, nodeToId, id)

            self.noOfNodes = len(self.nodeValues)
            self.noOfEdges = len(self.edges)

    def writeRawValues(self):
        print(self.noOfNodes)
        for i in range(self.noOfNodes):
            if i == self.noOfNodes - 1:
                print(self.nodeValues[i])
            else:
                print(self.nodeValues[i], end=' ')

        print(self.rootIndex)

        print(self.noOfEdges)
        for i in range(self.noOfEdges):
            print(self.edges[i].parentNodeIndex, self.edges[i].childNodeIndex, self.edges[i].leftRightFlag, sep=' ')


def readBinaryTree():
    inputBinaryTree = BinaryTree()
    inputBinaryTree.readRawValues()
    inputBinaryTree.buildFormRawValues()
    return inputBinaryTree.root


def printBinaryTree(root):
    outputBinaryTree = BinaryTree()
    outputBinaryTree.root = root
    outputBinaryTree.populateRawValuesFromTree()
    outputBinaryTree.writeRawValues()


def isOutputTreeCloned(inputTreeRoot, outputTreeRoot):
    if inputTreeRoot == None or outputTreeRoot == None:
        return True
    if inputTreeRoot == outputTreeRoot:
        return False
    isLeftSubtreeCloned = isOutputTreeCloned(inputTreeRoot.left_ptr, outputTreeRoot.left_ptr)
    isRightSubtreeCloned = isOutputTreeCloned(inputTreeRoot.right_ptr, outputTreeRoot.right_ptr)
    return (isLeftSubtreeCloned & isRightSubtreeCloned);

# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

# complete the function below

def cloneTree(root):
    pass



def main():
    root = readBinaryTree()
    result = cloneTree(root)
    if isOutputTreeCloned(root, result) == False:
        sys.stderr.write("Input tree is not cloned!\n")
    else:
        printBinaryTree(result)

main()



'''
We have provided one solution for this problem. This is the optimal solution.
The problem asks to clone a binary tree. We do it recursively. First we create a new node using the current root node value.
 We clone the current node’s left child and assign as left child of new node. We do the same for right child.
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

    void considerEdge(
        string lOrR, TreeNode* parent, TreeNode* child, 
        unordered_map<TreeNode*, int>& nodeToId, int& id, bool& edge_creates_cycle
    ){
        if (child){
            if (nodeToId.find(child) == nodeToId.end()){
                nodeToId[child] = id++;
                nodeValues.push_back(child->val);
            }else{
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

void printBinaryTree(TreeNode* clonedRoot, ofstream &fout){
    BinaryTree output_binary_tree;
    output_binary_tree.root = clonedRoot;
    output_binary_tree.populateRawValuesFromTree();
    output_binary_tree.writeRawValues(fout);
}

// ============================ Start ============================

/*
 * Complete the function below.
 */

TreeNode* cloneTree(TreeNode* root) {
    if(root == NULL){
        return root;
    }
    TreeNode *clonedRoot = new TreeNode(root->val);
    clonedRoot->left_ptr = cloneTree(root->left_ptr);
    clonedRoot->right_ptr = cloneTree(root->right_ptr);
    return clonedRoot;
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
        TreeNode *result = cloneTree(root);
        printBinaryTree(result, fout);
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
