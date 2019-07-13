'''
Cut The Rope
Problem Statement:
Given a rope with length n, find the maximum value maxProduct, that can be achieved for product len[0] * len[1] * ... *
 len[m - 1], where len[] is the array of lengths obtained by cutting the given rope into m parts.
Note that
there should be atleast one cut, i.e. m >= 2.
All m parts obtained after cut should have non-zero integer valued lengths.

Input/Output Format For The Function:
Input Format:
There is only one argument, an integer denoting n.
Output Format:
Return a number maxProduct, denoting maximum possible product as asked in the problem.
Input/Output Format For The Custom Input:
Input Format:
There should be only one line, containing an integer n, denoting length of rope.
If n = 5, then input should be:
5
Output Format:
There will be one line, containing an integer maxProduct.
For input n = 5, output will be:
6
Constraints:
2 <= n <= 111
We have to cut at least once. (2 <= m).
Length of the rope, as well as the length of each part are in positive
 integer value. (i.e. can't do partial cuts.)
Sample Test Case:
Sample Input:
4
Sample Output:
4
Explanation:
﻿
For n = 4, there are two cuts possible: 1 + 3 and 2 + 2.
We'll pick 2 + 2, because their product 2 * 2 = 4 is greater than product of the first one 1 * 3 = 3.
(So our m = 2, n[0] = 2 and n[1] = 2 and product is n[0] * n[1] = 4.)
Note:
JavaScript solutions will give “Wrong Answer” for the test cases from 023 to 029 because the answers exceed Number.MAX_SAFE_INTEGER.
 So, if your JavaScript solution passes all the previous test cases and for the test cases from 023 to 029 the answers are
 only slightly different (like 450283905890997300 vs 450283905890997363), then consider your solution as a correct solution.
'''
import os
import sys

#
# Complete the max_product_from_cut_pieces function below.
#
def max_product_from_cut_pieces(n):
    pass


if __name__ == "__main__":
    fptr = sys.stdout
    n = int(input())
    res = max_product_from_cut_pieces(n)
    fptr.write(str(res) + '\n')
    fptr.close()


'''
If getting wrong answer then first check if you are using appropriate data type in intermediate calculations. (For the
 given constraints integer will overflow.)
We have provided three solutions:
1) other_solution_1.cpp: dp quadratic solution.
2) other_solution_2.cpp: dp linear solution. Solution from observing fixed pattern.
3) optimal_solution.cpp: solution from observing fixed pattern. (Even though if you are able to directly come to this solution,
 we expect you to write dp solution once.) 
Have a look at the solutions. All of them contain detailed comments.
other_solution_1.cpp:
Time Complexity:
O(n^2). 
We are finding maximum product for all the rope lengths, from 1 to n. 
And to find maximum product for each rope length we are iterating over all previous rope lengths. 
So that is O(1 + 2 + 3 + ... + (n - 1)) = O(n^2).
Auxiliary Space Used:
O(n).
Because we are using array of length n + 1.
Space Complexity:
O(n).
Because auxiliary space used is O(n). 
other_solution_2.cpp:
Time Complexity:
O(n). 
We are finding maximum product for all the rope lengths, from 1 to n, in constant time. 
So that is O(n).
Auxiliary Space Used:
O(n).
Because we are using array of length n + 1.
Space Complexity:
O(n).
Because auxiliary space used is O(n). 
optimal_solution.cpp:
Time Complexity:
O(log(n)). (or more specifically O(log(n / 3)).)
Because we are using power function.
Auxiliary Space Used:
O(log(n)).
YES IT IS NOT O(1). 
Power function is recursive hence due to recursive function call stack it will be O(log(n)).
Note that here we can use iterative power function to reduce the auxiliary space used to O(1). 
But for readability purpose we have used recursive power function.  
Space Complexity:
O(log(n)). 
Because auxiliary space used is O(log(n)).
Other Note:
We can use direct multiplication instead of power function but its time complexity will be O(n / 3) instead of O(log(n /
 3)).
'''
'''
other_solution 1
#include<bits/stdc++.h>
using namespace std;

const int MIN_N = 2, MAX_N = 111;

// -------------------- START --------------------------

// Function to find maximum product by cutting rope of length n into pieces.
long long int max_product_from_cut_pieces(int n)
{
	// Need to use long long int otherwise it will overflow for the given constraints.
	vector<long long int> max_product(n + 1, 0);
	// Base case.
	max_product[1] = 1;
	// Use dp bottom-up approach.
	for (int cur_rope_length = 2; cur_rope_length <= n; cur_rope_length++)
	{
		/*
		Think practically, when ever we are making last cur it will be between 1 and 
		cur_rope_length - 1. 
		Also due to bottom-up approach we already have found the maximum product for smaller 
		lengths. 
		So now we iterate over all the possibilities of last cut (from 1 to cur_rope_length - 1) 
		and find the maximum product for the cur_rope_length.
		*/
		for (int cut_length = 1; cut_length < cur_rope_length; cut_length++)
		{
			max_product[cur_rope_length] = max(
				max_product[cur_rope_length], 
				(long long int) cut_length * max_product[cur_rope_length - cut_length]
			);
		}
		/*
		In the above loop we have found the answer when we have to make at least one cut.
		For cur_rope_length=n we have to make at least one cut and when we iterate over 1 to 
		cur_rope_length - 1 we are already making one cut, hence max_product[cur_rope_length - 
		cut_length] "need not" to have at least one cut.
		So for lengths other than n update answer when no cut. 
		*/
		if (cur_rope_length != n)
		{
			max_product[cur_rope_length] = max(
				max_product[cur_rope_length], 
				(long long int)cur_rope_length
			);
		}
	}
	return max_product[n];
}

// -------------------- STOP ---------------------------

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
	assert(test_cases >= 0);
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(MIN_N <= n);
		assert(n <= MAX_N);
		long long int ans = max_product_from_cut_pieces(n);
		assert(1 <= ans);
		cout << ans << endl;
	}

	return 0;
}
'''
'''
other_solution 2
#include<bits/stdc++.h>
using namespace std;

const int MIN_N = 2, MAX_N = 111;

// -------------------- START --------------------------

// Function to find maximum product by cutting rope of length n into pieces.
long long int max_product_from_cut_pieces(int n){
    // max_product[i] = maximum possible product for i, with at least one cut.
    vector<long long int> max_product(n + 1);
    
    // Assign maximum possible product manually for 2 <= i <= min(n, 4).
    // Maximum possible product for 2 = 1 * 1.
    // Given that n >= 2, so we do not need to check if (n >= 2){
    max_product[2] = 1LL;
    if (n >= 3){
        // Maximum possible product for 3 = 2 * 1.
        max_product[3] = 2LL;
    }
    if (n >= 4){
        // Maximum possible product for 4 = 2 * 2.
        max_product[4] = 4LL;
    }
    
    // Calculate maximum possible product using DP for 5 <= i <= n.
    for (int i = 5; i <= n; i++){
        /*
        Use the observation that for i >= 5, there will be at least one cut
        of length 3.

        1) i - 3LL => when exactly two cuts => one cut of length 3 and another
        cut of length i - 3.
        2) max_product[i - 3] => when more than two cuts => one cut of length 3
        and other cuts from max_product[i - 3].
        */
        max_product[i] = max(i - 3LL, max_product[i - 3]) * 3LL;
    }
    return max_product[n];
}

// -------------------- STOP ---------------------------

int main()
{
    //freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
    freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
    //freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
    //freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
    //freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
    freopen("..//test_cases//ignore.txt", "w", stdout);

    int test_cases;
    cin >> test_cases;
    assert(test_cases >= 0);
    while (test_cases--)
    {
        int n;
        cin >> n;
        assert(MIN_N <= n);
        assert(n <= MAX_N);
        long long int ans = max_product_from_cut_pieces(n);
        assert(1 <= ans);
        cout << ans << endl;
    }

    return 0;
}
'''
'''
OPTMIAL SOLUTION
#include<bits/stdc++.h>

using namespace std;

const int MIN_N = 2, MAX_N = 111;

// -------------------- START ---------------------------

// Function to find a^b in O(log(b)).
// Use long long int otherwise it will overflow, for the given constraints.
long long int power(int a, int b)
{
	// a^0 = 1.
	if (b == 0)
	{
		return 1LL;
	}
	/*
	Suppose we want to find a^13. 
	a^13 = a^6 * a^6 * a^1. 
	Now instead of finding a^6 two times we can calculate it once (to speedup) and then use it. 
	Then multiply with remaining a. 
	*/
	long long int ret = power(a, b / 2);
	ret = ret * ret;
	if (b % 2)
	{
		ret = ret * (long long int)a;
	}
	return ret;
}

// Function to find maximum product by cutting rope of length n into pieces.
// Also need to use long long int otherwise it will overflow for the given constraints.
long long int max_product_from_cut_pieces(int n)
{
	// Base cases.
	if (n <= 3)
	{
		return (long long int)n - 1;
	}
	// Try some examples and will notice that there is fixed pattern.
	// Cut the rope such that all pieces have length 3.
	if (n % 3 == 0)
	{
		return power(3, n / 3);
	}
	// Cut the rope such that one piece has length 4 and rest pieces have length 3.
	if (n % 3 == 1)
	{
		return power(3, (n - 4) / 3) * 4LL;
	}
	// Cut the rope such that one piece has length 2 and rest pieces have length 3.
	return power(3, (n - 2) / 3) * 2LL; 
}

// -------------------- STOP ---------------------------

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
	assert(test_cases >= 0);
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(MIN_N <= n);
		assert(n <= MAX_N);
		long long int ans = max_product_from_cut_pieces(n);
		assert(1 <= ans);
		cout << ans << endl;
	}

	return 0;
}
'''
