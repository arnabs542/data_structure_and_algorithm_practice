'''
Zip Given Linked List From Ends
Problem Statement:
Given an integer singly linked list L of size n, zip it from its two ends.
What does zipping mean?
Given a singly linked list L: L1 -> L2 ->… -> Ln-1 -> Ln -> NULL, rearrange the nodes in the list so that the new formed
 linked list is :
L1 -> Ln -> L2 -> Ln-1 -> L3 -> Ln-2 …
You have to do it in-place i.e. in the same linked list given in input, using only constant extra space.
(Looking at the sample test case will make it more clear.)
Input/Output Format For The Function:
Input Format:
There is only one argument in input, denoting integer singly linked list L.
Output Format:
Return zipped linked list resL.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting size of input linked list L. In next n lines, ith line should
 contain an integer Li, denoting value in ith node of L.
If n = 6 and L: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL, then input should be:
6
1
2
3
4
5
6
Output Format:
There will be n lines, where ith line contains value of ith node of resL. Here, resL is the resultant linked list returned
 by the solution function.
For input n = 6 and L: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL, output will be:
1
6
2
5
3
4

Constraints:
    * 0 <= n <= 100000
    * -2 * 10^9 <= value stored in any node <= 2 * 10^9
Sample Test Case:
Sample Input:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
Sample Output:
1 -> 6 -> 2 -> 5 -> 3 -> 4 -> NULL
(Other modification to try yourself for practice: zip two separate lists and unzip them back into original lists. i.e. unzip(zip(L1,
 L2)) should return L1 and L2.)
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
def zip_given_linked_list(head):
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


    res = zip_given_linked_list(head)

    while res != None:
        f.write(str(res.val))

        if res.next:
            f.write('\n')
        res = res.next

    f.write('\n')
    f.close()

'''
Suppose given a linked list is 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL. So zip of this linked list is defined as 1 -> 6 -> 2
 -> 5 -> 3 -> 4 -> NULL. 
The task is to achieve desired linked list using O(1) space.
This can be performed by a simple algorithm:
Split the list from the middle into two lists. We are splitting the list into two and not creating a new linked list hence
 maintaining O(1) space.
Now we have two lists : list1: 1 -> 2 -> 3 -> NULL and list2: 4 -> 5 -> 6 -> NULL. 
Reverse the second list.
This gives us two lists list1: 1 -> 2 -> 3 -> NULL and list2: 6 -> 5 -> 4 -> NULL.
Now merge the lists picking one node from each list as a time, merged: 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> NULL.
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

const int MIN_N = 0, MAX_N = 100000, MIN_VAL = -2000000000, MAX_VAL = 2000000000;

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

// Reverse singly linked list in O(len) time and O(1) space. 
LinkedListNode *reverse_linked_list(LinkedListNode *cur)
{
	LinkedListNode *prev = NULL;
	LinkedListNode *next;
	while (cur)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	return prev;
}

LinkedListNode *zip_given_linked_list(LinkedListNode *head)
{
	if (head == NULL)
	{
		return NULL;
	}
	/*
	Using slow-fast technique find the middle element.
	If head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL,
	then slow should stop at 3.
	*/ 
	LinkedListNode *slow = head;
	LinkedListNode *fast = head->next;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/*
	Separate linked lists from middle. 
	list1: 1 -> 2 -> 3 -> NULL
	list2: 4 -> 5 -> 6 -> NULL
	*/
	LinkedListNode *list1 = head;
	LinkedListNode *list2 = slow->next;
	/*
	Till now:
	1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
	With list1 pointing to 1, list2 pointing to 4 and slow pointing to 3.

	Now break main linked list into two parts.
	So do 3->next = NULL.
	*/
	slow->next = NULL;
	/*
	From
	list2: 4 -> 5 -> 6 -> NULL
	to 
	list2: 6 -> 5 -> 4 -> NULL
	*/
	list2 = reverse_linked_list(list2);
	/*
	Instead of defining two new pointers next1 and next2, we can use previously defined slow and 
	fast to save memory, but for readability purpose we have used two new pointers.
	*/
	LinkedListNode *next1;
	LinkedListNode *next2;
	/*
	Merge list1 and list2.
	list1: 1 -> 2 -> 3 -> NULL
	list2: 6 -> 5 -> 4 -> NULL
	merged: 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> NULL
	*/
	while (list2)
	{
		next1 = list1->next;
		next2 = list2->next;
		list1->next = list2;
		list2->next=next1;
		list1 = next1;
		list2 = next2;
	}
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

		LinkedListNode *ans = zip_given_linked_list(head);
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
