'''
Alternative Node Split
Problem Statement:
Given a linked list, split it into two such that every other node goes into the new list. For lists with odd number of nodes, first one should be longer. For example: an input list: {a, b, c, d, e, f, g} results in {a, c, e, g} and {b, d, f}.

Input format:
There is only one argument named head denoting the head of the input linked list.

Output format:
Return an array of linked list which contains two linked list.

Constraints:
    * 0 <= number of nodes <= 100000
    * 1 <= values stored in the nodes <= 1000000000
    * Input will be a singly linked list

Sample Test Case:
Sample Input:
1 -> 2 -> 3 -> 4 -> 5

Sample Output:
1 -> 3 -> 5
2 -> 4

Explanation:
Process is explained in the problem statement.
'''
import sys
from collections import deque

sys.setrecursionlimit(101000)
class LinkedListNode():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def createLinkedList(inputArray):
    head = None
    tail = None

    for i in range(0, len(inputArray)):
        currentNode = LinkedListNode(inputArray[i])
        if head == None:
            head = currentNode
            tail = currentNode
        else:
            tail.next = currentNode
            tail = tail.next
    return head

def readInput():
    numberOfNodes = int(input())
    nodeValuesStringArray = []
    if numberOfNodes > 0:
        nodeValuesStringArray = input().split(' ')
    nodeValues=[]
    for i in range(0, len(nodeValuesStringArray)):
        nodeValues.append(int(nodeValuesStringArray[i]))
    return createLinkedList(nodeValues)

# complete the function below

def alternativeSplit(head):
    pass


def printList(head):
    if head == None:
        print()
        return
    while head != None:
        if head.next == None:
            print(head.val)
        else:
            print(head.val, end=" ")
        head = head.next

def getArraySize(array):
    if array == None:
        return 0
    return len(array)

def main():
    head = readInput()
    result = alternativeSplit(head)
    outputArraySize = getArraySize(result)
    if outputArraySize != 2:
        sys.stderr.write("Output must be an array with 2 LinkedListNode\n")
        return
    printList(result[0])
    printList(result[1])

main()

'''
We have provided only the optimal solution for this problem.
The problem asks to split a given linked list into two linked list is such a way that consecutive nodes are in different
linked list. Which means, nodes in even positions will be in a linked list and nodes in odd positions will be in another
linked list. The provided solution creates two linked list. One of these holds nodes of even position and other one holds
nodes of odd position.

Time complexity:
O(N)

Auxiliary space:
O(N)

Space complexity:
Including input, O(N)
'''
'''
#include <bits/stdc++.h>

using namespace std;

struct LinkedListNode{
    int val;
    LinkedListNode *next;

    LinkedListNode(int _val){
        val = _val;
        next = NULL;
    }
};

LinkedListNode* createLinkedList(int *inputArray, int inputSize){
    LinkedListNode *head = NULL;
    LinkedListNode *tail = NULL;
    for(int i = 0; i<inputSize; i++){
        LinkedListNode *currentNode = new LinkedListNode(inputArray[i]);
        if(head == NULL){
            head = currentNode;
            tail = head;
        } else{
            tail->next = currentNode;
            tail = tail->next;
        }
    }
    return head;
}

LinkedListNode* readInput(ifstream &fin){
    int n; fin>>n;
    int *ar;
    ar = new int[n];
    for(int i=0;i<n;i++){
        fin>>ar[i];
    }
    return createLinkedList(ar, n);
}

// ============================ Start ============================
/*
    Complete the following methods
*/

vector<LinkedListNode*> alternativeSplit(LinkedListNode *head){
    LinkedListNode *evenListHead = NULL;
    LinkedListNode *evenListTail = NULL;

    LinkedListNode *oddListHead = NULL;
    LinkedListNode *oddListTail = NULL;

    int isEvenIndex = 1;
    while(head){
        LinkedListNode *currentNode = new LinkedListNode(head->val);
        if(isEvenIndex == 1){
            if(evenListHead == NULL){
                evenListHead = currentNode;
                evenListTail = currentNode;
            } else {
                evenListTail->next = currentNode;
                evenListTail = evenListTail->next;
            }
        } else {
            if(oddListHead == NULL){
                oddListHead = currentNode;
                oddListTail = currentNode;
            } else {
                oddListTail->next = currentNode;
                oddListTail = oddListTail->next;
            }
        }
        isEvenIndex = isEvenIndex^1;
        head = head->next;
    }
    vector<LinkedListNode*> result;
    result.push_back(evenListHead);
    result.push_back(oddListHead);
    return result;
}

// ============================ End ============================

void printList(LinkedListNode *head, ofstream &cout){
    int id = 0;
    while(head){
        if(id > 0) cout<<" ";
        cout<<head->val;
        head = head->next;
        id++;
    }
    cout<<endl;
}

void solve(string inputFileName, string outputFileName){
    ifstream fin(inputFileName);
    ofstream fout(outputFileName);
    int testCase; fin>>testCase;
    while(testCase--){
        LinkedListNode *root = readInput(fin);
        vector<LinkedListNode*> result = alternativeSplit(root);
        if(result.size()!=2){
            cerr<<"Answer size must be 2"<<endl;
            return;
        }
        printList(result[0], fout);
        printList(result[1], fout);
    }
}

int main(){
    solve("..//test_cases//sample_test_cases_input.txt", "..//test_cases//sample_test_cases_expected_output.txt");
    solve("..//test_cases//handmade_test_cases_input.txt", "..//test_cases//handmade_test_cases_expected_output.txt");
    solve("..//test_cases//generated_big_test_cases_input.txt", "..//test_cases//generated_big_test_cases_expected_output.txt");
    return 0;
}    
'''


