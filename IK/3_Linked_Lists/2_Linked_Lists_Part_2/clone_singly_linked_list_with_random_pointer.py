'''
Clone Singly Linked List With Random Pointer
Problem Statement:
Given a singly LinkedList list of n elements. The data stored in the nodes of the linked list are the continuous sequence
of the integral natural numbers i.e. the head node stores the integer 1 , then the  next node stores the integer 2 , so
on and so forth till the last node of the linked list stores the integer n. Now, apart the standard next pointer of the
linked-list node; there is a special random pointer that may or may not exists on each node. This random pointer of a node
can point to any node of the linked list including itself.

Your task is to clone the LinkedList List in an efficient manner both in terms of time and space.
Input Format:
First and only parameter of the function cloneLinkedList, that is to be implemented is the head node pointer of the given
 LinkedList list.
Output Format:
Return the head node of the newly cloned LinkedList in the cloneLinkedList function.
Then code written by us will traverse the returned linked list (starting from head node) and for each node, it will print
 one line containing three space separated integers 1) Data of the current node 2) If next node exists, then data of the
 next node, else -1 3) If random pointed node exists, then data of the random pointed node else -1.

Constraints:
    * 1 <= n <= 100000

Sample Test Case:
Sample Input:

https://i.imgur.com/PKkDrTn.png
             __
            |  |
            |  v
      1->2->3->4->5
      |     ^
      |     |
       \___/

﻿Sample Output:
1 2 3
2 3 -1
3 4 4
4 5 -1
5 -1 -1

Explanation:
Here the newly cloned list will be same as the input linkedlist. Hence, traversing from the head to tail node, code written
 by us will print 1 (data of the node), then 2 (data of its next node) and then 3 (data of its random pointed node). Now,
 it will move on the next node and print 2 (data of the node), then 3 (data of its next node), -1 (because this node has
 no random pointing node). Then it will move to the next node and print in the same fashion.
Note:
You may modify the given input linked-list list for cloning purpose.
'''
#!/bin/python
import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.randomPointer = None

    def set_randomPointer(self, randomPointer):
        self.__randomPointer = randomPointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    delimter = " "
    visited = set()
    while node:

        visited.add(node)
        if node.next != None and visited.__contains__(node.next) == True:
            sys.stderr.write(
                "The next pointer links in the cloned list are forming a loop")

        sys.stdout.write(str(node.data) + delimter)

        if node.next:
            sys.stdout.write(str(node.next.data) + delimter)
        else:
            sys.stdout.write("-1" + delimter)

        if node.randomPointer:
            sys.stdout.write(str(node.randomPointer.data))
        else:
            sys.stdout.write("-1")

        node = node.next

        if node:
            sys.stdout.write(sep)


def cloneCheck(clonedListHead, originalNodes):
    while(clonedListHead):
        if originalNodes.__contains__(clonedListHead):
            return False
        clonedListHead = clonedListHead.next
    return True


#
# Complete the 'cloneLinkedList' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST List as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#     SinglyLinkedListNode randomPointer
#


def cloneLinkedList(List):
    # Write your code here
    return List



if __name__ == '__main__':
    n = int(input().strip())

    List = SinglyLinkedList()

    mapper = {}
    originalNodes = set()
    mapper[-1] = None
    for i in range(n):
        List_item = i+1
        List.insert_node(List_item)
        mapper[List_item] = List.tail

    tmp = None
    for i in range(n):
        List_item = int(input().strip())
        List.head.randomPointer = mapper[List_item]
        if(i == 0):
            tmp = List.head
        originalNodes.add(List.head)
        originalNodes.add(List.head.randomPointer)
        List.head = List.head.next

    List.head = tmp

    clonedListHead = cloneLinkedList(List.head)

    if cloneCheck(clonedListHead, originalNodes) == False:
        # assert (False), "list not cloned"
        err_msg = "Instead of creating new node, you have used node from the input linked list. Any node from the input linked list must not be used in the cloned linked list"
        sys.stderr.write(err_msg)
    else:
        print_singly_linked_list(clonedListHead, "\n")


'''
Problem Overview:
Given a linked list with two standard attributes data and next pointer for each of its node. Also, the nodes in the given
list may or may-not contain one extra attribute : randomPointer, that can point to any node of the given linked list.
Our task is to clone the given linked list. Also, no node in our cloned list should be in the given linked list.
Brute-force Solution:
One thing is pretty much state forward that we can easily clone the linked list without the randomPointer. We can start
traversing from the head node and keep cloning the consecutive next pointer nodes in a linear time O(n), where n is the
number of nodes in the linked list. After this we can work on cloning the randomPointer links for the necessary nodes.
So, till now we have done a linear traversal on the linked list and cloned the nodes by following the next pointer links.
The process till now is O(n). Next, let’s see how we can link the random nodes. Consider some node X in original linked
list which has a randomPointer link. Now after the first cloning iteration we have some node X’ that is cloned node for
X. Now, we first go to the randomPointer node of the X node and get its distance(location) from the head node. Once, we
get that distance we move that distance linearly from newly cloned head node and reach some node S . Now, this node S,
should be the randomPointer node for the X’ node. Hence, we now link the randomPointer of X’ to S node. We do the same
process for all the nodes in the cloned list and make all the randomPointer links for the cloned nodes.
Let’s sum up the time complexities for both steps to get the overall time complexity. The first step of cloning the linked
list without the randomPointer links takes a linear amount of time O(n) as we are simply iterating on the nodes from head
to tail and each time we visit a node we are cloning it and linking it with its previous cloned node.
In second step we first find the location of the randomPointer node from the head node in the original node. This is again
a linear traversal from head node till the randomPointer node and takes O(n) in worst case. Next, after getting the distance
of the random node in the original list from its head node, we then move the same distance in the cloned list from its
head node to get the cloned randomPointer node. This again takes order of O(n) time to reach the cloned randomPointer node
from the cloned list. Then linking the cloned node with its randomPointer node is O(1) time. So, to link the randomPointer
node for a node in the cloned list takes O(n) + O(n) i.e. O(2*n) time. So, to do this for all the nodes it will take O(n*(2*n))
time i.e. O(2*n*n). Hence, the total time complexity sums up to O(n) + O(2*n*n) ~ O(2*n*n) ~ O(n*n).
Talking of Space complexity the input space complexity is O(n) as it gives us a linked list on n length. The auxiliary space
complexity is again O(n) as we are cloning a linked list as the same size of the input linked list and for doing so we
are using constant memory O(1) extra memory to hold the randomPointer node one at a time. Hence, the Total Space complexity
is O(n) + O(n) ~ O(n)
Optimal Solution:
We will now try solve it in linear amount of time O(n) and using same constant extra memory O(1) like in the brute force
approach. This approach is highly intuitive and knowing this trick is a plus point during your interview.
Now, let’s jump to the solution:

Assume the given input linked list is as below for n = 5:
https://i.imgur.com/9ErkR6c.png

      1->2->3->4->5
      |     ^  |  ^
      |     |  |  |
       \___/    \/


Step 1:
Now, we clone the ith node and insert it in between ith and (i+1)th node in the below manner.  Nodes in bracket are the
cloned nodes.

https://i.imgur.com/ZdLJ3a8.png

      1->(1)->2->(2)->->3->(3)->4->(4)->5->(5)
      |                 ^       |       ^  
      |                 |       |       |  
       \_______________/         \_____/   

Step 2:
Now we traverse the above linked list by moving 2 steps at a time and for every node x that we traverse and has a randomPointer
 link , we will link the randomPointer of next of x with the next link node of the x’s randomPointer node.
To be more specific we will do the below operation of every node x :
If x->randomPointer != null:
x->next->randomPointer = x->randomPointer->next
After performing this step all randomPointer links will be done for the newly cloned nodes in step 1 .
Our linked list will now look like the below depicted linked list :

https://i.imgur.com/1LqgDDh.png

           _________________         _______
          |                 |       |       |
          |                 v       |       v
      1->(1)->2->(2)->->3->(3)->4->(4)->5->(5)
      |                 ^       |       ^  
      |                 |       |       |  
       \_______________/         \_____/   


Step 3:
Now our last step will be to extract the cloned nodes from the above list by connecting the consecutive cloned nodes by
linking their next links. This extraction can be done in a single traversal on the linked list from the head node. In our
traversal for every node that we visit we simply re-link its next pointer with its next of next pointer (simply connecting
the next pointer 2 steps ahead of current node to counter the modification we did in step 1).
Hence, now we have our cloned list for the given initial input linked list.
Now, let’s do the Time Complexity analysis of the above three steps and all of them are pretty simple. In our first step
we traversed on the given input linked list of size n . So , its Time Complexity is O(n).
Similarly, for second and third step we are again traversing the linked list from head to tail node and hence take O(n)
time individually. Summing the Time complexities of all the three steps : O(n) + O(n) + O(n) = O(3*n) ~ O(n).
Talking of Space Complexity, the given input space is size of linked list O(n). The intermediate cloned nodes that we created
in step 1 take space equal to original linked list O(n) and these intermediate nodes are then chained and returned as the
final cloned list after linking their randomPointer nodes. So, we do not allocate any more memory for cloning the linked
list. Hence , the overall Space Complexity is O(2*n) ~ O(n) by using O(1) constant extra memory for cloning process.
'''
'''
BRUTE FORCE
#include <bits/stdc++.h>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);

class SinglyLinkedListNode
{
  public:
    int data;
    SinglyLinkedListNode *next;
    SinglyLinkedListNode *randomPointer;

    SinglyLinkedListNode(int node_data)
    {
        this->data = node_data;
        this->next = nullptr;
        this->randomPointer = nullptr;
    }

    void link_random_node(SinglyLinkedListNode *random_node) {
        this->randomPointer = random_node;
    }
};

class SinglyLinkedList
{
  public:
    SinglyLinkedListNode *head;
    SinglyLinkedListNode *tail;

    SinglyLinkedList()
    {
        this->head = nullptr;
        this->tail = nullptr;
    }

    void insert_node(int node_data)
    {
        SinglyLinkedListNode *node = new SinglyLinkedListNode(node_data);

        if (!this->head)
        {
            this->head = node;
        }
        else
        {
            this->tail->next = node;
        }

        this->tail = node;
    }

};

void print_singly_linked_list_with_random_node(SinglyLinkedListNode *node, string sep)
{   
    string delimitter = " ";
    while (node)
    {
        cout << node->data << delimitter;

        if(node->next != nullptr) {
            cout << node->next->data << delimitter;
        }
        else
            cout << -1 << delimitter;

        if(node->randomPointer != nullptr) {
            cout << node->randomPointer->data;
        }
        else {
            cout << "-1";
        }

        node = node->next;

        if (node)
        {
            cout << sep;
        }
    }
}

bool cloneCheck(SinglyLinkedListNode *head,unordered_set < SinglyLinkedListNode* > originalNodes) {
    SinglyLinkedListNode *tmp = head;
    while(tmp) {
        if(originalNodes.find(tmp) != originalNodes.end()) {
            return false;
        }
        tmp = tmp->next;
    }
    return true;
}

// ------------------------------ START ------------------------------

/*
 * @param list: pointer to the head node of the original linkedList
 * @returns the pointer to the newly cloned linkedList
 * This function clones the provided linkedList
 * Time Complexity : O(N*N)
 */
SinglyLinkedListNode* cloneLinkedList(SinglyLinkedListNode *list) {
    // initializing new clone list
    SinglyLinkedListNode *clonedListHead = nullptr;
    SinglyLinkedListNode *clonedListTail = nullptr;

    // first cloning the list by traversing the next pointeres
    SinglyLinkedListNode *headIterator = list;

    while (headIterator)
    {
        if (clonedListHead == nullptr)
        {
            clonedListHead = new SinglyLinkedListNode(headIterator->data);
            clonedListTail = clonedListHead;
        }
        else
        {
            clonedListTail->next = new SinglyLinkedListNode(headIterator->data);
            clonedListTail = clonedListTail->next;
        }
        headIterator = headIterator->next;
    }

    SinglyLinkedListNode *clonedHeadIterator = clonedListHead;
    headIterator = list;

    // now cloning link for random pointers
    while (headIterator)
    {   
        // getting random linked node for current node from original list
        SinglyLinkedListNode *randomNode = headIterator->randomPointer;
        if(randomNode == nullptr) {
            // if no random link exists 
            // mark the same for cloned list node
            clonedHeadIterator->randomPointer = nullptr;
        }
        else {
            SinglyLinkedListNode *tempHead = list;
            // this stores the distance of the randomNode from the head of 
            //  original list
            int steps = 0;

            // iteratig to count the steps required to reach randomNode
            while(tempHead != randomNode) {
                steps+=1;
                tempHead = tempHead->next;
            }

            // now going steps distance in the cloned list to get the corresponding
            // randomNode from the original list
            tempHead = clonedListHead;
            while(steps--) {
                tempHead = tempHead->next;
            }

            // linking the random node
            clonedHeadIterator->randomPointer = tempHead;
        }

        // moving to next original node 
        headIterator = headIterator->next;
        // moving to correspnding next cloned node
        clonedHeadIterator = clonedHeadIterator->next;
    }
    return clonedListHead;
}

// ------------------------------ STOP -------------------------------

int main()
{   
    unordered_map < int , SinglyLinkedListNode* > mapper;
    unordered_set < SinglyLinkedListNode* >originalNodes;
    SinglyLinkedList *List = new SinglyLinkedList();

    string linkedList_count_temp;
    getline(cin, linkedList_count_temp);

    int linkedList_count = stoi(ltrim(rtrim(linkedList_count_temp)));

    for(int i=1;i<=linkedList_count;i++) {
        List->insert_node(i);
        mapper[i] = List->tail;
        originalNodes.insert(List->tail);
    }

    for (int i = 1; i <= linkedList_count; i++) {
        string linkedList_item_temp;
        getline(cin, linkedList_item_temp);
        int linkedList_item = stoi(ltrim(rtrim(linkedList_item_temp)));
        if(linkedList_item != 0)
            mapper[i]->link_random_node(mapper[linkedList_item]);
    }

    SinglyLinkedListNode *clonedListHead = cloneLinkedList(List->head);

    if (cloneCheck(clonedListHead, originalNodes) == false)
    {
        cerr << "linked list not cloned";
        assert(false);
    }
    else {
        string seperator = "\n";
        print_singly_linked_list_with_random_node(clonedListHead,seperator);
    }

    return 0;
}

string ltrim(const string &str)
{
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str)
{
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}
'''
'''
OPTMIAL SOLUTION
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

class SinglyLinkedListNode
{
  public:
    int data;
    SinglyLinkedListNode *next;
    SinglyLinkedListNode *randomPointer;

    SinglyLinkedListNode(int node_data)
    {
        this->data = node_data;
        this->next = nullptr;
        this->randomPointer = nullptr;
    }

    // overloaded funtion to directly add constructed node
    void link_random_node(SinglyLinkedListNode *random_node)
    {
        this->randomPointer = random_node;
    }
};

class SinglyLinkedList
{
  public:
    SinglyLinkedListNode *head;
    SinglyLinkedListNode *tail;

    SinglyLinkedList()
    {
        this->head = nullptr;
        this->tail = nullptr;
    }

    void insert_node(int node_data)
    {
        SinglyLinkedListNode *node = new SinglyLinkedListNode(node_data);

        if (!this->head)
        {
            this->head = node;
        }
        else
        {
            this->tail->next = node;
        }

        this->tail = node;
    }

    void insert_node(SinglyLinkedListNode *node)
    {
        if (!this->head)
        {
            this->head = node;
        }
        else
        {
            this->tail->next = node;
        }

        this->tail = node;
    }
};

void print_singly_linked_list_with_random_node(SinglyLinkedListNode *node, string sep)
{   
    string delimitter = " ";
    while (node)
    {
        cout << node->data << delimitter;

        if (node->next != nullptr)
        {
            cout << node->next->data << delimitter;
        }
        else
            cout << -1 << delimitter;

        if (node->randomPointer != nullptr)
        {
            cout << node->randomPointer->data;
        }
        else
        {
            cout << "-1";
        }

        node = node->next;

        if (node)
        {
            cout << sep;
        }
    }
}

bool cloneCheck(SinglyLinkedListNode *head, unordered_set<SinglyLinkedListNode *> originalNodes)
{
    SinglyLinkedListNode *tmp = head;
    while (tmp)
    {
        if (originalNodes.find(tmp) != originalNodes.end())
        {
            return false;
        }
        tmp = tmp->next;
    }
    return true;
}

// ------------------------------ START ------------------------------

/*
 * @param list: pointer to the head node of the original linkedList
 * @returns the pointer to the newly cloned linkedList head node
 * This function clones the provided linkedList
 * Time Complexity : O(N)
 */
SinglyLinkedListNode *cloneLinkedList(SinglyLinkedListNode *list)
{   
    // Step 1:
    // inserting duplicate nodes between the consecutive nodes of 
    // original linked list
    // initial list:
    //  1 -- 2 -- 3 -- 4 -- null  (with some random links at each node)
    // after inserting new duplicate nodes
    //  1 -- {1} -- 2 -- {2} -- 3 -- {3} -- 4 -- {4} -- null
    SinglyLinkedListNode *tmpHead = list;
    while(tmpHead) {
        SinglyLinkedListNode *tmpNext = tmpHead -> next;
        tmpHead->next = new SinglyLinkedListNode(tmpHead->data);
        tmpHead->next->next = tmpNext;
        tmpHead = tmpNext;
    }

    // Step 2:
    // linking the random nodes for cloned nodes corresponding to
    // to its original node 
    tmpHead = list;
    while(tmpHead) {
        // getting the corresponding current node of the cloned list;
        // through out the iteration the "next" node of the current original
        // node tmpHead will give the current node of cloned list
        SinglyLinkedListNode *currentClonedNode = tmpHead->next;

        // getting the random linked node from the original list node
        SinglyLinkedListNode *tmpRandomLinkedNode = tmpHead->randomPointer;

        if(tmpRandomLinkedNode != nullptr) {
        // getting the corresponding random linked node for the cloned node;
        // as the "next" node of the tmpHead->randomPointer will point to the 
        // corresponding the random link node for the current cloned node
        tmpRandomLinkedNode = tmpRandomLinkedNode->next;
        }

        // linking the random pointed node for the current cloned node
        currentClonedNode->randomPointer = tmpRandomLinkedNode;

        // moving to next node of original linked list by jumping
        // two steps odd indexed nodes are original nodes (1-based indexing)
        tmpHead = tmpHead->next->next;
    }

    // Step 3:
    // detaching the cloned node from the original list 
    // and restoring the original list.
    // also extracting the cloned list nodes and forming the 
    // cloned linked list.
    tmpHead = list;
    SinglyLinkedListNode *clonedListHead = nullptr;
    SinglyLinkedListNode *clonedListTail = nullptr;
    while (tmpHead)
    {   
        // getting corresponding cloned node to tmpHead
        SinglyLinkedListNode *currentClonedNode = tmpHead->next;

        // detaching the cloned node and restoring original "next" node
        tmpHead->next = currentClonedNode->next;

        // building/chaining the cloned nodes to form separate linkedlist
        if(clonedListHead == nullptr) {
            clonedListHead = currentClonedNode;
            clonedListTail = clonedListHead;
        }
        else {
            clonedListTail->next = currentClonedNode;
            clonedListTail = clonedListTail->next;
        }

        // moving to next node of original linked list by jumping
        // one step as we have restored original configuration till this node
        tmpHead = tmpHead->next;
    }

    return clonedListHead;
}

// ------------------------------ STOP -------------------------------

int main()
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output.txt", "w",
    //     stdout);

    // freopen(
    //     "..//test_cases//generated_medium_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_medium_test_cases_expected_output.txt", "w",
    //     stdout);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output.txt", "w",
    //     stdout);

    // string testcases;
    // getline(cin,testcases);
    // int t = stoi(ltrim(rtrim(testcases)));
    // while(t--) {
    unordered_map<int, SinglyLinkedListNode *> mapper;
    unordered_set<SinglyLinkedListNode *> originalNodes;
    SinglyLinkedList *List = new SinglyLinkedList();

    string linkedList_count_temp;
    getline(cin, linkedList_count_temp);

    int linkedList_count = stoi(ltrim(rtrim(linkedList_count_temp)));

    for (int i = 1; i <= linkedList_count; i++)
    {
        List->insert_node(i);
        mapper[i] = List->tail;
        originalNodes.insert(List->tail);
    }

    for (int i = 1; i <= linkedList_count; i++)
    {
        string linkedList_item_temp;
        getline(cin, linkedList_item_temp);
        int linkedList_item = stoi(ltrim(rtrim(linkedList_item_temp)));
        if (linkedList_item != -1)
            mapper[i]->link_random_node(mapper[linkedList_item]);
    }

    SinglyLinkedListNode *clonedListHead = cloneLinkedList(List->head);

    if (cloneCheck(clonedListHead, originalNodes) == false)
    {
        cerr << "linked list not cloned";
        assert(false);
    }
    else
    {
        string seperator = "\n";
        // cout << linkedList_count << endl;
        print_singly_linked_list_with_random_node(clonedListHead, seperator);
    }
    // if(t)
    //     cout << endl;
    // }

    return 0;
}

string ltrim(const string &str)
{
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str)
{
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}
'''

