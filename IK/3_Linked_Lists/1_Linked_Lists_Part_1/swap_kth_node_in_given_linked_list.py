'''
Swap kth Nodes In Given Linked List
Problem Statement:
Given an integer singly linked list L of size n, and an integer k, you have to swap kth (1-indexed) node from the beginning,
with kth node from the end.
Note that you have to swap the nodes themselves, not just the contents.

Input/Output Format For The Function:
Input Format:
There are two arguments in input. First is an integer singly linked list L and second is an integer k.
Output Format:
Return resultant linked list resL, after swapping kth nodes of L.

Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting size of input linked list L. In next n lines, ith line should
contain an integer Li, denoting value in ith node of L. In the next line, there should be an integer k, denoting the size
of group as explained in problem statement section.
If n = 6, L: 1 -> 2 -> 3 -> 4 -> 7 -> 0 -> NULL and k = 2, then input should be:
6
1
2
3
4
7
0
2

Output Format:
There will be n lines, where ith line contains value of ith node of resL. Here, resL is the resultant linked list returned
by the solution function.
For input n = 6, L: 1 -> 2 -> 3 -> 4 -> 7 -> 0 -> NULL and k = 2, output will be:
1
7
3
4
2
0

Constraints:
    * 1 <= n <= 100000
    * -2 * 10^9 <= value stored in any node <= 2 * 10^9
    * 1 <= k <= n
    * Try to access linked list nodes minimum number of times.

Sample Test Case:
Sample Input:
list: 1 -> 2 -> 3 -> 4 -> 7 -> 0 -> NULL
k: 2
Sample Output:
1 -> 7 -> 3 -> 4 -> 2 -> 0 -> NULL
Notes:
Suggested time in interview: 30 minutes.
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework i.e.
 For the first attempt of a given homework problem, the focus should be to understand what the problem is asking, what approach
 you are using, coding it, as well as identifying any gaps that you can discuss during a TA session. Take your time, but
 limit yourself to 2 one hour sessions for most problems.
'''
# !/bin/python

import os
import sys


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

'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
def swap_nodes(head, k):
    pass


if __name__ == "__main__":
    f = sys.stdout

    head_size = int(input())

    head = None
    head_tail = None

    for head_i in range(head_size):

        head_item = int(input())

        head_tail = _insert_node_into_singlylinkedlist(head, head_tail, head_item)

        if head_i == 0:
            head = head_tail


    k = int(input())

    res = swap_nodes(head, k)

    while res != None:
        f.write(str(res.val))

        if res.next:
            f.write('\n')
        res = res.next

    f.write('\n')
    f.close()

'''
Have you considered "Try to access linked list nodes minimum number of times."?
If you have done:
1) First find linked list length n.
2) Then find k th node.
3) Then n - k + 1 th node.
4) Swap nodes. 
Then this is not the optimal solution.
Note that while finding length of linked list we could have found the kth node in the same loop!  
Now this is optimal solution. 
Also there is other optimal solution possible and we have presented that in optimal_solution.cpp.
Time Complexity:
O(n).
Auxiliary Space Used:
O(1). 
Space Complexity:
O(n).
As input is O(n) and auxiliary space used is O(1). So, O(n) + O(1) -> O(n). 
'''
'''
#include<bits/stdc++.h>

using namespace std;

const int MIN_N = 1, MAX_N = 100000, MIN_VAL = -2000000000, MAX_VAL = 2000000000;

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

LinkedListNode *insert_node_into_singly_linked_list(LinkedListNode *tail, int val)
{
	LinkedListNode *temp = new LinkedListNode(val);
	if (tail != NULL)
	{
		tail->next = temp;
	}
	return temp;
}

// -------------------------- START --------------------------

LinkedListNode *swap_nodes(LinkedListNode *head, int k)
{
	/*
	ptr1 will point to kth node from beginning and prev1 will point to its previous node.
	If ptr1 is head then prev1 will be NULL.
	*/
	LinkedListNode *prev1 = NULL;
	LinkedListNode *ptr1 = head;
	while(--k)
	{
		prev1 = ptr1;
		ptr1 = ptr1->next;
	}
	/*
	ptr2 will point to kth node from end and prev2 will point to its previous node.
	If ptr2 is head then prev2 will be NULL.

	If we set temp at kth node from beginning and ptr2 at head, 
	and we keep on increasing both till temp reaches last node,
	then ptr2 will be at the kth node from end.

	Let's understand why? - 
	When we started distance between ptr2 and temp is k - 1 links.
	We have incremented both temp and ptr2 same no of times, hence at the end also distance 
	between ptr2 and 
	temp will be k - 1 links. 
	Now temp is at last node hence ptr2 will be at kth node from end! 

	Try few examples to understand it clearly.  
	*/
	LinkedListNode *temp = ptr1;
	LinkedListNode *prev2 = NULL;
	LinkedListNode *ptr2 = head;
	while (temp->next)
	{
		temp = temp->next;
		prev2 = ptr2;
		ptr2 = ptr2->next;
	}
	if (prev1 != NULL)
	{
		// Link previous node of ptr1 to ptr2.
		prev1->next = ptr2;
	}
	else
	{
		// prev1 == NULL means ptr1 is head hence after swap, ptr2 will become head. 
		head = ptr2;
	}
	if (prev2 != NULL)
	{
		// Link previous node of ptr2 to ptr1.
		prev2->next = ptr1;
	}
	else
	{
		// prev2 == NULL means ptr2 is head hence after swap, ptr1 will become head.
		head = ptr1;
	}
	// Swap next pointers of ptr1 and ptr2.
	temp = ptr1->next;
	ptr1->next = ptr2->next;
	ptr2->next = temp;
	return head;
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
	assert(test_cases >= 0);
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(MIN_N <= n);
		assert(n <= MAX_N);

		LinkedListNode *head = NULL, *tail = NULL;

		for (int i = 0; i < n; i++)
		{
			int val;
			cin >> val;
			assert(MIN_VAL <= val);
			assert(val <= MAX_VAL);

			tail = insert_node_into_singly_linked_list(tail, val);
			if (head == NULL)
			{
				head = tail;
			}
		}
		int k;
		cin >> k;
		assert(1 <= k);
		assert(k <= n);

		LinkedListNode *ans = swap_nodes(head, k);
		while (ans != NULL)
		{
			cout << ans->val << endl;
			ans = ans->next;
		}
		cout << endl;
	}

	return 0;
}
'''

