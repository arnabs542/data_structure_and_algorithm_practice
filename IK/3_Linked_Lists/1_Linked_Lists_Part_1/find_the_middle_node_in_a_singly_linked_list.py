'''
Find The Middle Node In A Singly Linked List
Problem Statement:
Given an integer singly linked list L, you have to find the middle node of it. L has total n no. of nodes.
If it has even number of nodes, then consider the second of the middle two nodes as the middle node.
Input/Output Format For The Function:
Input Format:
There is only one argument in input, L, denoting head node of input integer singly linked list.
Output Format:
Return the middle node of the given integer singly linked list middle.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting total number of nodes in L. In the next n lines, ith line
 should contain an integer Li, denoting a value in ith node of L.
If n = 4 and L: 3 -> 7 -> 2 -> 9 -> NULL, then input should be:
4
3
7
2
9

Output Format:
There will be one line, containing an integer middle, denoting the result returned by the solution function.
For input n = 4 and L: 3 -> 7 -> 2 -> 9 -> NULL, output will be:
2

Constraints:
    * 0 <= n <= 10^5
* -2 * 10^9 <= value contained in any node <= 2 * 10^9
* Do it in one pass over the linked list.
* If given linked list is empty then return null.

Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
1 -> 2 -> 3 -> 4 -> 5 -> NULL
Sample Output 1:
Node containing value 3.
Sample Test Case 2:
Sample Input 2:
1 -> 2 -> 3 -> 4 -> NULL
Sample Output 2:
Node containing value 3.
Notes:
Suggested time in interview: 20 minutes.
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework i.e.
For the first attempt of a given homework problem, the focus should be to understand what the problem is asking, what approach
you are using, coding it, as well as identifying any gaps that you can discuss during a TA session. Take your time, but
limit yourself to 2 one hour sessions for most problems.
'''
#!/bin/python3

import sys
import os

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail

# Complete the function below.

#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}
def find_middle_node(head):
    pass


if __name__ == "__main__":
    f = sys.stdout

    head = None
    head_tail = None
    head_size = int(input())
    head_i = 0
    while head_i < head_size:
        head_item = int(input())

        head_tail = _insert_node_into_singlylinkedlist(head, head_tail, head_item)
        if head_i == 0:
            head = head_tail
        head_i += 1


    res = find_middle_node(head);
    while (res != None):
        f.write(str(res.val) + "\n")
        res = res.next;



    f.close()

'''
A typical solution involves computing the length of the list and then traversing exactly half of that. 
A faster approach is to use a slow pointer and a fast pointer, with the faster one traversing twice as fast. 
By the time the fast one reaches the end of the list, the slower one is at the mid-point. This is still O(n) but is faster
than previous one.
Have a look at the solution provided by us.
Time Complexity:
O(n).
Auxiliary Space Used:
O(1).
Space Complexity:
O(n).
As input is O(n) and auxiliary space used is O(1). So O(n) + O(1) -> O(n).
'''
'''
#include<bits/stdc++.h>

using namespace std;

const int MAX_N = 100000, MAX_NO = 2000000000;

class LinkedListNode
{
public:
	int val;
	LinkedListNode *next;

	LinkedListNode(int _val)
	{
		val = _val;
		next = NULL;
	}
};

LinkedListNode * insert_node_into_singly_linked_list(LinkedListNode * tail, int val)
{
	LinkedListNode *temp = new LinkedListNode(val);
	if (tail != NULL)
	{
		tail->next = temp;
	}
	return temp;
}

// -------------------------- START --------------------------

LinkedListNode* find_middle_node(LinkedListNode* head)
{
	LinkedListNode *slow_ptr = head;
	LinkedListNode *fast_ptr = head;
	while (fast_ptr && fast_ptr->next)
	{
		// Forward two steps.
		fast_ptr = fast_ptr->next->next;
		// Forward one step.
		slow_ptr = slow_ptr->next;
	}
	return slow_ptr;
}

// -------------------------- STOP ---------------------------

int main()
{
	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	assert(test_cases > 0);
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(0 <= n);
		assert(n <= MAX_N);
		LinkedListNode *head = NULL;
		LinkedListNode *tail = NULL;
		for (int i = 0; i < n; i++)
		{
			int val;
			cin >> val;
			assert(-MAX_NO <= val);
			assert(val <= MAX_NO);
			tail = insert_node_into_singly_linked_list(tail, val);
			if (head == NULL)
			{
				head = tail;
			}
		}
		LinkedListNode *middle_node = find_middle_node(head);
		while (middle_node)
		{
			cout << middle_node->val << endl;
			middle_node = middle_node->next;
		}
		cout << endl;
	}

	return 0;
}
'''
