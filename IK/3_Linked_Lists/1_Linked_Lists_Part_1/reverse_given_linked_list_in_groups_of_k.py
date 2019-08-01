'''
Reverse Given Linked List In Groups Of k
Problem Statement:
Given an integer singly linked list L, of size n, and an integer k, you have to reverse every k nodes of the linked list.

There are two cases possible:
1) When n % k = 0: There will be n / k  groups of size k. So, you have to reverse n / k  groups of size k.
2) When n % k != 0: Considering first (floor(n / k) * k) nodes, there will be floor(n / k) groups of size k and one group
 made of last few nodes of size n % k. So, you have to reverse
floor(n / k) groups of size k and one group of size n % k.

(Looking at sample test cases will make it more clear.)

Input/Output Format For The Function:
Input Format:
There are two arguments in input. First is an integer singly linked list L and second is an integer k.
Output Format:
Return resultant linked list resL, after reversing L in groups of k, as asked in problem statement.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting size of input linked list L. In next n lines, ith line should
contain an integer Li, denoting value in ith node of L. In the next line, there should be an integer k, denoting the size
of group as explained in problem statement section.

If n = 6, L: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL and k = 3, then input should be:
6
1
2
3
4
5
6
3

Output Format:
There will be n lines, where ith line contains value of ith node of resL. Here, resL is the resultant linked list returned
by the solution function.

For input n = 6, L: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL and k = 3, output will be:
3
2
1
6
5
4

Constraints:
    * 1 <= n <= 100000
    * -2 * 10^9 <= value stored in any node <= 2 * 10^9
    * 1 <= k <= n

Solve it with constant extra space.
Sample Test Case:
Sample Test Case 1:
Sample Input 1:
list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
k: 3
Sample Output 1:
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> NULL
Explanation 1:
n = 6, k = 3 hence n % k = 0. So there are n / k = 6 / 3 = 2 groups of size k = 3.
Groups to be reversed are (1 -> 2 -> 3) and (4 -> 5 -> 6).
Sample Test Case 2:
Sample Input 2:
list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL
k: 3
Sample Output 2:
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7-> NULL
Explanation 2:
n = 8, k = 3 hence n % k != 0, so there are floor(n / k) = floor(8 / 3) = 2 groups of size k = 3 and one group of size n
 % k = 8 % 3 = 2.
Groups to be reversed are (1 -> 2 -> 3), (4 -> 5 -> 6) and (7 -> 8).
Notes:
Suggested time in interview: 40 minutes.
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
def reverse_linked_list_in_groups_of_k(head, k):
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

    res = reverse_linked_list_in_groups_of_k(head, k)

    while res != None:
        f.write(str(res.val))

        if res.next:
            f.write('\n')
        res = res.next

    f.write('\n')
    f.close()


'''
Have you considered "Solve it with constant extra space."?
If you are using recursion, then it will be O(n / k) extra space due to recursion depth and when k = 1 it will be O(n) extra space!
Have a look at optimal_solution.cpp, it contains necessary comments to understand the solution. 
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

// Reverse singly linked list in O(len) time and O(1) space. 
void reverse_linked_list(LinkedListNode *cur)
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
}

LinkedListNode *reverse_linked_list_in_groups_of_k(LinkedListNode *head, int k)
{
	/*
	Input:
	list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL
	k: 3
	Output:
	3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7-> NULL
	Groups to be reversed are (1 -> 2 -> 3), (4 -> 5 -> 6) and (7 -> 8).

	We will call reverse_linked_list function when (start = 1 and stop = 2),
	(start = 4 and stop = 6) and (start = 7 and stop = 8). 
	*/
	// Points to previous node of start. When start = head, prev_of_start = NULL.
	LinkedListNode *prev_of_start = NULL;
	LinkedListNode *start = head;
	LinkedListNode *stop = head;
	int count = 0;
	// Traverse whole linked list.
	while (stop)
	{
		count++;
		/*
		If we have covered k nodes in between start and stop (inclusive) or we are at the last 
		node.
		*/
		if (count == k || stop->next == NULL)
		{
			// Points to next node of start. 
			LinkedListNode *next_of_stop = stop->next;
			/*
			We want to reverse start to stop nodes, set stop->next = NULL so we know where to 
			stop.
			*/
			stop->next = NULL;
			// Reverse start to stop nodes. 
			reverse_linked_list(start);
			if (prev_of_start == NULL)
			{
				// Head will change when we are reversing the linked list first time. 
				head = stop;
			}
			else
			{
				/*
				We have reversed start to stop nodes, hence now stop will be next node of 
				prev_of_start. 
				*/
				prev_of_start->next = stop;
			}
			/*
			We have reversed start to stop nodes, hence next_of_stop will be next node of start. 
			*/
			start->next = next_of_stop;
			/*
			In the above example, after we have reversed first k nodes list will be:
			3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 7 -> 8 -> NULL,
			start will point to 1, next_of_stop will point to 4.
			
			Now we will set start and stop to point at 4.
			And prev_of_start should be previous of 4 that is 1.
			*/
			prev_of_start = start;
			start = next_of_stop;
			stop = next_of_stop;
			// Reset counter. 
			count = 0;
		}
		else
		{
			// Go to next node. 
			stop = stop->next;
		}
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
		int k;
		cin >> k;
		assert(1 <= k);
		assert(k <= n);

		LinkedListNode *ans = reverse_linked_list_in_groups_of_k(head, k);
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
