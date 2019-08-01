'''
Merge Sort A Linked List
Problem Statement:
You are given a singly linked list. You have to sort the linked list using merge sort algorithm in ascending order.
Input/Output Format For The Function:
Input Format:
The function contains a single argument, the head node of the linked list head.
Output Format:
Return the head of the sorted linked list.
Input/Output Format For The Custom Input:
Input Format:
First line contains integer n, the number of integers. The next n lines contains an integer each.
If linked list is 1->2->4->3 then input should be:
4
1
2
4
3
Output Format:
The function should return the head of the sorted linked list. The inbuilt print function will print each integer of the
 linked list starting from head in a new line.
For above input, output will be
1
2
3
4
You should have correctly returned the head, in this case the node containing data as 1, after sorting the linked list.

Constraints:
    * 1 <= n <= 10^5
    * -10^9 <= value of each node of linked list <= 10^9

Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
4
0
1
10
7
Sample Output 1:
0
1
7
10
Explanation 1:
We see that the linked list is sorted in increasing order as 0<1<7<10.
Sample Test Case 2:
Sample Input 2:
3
1
2
3
Sample Output 2:
1
2
3
Explanation 2:
We see that the input is already sorted and so is the output linked list. It is correctly sorted in increasing order as
 1<2<3.
'''
#!/bin/python3


import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000100)

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

#
# Complete the 'merge_sort' function below.
#
# The function accepts the head of the linked list as parameter.
#

def merge_sort(head):
    pass


if __name__ == '__main__':
    fptr = sys.stdout

    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    result = merge_sort(head.head)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()

'''
Merge Sort A Linked List
We have provided 2 solutions which contain necessary comments to understand the approach used.
1) recursive solution.java
Description:
We are given a linked list. Now we will implement merge sort algorithm to sort the integers in this linked list. Merge sort
 algorithm is a divide and conquer algorithm. At each step, we split the linked list by the current middle element and sort
 both of these 2 new lists separately. After sorting these 2 lists we merge them. We keep on performing this step of splitting
 the current list and then merging the 2 smaller lists until we reach lists of size 1 when we can simply return the elements.
 Finally, the list gets sorted after all the steps. For more details, refer to the code given in solution.java.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*logn) considering the size of the linked list is n.
Here we keep on splitting the linked lists into halves until we reach linked list of size 1. For each of these sub linked
 lists, we sort them separately and merge them. Hence, after sorting and merging all the sub linked lists, the time complexity
 turns out to be O(n*logn).
Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) + Theta(n)
The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in case II of Master Method
 and solution of the recurrence is Theta(n*logn).
Time complexity of MergeSort is Theta(n*logn) in all 3 cases (worst, average and best) as merge sort always divides the
 linked list into two halves and takes linear time to merge two halves.
Time Complexity:
O(n*logn) considering the size of the linked list is n.
As time complexity assuming that input arguments are already given and excluding time used in declaration of output is O(n*logn),
 to read input it will take O(n) and to store output it will take O(n) hence total complexity will be O(n*logn) + O(n) +
 O(n) → O(n*logn).
Auxiliary Space Used:
O(logn) considering the size of the linked list is n.
Here, at each step of splitting the linked list, no extra memory is used as sorting is done in place to the smaller sub
 linked lists. These sub linked lists are then merged to form the original linked list over a series of steps. However,
 the mergesort algorithm is recursive, so it requires O(logn) stack space as at each step the current linked list gets halved
 until the size becomes one. Hence the stack space required is O(logn) which brings up the auxiliary space to O(logn).
Space Complexity:
O(n) considering the size of the linked list is n.
The input linked list is of size n, so the input space complexity is O(n), and auxiliary space used is O(logn) and output
 uses O(n), hence total complexity will be O(n).
 
 
 
 
2) iterative solution.java
Description:
We are given a linked list. Now we use the iterative approach of merge sort algorithm to sort the given linked list. We
 start by dividing the linked list into blocks of size 1,2,4,8... and so on. For each of these blocks, we divide the linked
 list into corresponding sub linked lists of the size equal to block size and then sort them. Finally, we merge the sorted
 sub linked lists and obtain the final sorted linked list. For more details, refer to the code given in iterative_solution.java.

Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*logn) considering the size of the linked list is n.
Here we iterate over block sizes starting from 1 and then move on in multiples of 2, that is, 2, 4, 8... and so on. For
 each of these block sizes, we take 2 consecutive sub linked lists of that size over the entire linked list. So for a block
 size of 1, there will be 2 sub linked lists of size 1 and we then sort them separately and merge them. We do this over
 the entire linked list. So for each block size, we require O(n) time to sort the sub linked lists and merge them. Hence,
 after sorting and merging all the sub linked lists, for all the block sizes, 1,2,4,8,...,log2(n) the time complexity turns
 out to be O(n*logn).
Time Complexity:
O(n*logn) considering the size of the linked list is n.
As time complexity assuming that input arguments are already given and excluding time used in declaration of output is O(n*logn),
 to read input it will take O(n) and to store output it will take O(n) hence total complexity will be O(n*logn) + O(n) +
 O(n) → O(n*logn).
Auxiliary Space Used:
O(1) considering the size of the linked list is n.
Here, at each step of splitting the linked list, no extra memory is used as sorting is done in place to the smaller sub
 linked lists. These sub linked lists are created at each step of splitting. These sub linked lists are then merged to form
 the original linked list over a series of steps.
Space Complexity:
O(n) considering the size of the linked list is n.
The input linked list is of size n, so the input space complexity is O(n), and auxiliary space used is O(1) and output uses
 O(n), hence total complexity will be O(n).
'''
'''
RECURSIVE SOLUTION
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

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
        SinglyLinkedListNode SinglyLinkedListNode = new SinglyLinkedListNode(nodeData);

        if (this.head == null) {
            this.head = SinglyLinkedListNode;
        } else {
            this.tail.next = SinglyLinkedListNode;
        }

        this.tail = SinglyLinkedListNode;
    }
}

class SinglyLinkedListPrintHelper {
    public static void printList(SinglyLinkedListNode SinglyLinkedListNode, String sep, BufferedWriter bufferedWriter)
            throws IOException {
        while (SinglyLinkedListNode != null) {
            bufferedWriter.write(String.valueOf(SinglyLinkedListNode.data));

            SinglyLinkedListNode = SinglyLinkedListNode.next;

            if (SinglyLinkedListNode != null) {
                bufferedWriter.write(sep);
            }
        }
    }
}

class Result {

    /*-------------------START----------------------*/
    public static SinglyLinkedListNode merge_sort(SinglyLinkedListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        // get the middle of the list
        SinglyLinkedListNode middle = split(head);
        SinglyLinkedListNode nextofmiddle = middle.next;

        // set the next of middle SinglyLinkedListNode to null
        middle.next = null;

        // Apply split on left list
        SinglyLinkedListNode left = merge_sort(head);

        // Apply split on right list
        SinglyLinkedListNode right = merge_sort(nextofmiddle);

        // Merge the left and right lists
        SinglyLinkedListNode sortedlist = merge(left, right);
        return sortedlist;
    }

    public static SinglyLinkedListNode merge(SinglyLinkedListNode list1, SinglyLinkedListNode list2) {
        SinglyLinkedListNode result = null;
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }

        // Pick either list1 or list2 and recur the merge method
        if (list1.data <= list2.data) {
            result = list1;
            result.next = merge(list1.next, list2);
        } else {
            result = list2;
            result.next = merge(list1, list2.next);
        }
        return result;
    }

    public static SinglyLinkedListNode split(SinglyLinkedListNode head) {
        // Base case
        if (head == null) {
            return head;
        }
        SinglyLinkedListNode fast = head.next;
        SinglyLinkedListNode slow = head;

        // Move fast by two and slow by one
        // Finally slow will point to middle SinglyLinkedListNode
        while (fast != null) {
            fast = fast.next;
            if (fast != null) {
                slow = slow.next;
                fast = fast.next;
            }
        }
        return slow;
    }
    /*-------------------END----------------------*/

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
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        SinglyLinkedList head = new SinglyLinkedList();

        int headCount = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, headCount).forEach(i -> {
            try {
                int headItem = Integer.parseInt(bufferedReader.readLine().trim());

                head.insertNode(headItem);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        SinglyLinkedListNode result = Result.merge_sort(head.head);

        SinglyLinkedListPrintHelper.printList(result, "\n", bufferedWriter);
        bufferedWriter.newLine();

        bufferedWriter.close();

        bufferedReader.close();
    }
}
'''
'''
ITERATIVE SOLUTION
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

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
        SinglyLinkedListNode SinglyLinkedListNode = new SinglyLinkedListNode(nodeData);

        if (this.head == null) {
            this.head = SinglyLinkedListNode;
        } else {
            this.tail.next = SinglyLinkedListNode;
        }

        this.tail = SinglyLinkedListNode;
    }
}

class SinglyLinkedListPrintHelper {
    public static void printList(SinglyLinkedListNode SinglyLinkedListNode, String sep, BufferedWriter bufferedWriter)
            throws IOException {
        while (SinglyLinkedListNode != null) {
            bufferedWriter.write(String.valueOf(SinglyLinkedListNode.data));

            SinglyLinkedListNode = SinglyLinkedListNode.next;

            if (SinglyLinkedListNode != null) {
                bufferedWriter.write(sep);
            }
        }
    }
}

class Result {

    /*-------------------START----------------------*/
   public static SinglyLinkedListNode merge_sort(SinglyLinkedListNode head) throws IOException {
        if (head == null) {
            return head;
        }
        SinglyLinkedListNode node1 = null, node3 = null;
        SinglyLinkedListNode node2 = null, node4 = null;
        SinglyLinkedListNode prev = null;
        // get the length of the current linked list
        int len = getLengthOfLinkedList(head);

        // we will loop over block sizes starting from 1 and then doubling it every time
        // that is 1,2,4,...,log(n).
        for (int block = 1; block < len; block = block * 2) {
            node1 = head;
            while (node1 != null) {

                boolean flag = false;

                // If this is first iteration we mark flag as true
                if (node1 == head) {
                    flag = true;
                }

                // First sub linked list for merging
                int cnt = block;
                node3 = node1;
                while (--cnt > 0 && node3.next != null) {
                    node3 = node3.next;
                }

                // Second sub linked list for merging
                node2 = node3.next;
                if (node2 == null) {
                    break;
                }
                cnt = block;
                node4 = node2;
                while (--cnt > 0 && node4.next != null) {
                    node4 = node4.next;
                }

                // To store for next iteration.
                SinglyLinkedListNode temp = node4.next;

                // Making sure that first node of second list is higher.
                SinglyLinkedListNode tempo = null;
                if ((node1).data > (node2).data) {
                    SinglyLinkedListNode n = node1;
                    node1 = node2;
                    node2 = n;
                    n = node3;
                    node3 = node4;
                    node4 = n;
                }

                // Merging the nodes of the 2 linked lists
                SinglyLinkedListNode start1 = node1, end1 = node3;
                SinglyLinkedListNode start2 = node2, end2 = node4;
                SinglyLinkedListNode next = (node4).next;

                // we merge in such a way that start1 is always less than start2
                while (start1 != end1 && start2 != next) {
                    if (start1.next.data > start2.data) {
                        tempo = start2.next;
                        start2.next = start1.next;
                        start1.next = start2;
                        start2 = tempo;
                    }
                    start1 = start1.next;
                }

                if (start1 == end1) {
                    start1.next = start2;
                } else {
                    node4 = node3;
                }

                // Update head for first iteration, else append after previous list
                if (flag) {
                    head = node1;
                } else {
                    prev.next = node1;
                }

                prev = node4;
                node1 = temp;
            }
            prev.next = node1;
        }
        return head;
    }

    public static int getLengthOfLinkedList(SinglyLinkedListNode head) {
        int cnt = 0;
        while (head != null) {
            cnt++;
            head = head.next;
        }
        return cnt;
    }
    /*-------------------END----------------------*/

}

class Solution {
    public static void main(String args[]) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        SinglyLinkedList head = new SinglyLinkedList();

        int headCount = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, headCount).forEach(i -> {
            try {
                int headItem = Integer.parseInt(bufferedReader.readLine().trim());

                head.insertNode(headItem);
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        SinglyLinkedListNode result = Result.merge_sort(head.head);

        SinglyLinkedListPrintHelper.printList(result, "\n", bufferedWriter);
        bufferedWriter.newLine();

        bufferedWriter.close();

        bufferedReader.close();
    }
}
'''
