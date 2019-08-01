'''
Add Two Numbers
Write a function which adds two numbers a and b, represented as linked lists of size lenA and lenB respectively, and returning
 the sum c in form of a new linked list.
Ignoring the allocation of a new linked list, try to use constant memory when solving it.
A number is represented by a linked list, with the head of the linked list being the least significant digit. For example
 125 is represented as 5->2->1, and 371 is represented as 1->7->3. Adding 5->2->1(125) and 1->7->3(371) should produce 6->9->4(496).

Input Format
There will be two arguments l_a and l_b, denoting linked lists representing numbers a and b respectively
Output Format
Return result denoting head node of resultant sum linked list.
Constraints
    * 1<= lenA, lenB <= 100000
    * Numbers represented by l_a and l_b will always be non-negative.
    * As digits of number can be [0-9], nodes of linked list l_a and l_b will always have number [0-9].
    * If a or b is 0, then corresponding linked list will contain only one node having value 0. For values greater than 0, there will not be any leading zeros. Same for expected output. If answer is 0, then there must be only one node having value 0 and if answer is greater than 0, then there must not be any leading zeros.

Sample Test Cases
Sample Test Case 1

Sample Input 1
l_a = 7->5->2
l_b = 2->0->3

Sample Output 1
result = 9->5->5

Explanation 1
As l_a = 7->5->2 means number 257 and l_b = 2->0->3 means number 302. Sum of 257 and 302 is 559 so, result will represent
 9->5->5.

Sample Test Case 2
Sample Input 2
l_a = 5->8->3
l_b = 9->4->1

Sample Output 2
result = 4->3->5

Explanation 2
As l_a = 5->8->3 means number 385 and l_b = 9->4->1 means number 149. Sum of 385 and 149 is 534 so, result will represent 4->3->5.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the 'addTwoNumbers' function below.
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
def addTwoNumbers(l_a, l_b):
    pass


if __name__ == '__main__':
    l_a_count = int(input().strip())

    l_a = SinglyLinkedList()

    for _ in range(l_a_count):
        l_a_item = int(input().strip())
        l_a.insert_node(l_a_item)

    l_b_count = int(input().strip())

    l_b = SinglyLinkedList()

    for _ in range(l_b_count):
        l_b_item = int(input().strip())
        l_b.insert_node(l_b_item)

    fptr = sys.stdout
    result = addTwoNumbers(l_a.head, l_b.head)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()

'''
We have provided solutions which contain necessary comments to understand the approach used:
1) other_solution1.java
Description:
Let's have a look at an approach for having sum of two numbers x and y represented in decimal number system:
(Lets say string representation of number is num_str, then Least significant digit means digit represented by character
at 0th index of num_str and Most significant digit means digit represented by character at (len(num_str) - 1)th index of num_str).
    * Add trailing zeroes to make the lengths of x and y equal(in decimal system). Let say this length is N.
    * Set carryForward=0 and i=0.
    * Add ith significant digit of x and y and add carryForward to it(let say this sum 'sumD'). If at ith significant digit, sumD is greater than 9, we carry forward the tenth place digit of sumD to the next significant digit.
    * Set carryForward = sumD/10 and ith significant digit of result to sumD % 10.
    * i=i+1, Repeat #3 till i<=N-1.
    * If carryForward>0, set nth significant digit of result as carryForward.
    * Return result.
    
Now, as numbers are represented as a linked list, with the head of the linked list being the least significant digit, ith
node in linked list will be ith least significant digit of the number. We need to start traversing linked lists corresponding
to given two numbers starting from their heads and follow the above mentioned steps.

In this solution, we are creating extra linked list to store resultant sum. In actual interview, ignore the allocation of
a new linked list, try to use constant memory when solving it. But if interviewer asks for the solution which does not
modify the input linked lists, then this is the expected solution.
 
Time Complexity:
O(Math.max(lenA, lenB)) where lenA and lenB is length of given linked list l_a and l_b respectively.
As we are iterating over given linked list l_a and l_b simultaneously in one iteration. Hence complexity is maximum of length
 of l_a and length l_b.
Auxiliary Space Used:
O(Math.max(lenA, lenB)) where lenA and lenB is length of given linked list l_a and l_b respectively.
We are storing resultant sum by creating new linkedlist and size of that newly created linked list can be 1 + Math.max(lenA,
 lenB).
Space Complexity:
O(lenA+lenB) where lenA and lenB is length of given linked list l_a and l_b respectively.
Input will have two linked lists l_a and l_b of lenA and lenB respectively so, input takes O(lenA+lenB) and auxiliary space
 used is O(Math.max(lenA, lenB)).
So, O(lenA+lenB) + O(Math.max(lenA, lenB)) → O(lenA+lenB)



2) other_solution2.java
Description:
Approach will be as similar as explained other_solution1, but this approach is bit optimised in terms of space used as we
will not create new linked list to store resultant sum rather than use one of the linked list l_a or l_b. We are iterating
over given two linked lists to find out which one is longer and always making sure that l_b will always be longer linked
list to store resultant sum if not then by swapping l_a and l_b.
Time Complexity:
O(lenA+lenB) where lenA and lenB is length of given linked list l_a and l_b respectively.
As we are iterating over two given linked list l_a and l_b. Hence complexity is sum of length of these two given linked
 lists.
Auxiliary Space Used:
O(1).

We aren’t storing anything extra and using one of the two given linked list to store the resultant sum.
Space Complexity:
O(lenA+lenB) where lenA and lenB is length of given linked list l_a and l_b respectively.
Input will have two linked lists l_a and l_b of lenA and lenB respectively so, input takes O(lenA+lenB) and auxiliary space
 used is O(1).
So, O(lenA+lenB) + O(1) → O(lenA+lenB)

3) optimal_solution.java
Description:
Approach will be as similar as explained other_solution1, but this approach is optimised in terms of number of iterations
 and extra space used as we are storing the resultant value in one of the given two input linked list only so, we don’t
 require to create and allocate new linked list.
And we are not finding the longer linked list by iterating over given two linked list as we were doing in other_solution2
 but when finding the resultant sum we are changing the pointer and appending the longer list’s remaining nodes to the linked
 list in which we are storing the resultant sum.
For more detailed explanation refer optimal_solution.
Time Complexity:
O(Math.max(lenA, lenB)) where lenA and lenB is length of given linked list l_a and l_b respectively.
As we are iterating over given linked list l_a and l_b simultaneously in one iteration. Hence complexity is maximum of length
 of l_a and length l_b.
Auxiliary Space Used:
O(1).
We aren’t storing anything extra and using one of the two given linked list to store the resultant sum.
Space Complexity:
O(lenA+lenB) where lenA and lenB is length of given linked list l_a and l_b respectively.
Input will have two linked lists l_a and l_b of lenA and lenB respectively so, input takes O(lenA+lenB) and auxiliary space
 used is O(1).
So, O(lenA+lenB) + O(1) → O(lenA+lenB)
'''
'''
import java.io.*;

class SinglyLinkedListNode {
    public int data;
    public SinglyLinkedListNode next;

    public SinglyLinkedListNode(int nodeData) {
        this.data = nodeData;
        this.next = null;
    }
}

class SinglyLinkedList {
    public SinglyLinkedListNode head;
    public SinglyLinkedListNode tail;

    public SinglyLinkedList() {
        this.head = null;
        this.tail = null;
    }

    public void insertNode(int nodeData) {
        SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

        if (this.head == null) {
            this.head = node;
        } else {
            this.tail.next = node;
        }

        this.tail = node;
    }
}

class SinglyLinkedListPrintHelper {
    public static void printList(SinglyLinkedListNode node, String sep, BufferedWriter bufferedWriter) throws IOException {
        while (node != null) {
            bufferedWriter.write(String.valueOf(node.data));

            node = node.next;

            if (node != null) {
                bufferedWriter.write(sep);
            }
        }
    }
}

class Result {

    /*
     * Complete the 'addTwoNumbers' function below.
     *
     * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
     */
    
    // ============================ Start ============================

    static SinglyLinkedListNode addTwoNumbers(SinglyLinkedListNode l_a, SinglyLinkedListNode l_b) {
        
        SinglyLinkedListNode result = l_b;
        // We are storing resultant sum in l_b.
        int carryForward = 0, sum=0;
        // To store carry and current sum.
        // We are iterating till we reach at end of one of linkedlist.
        // and update l_b with resultant sum.
        while(true){
            sum = l_a.data + l_b.data + carryForward;
            l_b.data = sum%10;
            carryForward = sum/10;
            if(l_a.next == null || l_b.next == null){
                break;
            }
            l_a = l_a.next;
            l_b = l_b.next;
        }
        // If we reached at end of l_b but l_a is still remaining then we point next of l_b to next of l_a. So, we can utilise already created linkedlist node of l_a by appending it with l_b.
        if(l_a.next != null && l_b.next == null){
            l_b.next = l_a.next;
        }
        // We iterate through remaining nodes of l_b and update it with sum of node and carry.
        while(carryForward > 0 && l_b.next != null){
            l_b = l_b.next;
            sum = carryForward + l_b.data;
            l_b.data = sum%10;
            carryForward = sum/10;
        }
        // If still carry is remaining then we add extra node at tail of linkedlist l_b.
        if(carryForward > 0){
            SinglyLinkedListNode new_node = new SinglyLinkedListNode(carryForward);
            l_b.next = new_node;
        }
        // Result will be head node of l_b (which is storing our resultant sum)
        return result;
    }
    
    // ============================ End =============================
}


class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        SinglyLinkedList l_a = new SinglyLinkedList();

        int lenA = Integer.parseInt(bufferedReader.readLine().trim());

        for (int i = 0; i < lenA; i++) {
            int node = Integer.parseInt(bufferedReader.readLine().trim());

            l_a.insertNode(node);
        }

        SinglyLinkedList l_b = new SinglyLinkedList();

        int lenB = Integer.parseInt(bufferedReader.readLine().trim());

        for (int i = 0; i < lenB; i++) {
            int node = Integer.parseInt(bufferedReader.readLine().trim());

            l_b.insertNode(node);
        }

        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        SinglyLinkedListNode result = Result.addTwoNumbers(l_a.head, l_b.head);

        SinglyLinkedListPrintHelper.printList(result, "\n", bufferedWriter);
        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}

/**
 * Time complexity: O(lenA+lenB)
 * Space complexity: O(lenA+lenB)
 */
'''


