'''
How Many Binary Search Trees With n Nodes?
Problem Statement:
Write a function that will return the number of binary search trees that can be constructed with n nodes.
There may be other iterative solutions, but for the purpose of this exercise, please use recursive solution.
The purpose of this problem is to learn recursion and not DP. So, you must write at least one recursive solution.
After that, you can write a DP solution if you want.

Input/Output Format For The Function:
Input Format:
There is only one argument denoting integer n.
Output Format:
Return number of binary search trees that can be constructed, with n nodes.

Input/Output Format For The Custom Input:
Input Format:
The first and only line of input should contain an integer n.
If n = 3, then input should be:
3

Output Format:
There will be one line, containing an integer res, denoting the result returned by solution function.
For input n = 3, output will be:
5

Constraints:
1 <= n <= 16

Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
1

Sample Output 1:
1

Explanation 1:
1) root (node val = 1)
Sample Test Case 2:
Sample Input 2:
2
Sample Output 2:
2
Explanation 2:
1) root (node val = 2), root->left (node val = 1)
2) root (node val = 1), root->right (node val = 2)

Sample Test Case 3:
Sample Input 3:
3
Sample Output 3:
5
Explanation 3:
1) root (node val = 3), root->left (node val = 2), root->left->left (node val = 1)
2) root (node val = 3), root->left (node val = 1), root->left->right (node val = 2)
3) root (node val = 1), root->right (node val = 2), root->right->right (node val = 3)
4) root (node val = 1), root->right (node val = 3), root->right->left (node val = 2)
5) root (node val = 2), root->left (node val = 1), root->right (node val = 3)
If you keep doing this, it will form a series called Catalan numbers. One can simply lookup the formula for Catalan
numbers and write code for it. But that's not how we want to do this. We want to do this by understanding the
underlying recursion. The recursion is based on tree-topology only, as you can see by examples above, contents of the
nodes of the tree do not matter.
'''
import sys
import os

def how_many_BSTs(n):
    pass



if __name__ == "__main__":
    f = sys.stdout

    n = int(input())

    res = how_many_BSTs(n);
    f.write(str(res) + "\n")


    f.close()

'''
We have provided 4 solutions:
1) Catalan Number Solution: catalan_number_solution.cpp (If you simply provide this solution in interview, without 
explaining the intuition, then it will not be accepted.)
2) Recursive Solution : brute_force_solution.cpp (In this problem, we only want to practice recursion so constraints 
are intentionally kept low to allow this solution to pass all the test cases.)
3) Recursive Solution With Memorization : other_solution.cpp (Much much faster solution that the above recursive 
solution.)
4) Iterative Solution : optimal_solution.cpp (Logically same solution as the above recursive solution with 
memorization. But faster by some constant, because recursion is removed.)

First look at the Recursive Solution then Recursive Solution With Memorization and then Iterative Solution.
We expect you to implement recursive solution with memorization at least once. 
For Recursive Solution (brute_force_solution.cpp):
Time Complexity: 
O(Catalan number(n)).

This is a loose bound, tight bound is very complex to derive and explain.
Auxiliary Space Used: 
O(n).

Due to spaced used by function call stack, during recursive function calls. 
Space Complexity: 
O(n).
As auxiliary space used is O(n) and input is O(1), giving O(n) + O(1) -> O(n).
In recursive function you will note that function how_many_BSTs is called to calculate same values too many times! 
So this recalculation can be avoided by using memorization techniques. (We can use an array to store the result once 
it is calculated and afterwards reuse it!)
In Recursive Solution With Memorization, a few lines of code addition will improve time complexity from O(Catalan 
number(n))) to O(n ^ 2) and that is too big difference!
For n = 35, catalan number(35) = 3116285494907301262, while 35^2 = 1225. Now you see the difference of memorization!! 
Once you use memorization in your recursive implementation, time complexity, auxiliary space used and space complexity 
of Iterative Solution and Recursive Solution With Memorization will become same as mentioned below.

Time Complexity:
O(n ^ 2).
Auxiliary Space Used:
O(n).

As we are using array to store the calculated results. 
Space Complexity:
O(n).

As auxiliary space used is O(n) and input is O(1), giving O(n) + O(1) -> O(n).
'''

'''
def how_many_BSTs(n):
    def how_many_bsts_memo(n, memo):
        if n in memo:
            return memo[n]

        if n == 0 or n == 1:
            memo[n] = 1
            return 1

        result = 0
        for i in range(n):
            result += how_many_bsts_memo(i, memo) * how_many_bsts_memo(n - i - 1, memo)
        memo[n] = result
        return result
    return how_many_bsts_memo(n, dict())


def how_many_bsts_no_memo(n):

    if n == 0 or n == 1:
        return 1

    result = 0
    for i in range(n):
        result += how_many_bsts_no_memo(i) * how_many_bsts_no_memo(n - i - 1)
    return result


num = 50
print how_many_BSTs(num)
# print how_many_bsts_no_memo(num)
'''

'''
CATALAN NUMBER SOLUTION
#include<bits/stdc++.h>

using namespace std;

const int MAX_N = 16;

// ------------------- START -------------------


/* -------- 
THIS SOLUTION WILL FAIL SOME OF THE TEST CASES DUE TO OVERFLOW (of long long int) ISSUE IN 
n_choose_r FUNCTION. 

Also if you will simply provide solution using Catalan numbers in interview, without explaining 
the intuition,
then it will not be accepted.

Solution using recursion with memorization, is preferable than this solution. 
-------- */

long long int n_choose_r(long long int n, long long int r)
{
	// n choose r = n choose (n - r) property. Like 5 Choose 2 = 10 = 5 Choose 3. 
	if (r > n - r)
	{
		r = n - r;
	}
	// n choose r = [n * (n - 1) * --- * (n - r + 1)] / [r * (r - 1) * --- * 1].
	long long int nCr = 1;
	for (long long int i = 0; i < r; i++)
	{
		nCr *= (n - i);
		nCr /= (i + 1LL);
	}
	return nCr;
}

// Return nth Catalan number.
long long int how_many_BSTs(int n)
{
	/*
	Value of nth Catalan number = (2n Choose n) / (n + 1)
	*/
	long long int two_n_choose_n = n_choose_r(n + n, n);
	return two_n_choose_n / ((long long int) n + 1LL);
}

// ------------------- STOP -------------------

int main()
{
	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		cout << how_many_BSTs(n) << endl;
	}

	return 0;
}
'''

'''
BRUTE FORCE SOLUTION
#include<bits/stdc++.h>

using namespace std;

const int MAX_N = 16;

// ------------------- START -------------------

long long int how_many_BSTs(int n)
{
	// If base case.
	if (n == 0)
	{
		return 1LL;
	}
	/*
	Any BST with n nodes can be divided in 3 parts, 
	1) root.
	2) left sub-BST. 
	3) right sub-BST.
	
	There will be always one root hence structure of BST will only depend on the left sub-BST and 
	the right sub-BST. 

	We have 1 root fixed hence we have n - 1 nodes in left sub-BST + right sub-BST.
	So that is,
	n - 1 = nodes in left sub-BST + nodes in right sub-BST. 
	To get all the possibilities we can fix nodes in left sub-BST and get nodes in right sub-BST!
	So from the above formula,

	nodes in left sub-BST -> nodes in right sub-BST
	
	0 -> n - 1
	1 -> n - 2
	2 -> n - 3
	...
	n - 3 -> 2 
	n - 2 -> 1
	n - 1 -> 0

	Now suppose we take one fixed possibility 2 (nodes in left sub-BST) -> n - 3 
	(nodes in right sub-BST), then if we can get total number of BSTs possible with 2 nodes 
	(let's say it is x) and total number of BSTs possible with n - 3 nodes (let's say it is y), 
	then we can get the total number of BSTs possible with n nodes for the current possibility 
	(WHEN IN LEFT SUB-BST WE HAVE 2 NODES AND IN RIGHT SUB-BST WE HAVE n - 3 NODES) by x * y. Now 
	question is why x * y? For BST with n nodes we will fix one root, on the left subBST we fix 1 
	tree out of x possible BSTs, then to create BST with n nodes, we can use any of the y possible
	BSTs on the right sub-BST. So for one fixed sub-BST on left side we have generated y BSTs with
	n nodes. Now doing this for all x sub-BSTs possible on left side, total number of generated 
	BSTs = y + y + ... y (total x times) and that is x * y. (This will be difficult to understand 
	unless you try some examples yourself.)

	Now as we have done for 2 -> n - 3, we can try all possibilities and get the final answer 
	denoting total number of BSTS possible with n nodes!

	Let's take a small example n = 3 and see how every possible BST is covered in one of the 
	parition.
	All possible BSTs with 3 nodes are,
	1) root, root->left, root->left->left
	2) root, root->left, root->left->right
	3) root, root->right, root->right->right
	4) root, root->right, root->right->left
	5) root, root->left, root->right

	Now if we try:
	0 -> 2
	1 -> 1
	2 -> 0

	then we can divide the above 5 possibilities as:
	0 -> 2 : 	3) root, root->right, root->right->right
				4) root, root->right, root->right->left
	1 -> 1 : 	5) root, root->left, root->right
	2 -> 0 : 	1) root, root->left, root->left->left
				2) root, root->left, root->left->right
	*/
	long long int BSTs = 0LL;
	// Try all possibilities by taking number of nodes in left subBST from 0 to n - 1.
	for (int number_of_nodes_in_left_subBST = 0; number_of_nodes_in_left_subBST < n; 
		number_of_nodes_in_left_subBST++)
	{
		int number_of_nodes_in_right_subBST = n - 1 - number_of_nodes_in_left_subBST;
		BSTs += how_many_BSTs(number_of_nodes_in_left_subBST) * 
			how_many_BSTs(number_of_nodes_in_right_subBST);
	}
	return BSTs;
}

// ------------------- STOP -------------------

int main()
{
	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		cout << how_many_BSTs(n) << endl;
	}

	return 0;
}
'''

'''
#include<bits/stdc++.h>

using namespace std;

const int MAX_N = 16;

// ------------------- START -------------------

long long int how_many_BSTs(int n)
{
	// BSTs[i] stores the number of BSTS possible with i nodes.
	vector<long long int> BSTs(n + 1, 0LL);
	// Base case.
	BSTs[0] = 1LL;
	/*
	In recursion there will be lots of recalculations (unnecessary recalculations), so to avoid 
	that we can store the values once calculated. 
	Here in each loop iteration we will find the value of BSTs[cur_BST_size]. As we are 
	calculating from 1 to n, when we are finding value for BSTs[cur_BST_size], we will have 
	values for BSTs[ < cur_BST_size] already calculated and they can be used directly.
	*/
	for (int cur_BST_size = 1; cur_BST_size <= n; cur_BST_size++)
	{
		// Calculate BSTs[cur_BST_size].
		for (int number_of_nodes_in_left_subBST = 0; 
			number_of_nodes_in_left_subBST < cur_BST_size; 
			number_of_nodes_in_left_subBST++)
		{
			int number_of_nodes_in_right_subBST = 
				cur_BST_size - 1 - number_of_nodes_in_left_subBST;
			BSTs[cur_BST_size] += BSTs[number_of_nodes_in_left_subBST] * 
				BSTs[number_of_nodes_in_right_subBST];
		}
	}
	return BSTs[n];
}

// ------------------- STOP -------------------

int main()
{
	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		cout << how_many_BSTs(n) << endl;
	}

	return 0;
}
'''
