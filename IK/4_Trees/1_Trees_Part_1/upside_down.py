'''
Upside Down
Problem Statement:
Given a binary tree where every node has either 0 or 2 children and every right node is a leaf node, flip it upside down
turning it into a binary tree where all left nodes are leafs.

For example, turn this:

https://i.imgur.com/FnYa8Bc.png

into this:

https://i.imgur.com/Aqrl3ut.png

where 6 is the root of the new tree.
Oriented differently, the new tree looks like this:

https://i.imgur.com/08dcpvk.png

Input/Output Format For The Function:
Input format:
Function has one argument of type TreeNode named root: root of the input tree.

Output format:
Function has to return a TreeNode value: root of the flipped-upside-down tree.

Constraints:
0 <= number of nodes <= 100000
1 <= values stored in the nodes <= 100000
Every node either has 0 or 2 children.
Every right node is a leaf node.

Sample Test Case:
Sample Input:
https://i.imgur.com/zTOidXi.png

Sample Output:
https://i.imgur.com/9lOEyEr.png

Tree node structure:
Class TreeNode {
    int val;
    TreeNode left_ptr;
    TreeNode right_ptr;
}

Input/Output Format For The Custom Input:
Input Format:
line number 1: <noOfNodes> denoting number of nodes of the tree.
line number 2: <noOfNdoes space separated integers> denoting the values of the nodes. Please make sure there are no leading or trailing spaces and between two integers there must be a single space.
line number 3: <rootIndex> denoting the root of the tree. value of rootIndex must be between -1 to noOfNodes-1
line number 4: <noOfEdges> denoting the number of edges of the tree
next noOfEdges line: <parentNodeIndex><space><childNodeIndex><space><leftOrRightFlag>
Here <parentNodeIndex> and <childNodeIndex> are the node indexes ranging from 0 to noOfNodes-1. <leftOrRighFlag> is either "L" or "R" (without quotes) denoting the left or right child where "L" stands for left child and "R" stands for right child.

Raw input of sample:
3
1 2 3
0
2
0 1 L
0 2 R

Output Format:
It is exactly the same as raw input format.
Raw output for the sample:
3
2 3 1
0
2
0 1 L
0 2 R
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
            print(
                self.edges[i].parentNodeIndex, self.edges[i].childNodeIndex,
                self.edges[i].leftRightFlag, sep=' '
            )


def printBinaryTree(root):
    outputBinaryTree = BinaryTree()
    outputBinaryTree.root = root
    outputBinaryTree.populateRawValuesFromTree()
    outputBinaryTree.writeRawValues()


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

def flipUpsideDown(root):
    pass



def main():
    root = readBinaryTree()
    result = flipUpsideDown(root)
    printBinaryTree(result)

main()

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

    void readRawValues(){
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

    void writeRawValues(){
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

void printBinaryTree(TreeNode* root){
    BinaryTree output_binary_tree;
    output_binary_tree.root = root;
    output_binary_tree.populateRawValuesFromTree();
    output_binary_tree.writeRawValues();
}

TreeNode* readBinaryTree(){
    BinaryTree input_binary_tree;
    input_binary_tree.readRawValues();
    input_binary_tree.buildFromRawValues();
    return input_binary_tree.root;
}

// ============================ Start ============================

TreeNode* flipUpsideDown(TreeNode* root){
    if(root == NULL){
        return root;
    }
    // If the root is a leaf node, then it will be the root of 
    // our flipped upside down tree.
    if(root->left_ptr == NULL && root->right_ptr == NULL){
        return root;
    }

    // Recursively flip upside down the left subtree.
    TreeNode* new_root = flipUpsideDown(root->left_ptr);
    // Update the left child of the root.
    root->left_ptr->left_ptr = root->right_ptr; 
    root->left_ptr->right_ptr = root;
    // Update the root.
    root->left_ptr = NULL;
    root->right_ptr = NULL;

    // Return the root of our flipped upside down tree.
    return new_root;
}

// ============================ End =============================

void validateInput(TreeNode* root){
    if(root == NULL){
        return;
    }
    if(root->left_ptr == NULL && root->right_ptr == NULL){ // leaf node
        return;
    }
    if(root->left_ptr == NULL || root->right_ptr == NULL){
        cout << "Each node must have 0 or 2 child." << endl;
        exit(1);
    }
    if(root->right_ptr->left_ptr != NULL || root->right_ptr->right_ptr != NULL){
        cout << "Right node must be leaf node." << endl;
        exit(1);
    }
    validateInput(root->left_ptr);
}

int main(){
    //freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
    //freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
    //freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
    //freopen("..//test_cases//generated_medium_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//generated_medium_test_cases_expected_output.txt", "w", stdout);
    freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
    freopen("..//test_cases//ignore.txt", "w", stdout);

    int test_cases;
    cin >> test_cases;
    assert(0 <= test_cases);
    while (test_cases--){
        TreeNode* root = readBinaryTree();
        validateInput(root);
        TreeNode* ans = flipUpsideDown(root);
        printBinaryTree(ans);
        cout << endl;
    }
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

void printBinaryTree(TreeNode* root, ofstream &fout){
    BinaryTree output_binary_tree;
    output_binary_tree.root = root;
    output_binary_tree.populateRawValuesFromTree();
    output_binary_tree.writeRawValues(fout);
}

TreeNode* readBinaryTree(ifstream &fin){
    BinaryTree input_binary_tree;
    input_binary_tree.readRawValues(fin);
    input_binary_tree.buildFromRawValues();
    return input_binary_tree.root;
}

// ============================ Start ============================

TreeNode* flipUpsideDown(TreeNode* root){
    if(root == NULL){
        return root;
    }
    
    // In upside down tree, for current root, these should be
    // the left and right children.
    TreeNode* assign_me_as_left_of_root = NULL;
    TreeNode* assign_me_as_right_of_root = NULL;
    
    while(root) {
        // Before updating root->left_ptr, store its value for future use.
        TreeNode* next_root = root->left_ptr;

        // In upside down tree, for next_root, these will be
        // the left and right children.
        TreeNode* next_assign_me_as_left_of_root = root->right_ptr;
        TreeNode* next_assign_me_as_right_of_root = root;
        
        // Make changes for current root. Update left and right children.
        root->left_ptr = assign_me_as_left_of_root;
        root->right_ptr = assign_me_as_right_of_root;

        if (next_root) {
            // We have made changes for current root, now go to the next root.
            root = next_root;
            assign_me_as_left_of_root = next_assign_me_as_left_of_root;
            assign_me_as_right_of_root = next_assign_me_as_right_of_root;
        } else {
            return root;
        }
    }
    // Should never reach here.
    assert(false);
    return NULL;
}

// ============================ End =============================

void validateInput(TreeNode* root){
    if(root == NULL){
        return;
    }
    if(root->left_ptr == NULL && root->right_ptr == NULL){ // leaf node
        return;
    }
    if(root->left_ptr == NULL || root->right_ptr == NULL){
        cout << "Each node must have 0 or 2 child." << endl;
        exit(1);
    }
    if(root->right_ptr->left_ptr != NULL || root->right_ptr->right_ptr != NULL){
        cout << "Right node must be leaf node." << endl;
        exit(1);
    }
    validateInput(root->left_ptr);
}

void solve(string inputFileName, string outputFileName){
    ifstream fin(inputFileName);
    ofstream fout(outputFileName);
    int testCase;
    fin>>testCase;
    fout<<testCase<<endl;
    int cnt=0;
    while(testCase--){
        TreeNode* root = readBinaryTree(fin);
        validateInput(root);
        TreeNode* ans = flipUpsideDown(root);
        printBinaryTree(ans, fout);
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


