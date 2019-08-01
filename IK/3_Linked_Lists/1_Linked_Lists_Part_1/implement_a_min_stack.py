'''
Implement A Min Stack
Problem Statement:
You have to build a min stack. Min stack should support push, pop methods (as usual stack) as well as one method that returns
 the minimum element in the entire stack.
You are given an integer array named operations of size n, containing values >= -1.
operations[i] = -1 means you have to perform a pop operation. The pop operation does not return the removed/popped element.

operations[i] = 0 means you need to find the minimum element in the entire stack and add it at the end of array to be returned.

operations[i] >= 1 means you you need to push operations[i] on the stack.
Input/Output Format For The Function:
Input Format:
There is only one argument in input, denoting integer array named operations.
Output Format:
Return an integer array res, containing answer for each operations[i] = 0.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting length of operations array. In next n lines, ith line should
contain an integer operations[i], denoting value at index i of operations array. (i=0,1,...,n-1)
If n = 7 and operations = [10, 5, 0, -1, 0, -1, 0], then input should be:
7
10
5
0
-1
0
-1
0

Output Format:
Let’s denote the total number of min query operations(i.e. operations[j]=0) in input array operations as x. So, length of
 returned array res must be x.
There will be x lines, where ith line contains an integer res[i], denoting value at index i of res.
For input n = 7 and operations = [10, 5, 0, -1, 0, -1, 0], output will be:
5
10
-1

Constraints:
    * 1 <= n <= 100000
    * -1 <= operations[i] <= 2 * 10^9, (i=0,1,...,n-1)
    * If stack is empty, then do nothing for pop operation.
    * If stack is empty, then consider -1 as the minimum element.

Sample Test Case:
Sample Input:
[10 5 0 -1 0 -1 0]
Sample Output:
[5 10 -1]

Explanation:
Initially stack = [], ans = [].
operations[0] = 10 -> push -> stack = [10], ans = []
operations[1] = 5 -> push -> stack = [10 5], ans = []
operations[2] = 0 -> get minimum element -> stack = [10, 5], ans = [5]
operations[3] = -1 -> pop -> stack = [10], ans = [5]
operations[4] = 0 -> get minimum element ->stack = [10], ans = [5 10]
operations[5] = -1 -> pop -> stack = [], ans = [5, 10]
operations[6] = 0 -> get minimum element -> stack = [], ans = [5 10 -1] (as stack is empty we have to consider -1 as the minimum element.)
'''
#!/bin/python

import os
import sys

# Complete the function below.

def min_stack(operations):
    pass


if __name__ == "__main__":
    f = sys.stdout

    operations_size = int(input())

    operations = []
    for _ in range(operations_size):
        operations_item = int(input())
        operations.append(operations_item)


    res = min_stack(operations)

    f.write('\n'.join(map(str, res)))

    f.write('\n')
    f.close()


'''
We have provided two solutions and both solutions contain necessary comments to understand the approach used:

1) brute_force.cpp
Time Complexity:
O(n ^ 2).

As we are transferring all elements of the stack while finding minimum value. 
Auxiliary Space Used:
O(n).

As we are using two extra stacks and one extra vector to store values.  
Space Complexity:
O(n).

As input is O(n) and auxiliary space used is also O(n). So, O(n) + O(n) -> O(n).

2) optimal_solution.cpp
Time Complexity: 
O(n).

As each operation is performed in constant time and there are total n operations.

Auxiliary Space Used:
O(n). 

As we are using one extra stack and one extra vector to store values.
Space Complexity:
O(n).

As input is O(n) and auxiliary space used is also O(n). So, O(n) + O(n) -> O(n). 
'''
'''
BRUTE FORCE
#include<bits/stdc++.h>

using namespace std;

// -------------------------- START --------------------------

const int MAX_N = 100000, MIN_VAL = -1, MAX_VAL = 2000000000;

vector<int> min_stack(vector<int> operations)
{
	int n = operations.size();
	vector<int> ans;
	stack<int> original, helper;
	for (int i = 0; i < n; i++)
	{
		if (operations[i] >= 1)
		{
			original.push(operations[i]);
		}
		else if (operations[i] == -1)
		{
			if (original.empty() == false)
			{
				original.pop();
			}
		}
		else
		{
			if (original.empty())
			{
				// If stack is empty, consider -1 as the minimum element.
				ans.push_back(-1);
			}
			else
			{
				/*
				Transfer all elements to other stack updating the minimum
				value.
				*/
				int min_val = MAX_VAL;
				while (original.empty() == false)
				{
					min_val = min(min_val, original.top());
					helper.push(original.top());
					original.pop();
				}
				// Add the minimum value.
				ans.push_back(min_val);
				// Restore the stack.
				while(helper.empty() == false)
				{
					original.push(helper.top());
					helper.pop();
				}
			}
		}
	}
	return ans;
}

// -------------------------- STOP ---------------------------

int main()
{
	// freopen(
	// 	"..//test_cases//sample_test_cases_input.txt", 
	// 	"r", stdin
	// );
	// freopen(
	// 	"..//test_cases//sample_test_cases_expected_output.txt",
	// 	"w", stdout
	// );
	// freopen(
	// 	"..//test_cases//handmade_test_cases_input.txt",
	// 	"r", stdin
	// );
	// freopen(
	// 	"..//test_cases//handmade_test_cases_expected_output.txt",
	// 	"w", stdout
	// );
	// freopen(
	// 	"..//test_cases//generated_small_test_cases_input.txt",
	// 	"r", stdin
	// );
	// freopen(
	// 	"..//test_cases//generated_small_test_cases_expected_output.txt",
	// 	"w", stdout
	// );
	// freopen(
	// 	"..//test_cases//generated_big_test_cases_input.txt",
	// 	"r", stdin
	// );
	// freopen(
	// 	"..//test_cases//generated_big_test_cases_expected_output.txt",
	// 	"w", stdout
	// );
	// freopen(
	// 	"..//test_cases//ignore.txt",
	// 	"w", stdout
	// );

	int test_cases;
	cin >> test_cases;
	assert(test_cases >= 0);
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		vector<int> operations(n);
		int queries = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> operations[i];
			assert(MIN_VAL <= operations[i]);
			assert(operations[i] <= MAX_VAL);
			queries += (operations[i] == 0);
		}
		vector<int> ans = min_stack(operations);
		int len = ans.size();
		assert(len == queries);
		for (int i = 0; i < queries; i++)
		{
			cout << ans[i] << endl;
		}
		cout << endl;
	}

	return 0;
}
'''
'''
#include<bits/stdc++.h>

using namespace std;

const int MAX_N = 100000, MIN_VAL = -1, MAX_VAL = 2000000000;

// -------------------------- START --------------------------

vector<int> min_stack(vector<int> operations)
{
	int n = operations.size();
	vector<int> ans;
	// At any point of time min_till_now.top() will contain minimum of all elements present in stack.
	stack<int> min_till_now;
	for (int i = 0; i < n; i++)
	{
		if (operations[i] >= 1)
		{
			/*
			If stack is empty then after adding operations[i], minimum of entire stack will become
			operations[i]. 
			If stack is not empty then after adding operations[i], minimum of entire stack will 
			become min(operations[i], minimum of already present elements in stack).
			*/
			int minimum_value = operations[i];
			if (min_till_now.empty() == false)
			{
				minimum_value = min(minimum_value, min_till_now.top());
			}
			min_till_now.push(minimum_value);
		}
		else if (operations[i] == -1)
		{
			if (min_till_now.empty() == false)
			{
				min_till_now.pop();
			}
		}
		else
		{
			if (min_till_now.empty())
			{
				// If stack is empty, consider -1 as the minimum element.
				ans.push_back(-1);
			}
			else
			{
				/*
				min_till_now.top() contains the minimum of all elements present in stack 
				simple_stack. 
				*/
				ans.push_back(min_till_now.top());
			}
		}
	}
	return ans;
}

// -------------------------- STOP ---------------------------

int main()
{
	// freopen(
	// 	"..//test_cases//sample_test_cases_input.txt", 
	// 	"r", stdin
	// );
	// freopen(
	// 	"..//test_cases//sample_test_cases_expected_output.txt",
	// 	"w", stdout
	// );
	// freopen(
	// 	"..//test_cases//handmade_test_cases_input.txt",
	// 	"r", stdin
	// );
	// freopen(
	// 	"..//test_cases//handmade_test_cases_expected_output.txt",
	// 	"w", stdout
	// );
	// freopen(
	// 	"..//test_cases//generated_small_test_cases_input.txt",
	// 	"r", stdin
	// );
	// freopen(
	// 	"..//test_cases//generated_small_test_cases_expected_output.txt",
	// 	"w", stdout
	// );
	// freopen(
	// 	"..//test_cases//generated_big_test_cases_input.txt",
	// 	"r", stdin
	// );
	// freopen(
	// 	"..//test_cases//generated_big_test_cases_expected_output.txt",
	// 	"w", stdout
	// );
	// freopen(
	// 	"..//test_cases//ignore.txt",
	// 	"w", stdout
	// );

	int test_cases;
	cin >> test_cases;
	assert(test_cases >= 0);
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		vector<int> operations(n);
		int queries = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> operations[i];
			assert(MIN_VAL <= operations[i]);
			assert(operations[i] <= MAX_VAL);
			queries += (operations[i] == 0);
		}
		vector<int> ans = min_stack(operations);
		int len = ans.size();
		assert(len == queries);
		for (int i = 0; i < queries; i++)
		{
			cout << ans[i] << endl;
		}
		cout << endl;
	}

	return 0;
}
'''
