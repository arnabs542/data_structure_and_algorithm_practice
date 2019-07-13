'''
Find The Next Palindromic Number
Problem Statement:
Given a number n, you have to find next palindromic number pal. To be precise, you have to find an integer pal, which is
 smallest palindromic number, greater than n.
Input/Output Format For The Function:
Input Format:
There is only one argument denoting integer n.
Output Format:
Return the required number pal.
Input/Output Format For The Custom Input:
Input Format:
There should be only one line, containing an integer n.
If n = 5, then input should be:
5
Output Format:
There will be one line, containing resultant integer pal.
For input n = 5, output will be:
6
Constraints:
0 <= n <= 2147483647
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
5
Sample Output 1:
6
Explanation 1:
6 is a palindromic number, and bigger than 5. There is no palindromic number less than 6 and bigger than 5.
Sample Test Case 2:
Sample Input 2:
10
Sample Output 2:
11
Notes:
Suggested time in interview: 30 minutes.
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework i.e.
 For the first attempt of a given homework problem, the focus should be to understand what the problem is asking, what approach
 you are using, coding it, as well as identifying any gaps that you can discuss during a TA session. Take your time, but
 limit yourself to 2 one hour sessions for most problems.
'''
import sys
import os


# Complete the function below.
def next_palindrome(n):
    pass


if __name__ == "__main__":
    f = sys.stdout
    n = int(input())
    res = next_palindrome(n);
    f.write(str(res) + "\n")
    f.close()

'''
If you are getting wrong answer, then first thing you should make sure is to use appropriate data type. (using int will
not work, it will overflow for given constratins!)

We have provided two solutions, optimal_solution1.cpp and optimal_solution2.cpp.
First have a look at optimal_solution1.cpp (it might look lengthy, but we have focused on readability of the code) and then
look at optimal_solution2.cpp. Try some examples to understand the solutions clearly. 

optimal_solution2.cpp is different from most of the solutions you will see online. It will take some time to understand
initially, but after that in interviews it will be less error prone to write the solution. 

In optimal_solution1.cpp we can use int array instead of strings to simplify some of the steps, but it will take more memory.
 int is 4 bytes while char is only 1 byte. So 3 times more memory!
 
For both the solutions:
Time Complexity:
O(n).
Auxiliary Space Used
O(n). 
Space Complexity:
O(n).
'''
'''
OPTIMAL SOLUTION 1
#include<bits/stdc++.h>

using namespace std;

// -------------------------- START --------------------------

// Function to convert string to long long int.
// Alternatively you can use the built in function "stoll" introduced by C++11.
long long int string_to_lli(string &no_str)
{
	long long int no = 0;
	int len = no_str.length();
	for (int i = 0; i < len; i++)
	{
		no = 10LL * no + (no_str[i] - '0');
	}
	return no;
}

/*	
	This function copies digit at position i to position len - 1 - i for i in range 0 to l. If 
	876555123 and l = 2, r = 6 then this function will return 876555678.   
*/
long long int copy_left_to_right(int len, string &n_str, int l, int r)
{
	while (l >= 0)
	{
		n_str[r] = n_str[l];
		l--;
		r++;
	}
	return string_to_lli(n_str);
}

/*
	This function adds 1 to lth position and propagates carry if needed. It also copies lth 
	position to rth position i.e if 190 then this function will return 202. 
*/
long long int add_to_mid_and_copy_left_to_right(int len, string &n_str, int l, int r)
{
	n_str[l]++;
	while (l >= 0)
	{
		if (n_str[l] >= char (10 + '0'))
		{
			n_str[l - 1]++;
			n_str[l] = (n_str[l] - '0') % 10 + '0';
		}
		n_str[r] = n_str[l];
		l--;
		r++;
	}
	return string_to_lli(n_str);
}

// Function to find next smallest palindrome of n_str.
long long int solve(int len, string &n_str, int l, int r)
{
	int l_copy = l, r_copy = r;
	/*
	Start from middle and try to find first mismatch. 
	n_str = "87655078", l = 3, r = 4.
	First compare n_str[3] and n_str[4], then n_str[2] and n_str[5], then n_str[1] and n_str[6]...
	We will stop when we will find the mismatch i.e. n_str[l] != n_str[r].
	*/
	while (l >= 0 && n_str[l] == n_str[r])
	{
		l--;
		r++;
	}
	// Given no is already palindrome i.e. 12321.
	if (l < 0)											
	{
		return add_to_mid_and_copy_left_to_right(len, n_str, l_copy, r_copy);
	}
	// No is of type 8(7)6(5)4 here 8 > 5 hence next smallest palindrome will be 87678.
	if (n_str[l] > n_str[r])									
	{
		return copy_left_to_right(len, n_str, l_copy, r_copy);
	}
	// No is of type 8(7)6(8)9 here 7 < 8 hence next smallest palindrome will be 87778. 
	else												
	{
		return add_to_mid_and_copy_left_to_right(len, n_str, l_copy, r_copy);	
	}
}

// Function to check if all digits are 9 or not.
bool all_nine(string &n_str)
{
	int len = n_str.length();
	for (int i = 0; i < len; i++)
	{
		if (n_str[i] != '9')
		{
			return false;
		}
	}
	return true;
}

// Function to convert int to string.
// Alternatively you can use the built in function "to_string" introduced by C++11.
string int_to_string(int no)
{
	if (no == 0)
	{
		return "0";
	}
	string no_str = "";
	while (no)
	{
		no_str = (char) (no % 10 + '0') + no_str;
		no /= 10;
	}
	return no_str;
}

// Function to find next smallest palindrome of n.
long long int next_palindrome(int n) 
{
	string n_str = int_to_string(n);
	int len = n_str.length();
	// Only possible case when no of digits will be increased. 
	if (all_nine(n_str))									
	{
		long long int ret = 1LL;
		for (int i = 0; i < len; i++)
		{
			ret *= 10LL;
		}
		ret++;
		return ret;
	}
	// 1-indexed. When n = 1234321 then l = 4, r = 4 and when n = 12344321 then l = 4, r = 5.
	int l, r;											
	if (len % 2)									
	{
		l = (len + 1) / 2;
		r = (len + 1) / 2;
	}
	else										
	{
		l = len / 2;							
		r = len / 2 + 1;
	}
	// It will be easy if l and r are 0 indexed instead of 1 indexed. 
	return solve(len, n_str, l - 1, r - 1);					
}

// -------------------------- STOP ---------------------------

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
		long long int n;
		cin >> n;
		assert(0 <= n);
		assert(n <= INT_MAX);
		long long int ans = next_palindrome(n);
		cout << ans << endl;
	}

	return 0;
}
'''
'''
OPTIMAL SOLUTION 2
#include<bits/stdc++.h>

using namespace std;

// -------------------------- START --------------------------

// Function to convert long long int to string.
// Alternatively you can use the built in function "to_string" introduced by C++11.
string lli_to_string(long long int no)
{
	if (no == 0LL)
	{
		return "0";
	}
	string no_str = "";
	while (no)
	{
		no_str = (char) (no % 10LL + '0') + no_str;
		no /= 10LL;
	}
	return no_str;
}

// Function to convert string to long long int.
// Alternatively you can use the built in function "stoll" introduced by C++11.
long long int string_to_lli(string no_str)
{
	long long int no = 0LL;
	int len = no_str.length();
	for (int i = 0; i < len; i++)
	{
		no = 10LL * no + (no_str[i] - '0');
	}
	return no;
}

long long int next_palindrome(int n)
{
	string n_str = lli_to_string(n);
	int len = n_str.length();
	/*
	Will be used to divide string into left half and right half.
	n = 123456 -> left half= "123" -> right half = "456",
	n = 1234567 -> left half = "1234" -> right half = "567".
	*/
	int offset = len % 2;
	/*
	n = 999 -> all_nine_case = 1001,
	n = 125 -> all_nine_case = 1001.

	Suppose n = 2147447411 -> all_nine_case = 10000000001, which can not be stored in int, so use 
	long long int to avoid overflow. 
	*/
	long long int all_nine_case = pow(10, len) + 1LL;
	/*
	n = 123456 -> left_half_str = "123",
	n = 1234567 -> left_half_str = "1234".
	*/
	string left_half_str = n_str.substr(0, len / 2 + offset);
	/*
	n = 123456 -> left_half_str = "123" -> left_half_plus_one_str = "124",
	n = 1234567 -> left_half_str = "1234" -> left_half_plus_one_str = "1235".
	*/ 
	string left_half_plus_one_str = lli_to_string(string_to_lli(left_half_str) + 1LL);
	/*
	n = 123456 -> left_half_str = "123" -> mirror_without_addition_case = 123321,
	n = 1234567 -> left_half_str = "1234" -> mirror_without_addition_case = 1234321.
	*/
	long long int mirror_without_addition_case = string_to_lli(
		left_half_str + 
		string(
			left_half_str.rbegin() + 
			offset, left_half_str.rend()
		)
	);
	/*
	n = 123456 -> left_half_str = "123" -> left_half_plus_one_str = "124" -> 
	mirror_with_addition_case = 124421,
	n = 1234567 -> left_half_str = "1234" -> left_half_plus_one_str = "1235" -> 
	mirror_with_addition_case = 1235321.

	Suppose n = 2147447411 -> mirror_with_addition_case = 2147557412, which can not be stored in 
	int, so use long long int to avoid overflow. 
	*/ 
	long long int mirror_with_addition_case = string_to_lli(
		left_half_plus_one_str + 
		string(
			left_half_plus_one_str.rbegin() + 
			offset, 
			left_half_plus_one_str.rend()
		)
	);
	/*
	In these cases mirror_without_addition_case will be smaller than n, so it can not be the 
	answer.

	n = 123456 -> left_half_str = "123" -> mirror_without_addition_case = 123321,
	n = 1234567 -> left_half_str = "1234" -> mirror_without_addition_case = 1234321.

	In these cases mirror_without_addition_case will be greate than n, so it is the answer.

	n = 123156 -> left_half_str = "123" -> mirror_without_addition_case = 123321,
	n = 1234167 -> left_half_str = "1234" -> mirror_without_addition_case = 1234321.	
	*/
	if (mirror_without_addition_case - n > 0LL)
	{
		return mirror_without_addition_case;
	}
	// When mirror_without_addition_case - n <= 0.
	return min(all_nine_case, mirror_with_addition_case);
}

// -------------------------- STOP ---------------------------

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
		long long int n;
		cin >> n;
		assert(0 <= n);
		assert(n <= INT_MAX);
		long long int ans = next_palindrome(n);
		cout << ans << endl;
	}

	return 0;
}
'''
