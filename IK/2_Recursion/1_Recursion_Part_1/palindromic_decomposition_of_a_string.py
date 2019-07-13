'''
Palindromic Decomposition Of A String
Problem Statement:
A palindromic decomposition of string is a decomposition of the string into substrings, such that all those substrings
are valid palindromes.
Given a string s, you have to find ALL possible palindromic decompositions of it.
Note that string s itself is also a substring of s.

The purpose of this problem is to learn recursion and not DP. So, you must write at least one recursive solution. After
 that, you can write a DP solution if you want.

Input/Output Format For The Function:
Input Format:
There is only one argument: string s.
Output Format:
Return array of string res, containing ALL possible palindromic decompositions of given string.

To separate substrings in the decomposed string, use '|' as a separator between them. (Look at the sample test cases
for more clarity.)

Note that:
You need not to worry about the order of strings in your output array. Like for s = "aa", arrays ["a|a", "aa"] and
["aa", "a|a"] both will be accepted.
In any string in your returned array res, order of characters should remain same as in given string. (i.e. for
s = "ab" you should return ["a|b"] and not ["b|a"].)

Any string in the returned array should not contain any spaces. e.g. s = "ab" then ["a|b"] is expected, ["a |b"] or
["a| b"] or ["a | b"] will give wrong answer.

Input/Output Format For The Custom Input:
Input Format:
The first and only line of input should contain a string s, denoting the input string.
If s = “abracadabra”, then input should be:

abracadabra

Output Format:
Let’s denote size of res array as m, where res is the resultant array of string returned by solution function.
Then, there will be m lines of output, where ith line contains a string res[i], denoting string at index i of res.

For input s = “abracadabra”, output will be:

a|b|r|a|c|ada|b|r|a
a|b|r|aca|d|a|b|r|a
a|b|r|a|c|a|d|a|b|r|a

Constraints:
1 <= |s| <= 20
s only contains lowercase letters ('a' - 'z').

Sample Test Cases:
Sample Input:
"abracadabra"

Sample Output:
[
   "a|b|r|a|c|a|d|a|b|r|a",
   "a|b|r|a|c|ada|b|r|a",
   "a|b|r|aca|d|a|b|r|a"
]

Notes:
Suggested time in interview: 40 minutes
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework
i.e. For the first attempt of a given homework problem, the focus should be to understand what the problem is asking,
what approach you are using, coding it, as well as identifying any gaps that you can discuss during a TC session. Take
your time, but limit yourself to 2 one hour sessions for most problems.
'''

import sys
import os

# Complete the function below.

from copy import deepcopy
def generate_palindromic_decompositions(string):
    results = []
    generate_palindromic_decomposition_rec(list(string), 0, [], results)
    return results

def generate_palindromic_decomposition_rec(string, index, current, results):
    if index == len(string):
        if is_current_section_palindrome(current):
            results.append(''.join(current))
        return

    current.append(string[index])
    generate_palindromic_decomposition_rec(string, index+1, deepcopy(current), results)

    if is_current_section_palindrome(current):
        current.append('|')
        generate_palindromic_decomposition_rec(string, index+1, deepcopy(current), results)


def is_current_section_palindrome(current_string):
    end = len(current_string)-1
    start = len(current_string) - 1
    while start-1 >= 0 and current_string[start-1] != '|':
        start -= 1
    while start <= end:
        if current_string[start] != current_string[end]:
            return False
        start += 1
        end -= 1
    return True

if __name__ == "__main__":
    f = sys.stdout

    try:
        s = str(input())
    except:
        s = None

    res = generate_palindromic_decompositions(s);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()


'''
We have provided two solutions:
1) Solution Using 2 - Recursion: other_solution.cpp
2) Solution Using Dynamic Programming: optimal_solution.cpp

Try to solve the problem using both the approaches.
First look at the solution using recursion and then solution using dynamic programming.
In solution using dynamic programming we have pre-calculated is_palindrome array, but in solution using recursion we 
have not. But you should do it in recursive solution also. (To make code readable and easy to understand, we have not
 pre-calculated in recursive solution.) 

Time Complexity Of The Optimal Solution:
O((2^(n - 1)) * n).

Consider input s = "aaaaaaaaaaaaaaaaaaaa" (20 times.)
For strings like this, every substring will be a palindrome, hence total number of palindromic decomposition in worst 
case will be 2^(n - 1). 
(Try s = "aaa" and it will be more clear why 2^(n - 1).)

We will store 2^(n - 1) palindromic decomposition and length of each will be O(n) hence time complexity will be 
O((2^(n - 1)) * n).

Auxiliary Space Used Of The Optimal Solution:
O((2^(n - 1)) * n).

In answer array we will store all 2^(n - 1) palindromic decomposition of length O(n). 
Also is_palindrome array is O(n ^ 2) so O((2^(n - 1)) * n) + O(n ^ 2) -> O((2^(n - 1)) * n).
Space Complexity Of The Optimal Solution:
O((2^(n - 1)) * n).

Auxiliary space used is O((2^(n - 1)) * n) and input size is O(n) hence O((2^(n - 1)) * n) + O(n) -> O((2^(n - 1)) * n).
'''

'''
def generate_palindromic_decompositions(string):
    if not string or len(string) == 1:
        return [string]

    output = []
    n = len(string)

    def _palindromic_decomposition(so_far, start):
        # base case
        if start == n:
            output.append('|'.join(so_far))
            return

        # take every possible string from the current position and if it's palndromic go forward, and if it's not prune
        for i in range(start+1, n+1):
            curr = string[start:i]
            if is_palindrome(curr):
                so_far.append(curr)
                _palindromic_decomposition(so_far, i)
                # at the end of dfs remove what was appended to
                so_far.pop()

    _palindromic_decomposition([], 0)
    return output


def is_palindrome(string):
    if not string or len(string) == 1:
        return True

    low, high = 0, len(string) - 1
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1

    return True


def is_palindrome_rec(string):
    if len(string) == 0:
        return True
    return _is_palindrome(string, 0, len(string)-1)


def _is_palindrome(string, start, end):
    # empty string or string of 1 character
    if start == end or start > end:
        return True

    return string[start] == string[end] and _is_palindrome(string, start+1, end-1)


print generate_palindromic_decompositions('abcba')
'''

'''
OPTIMIAL SOLUTION
#include<bits/stdc++.h>

using namespace std;

const int MAX_N = 20;

// ------------------------ START -------------------------

// Find is_palindrome[i][j] for all possible substrings in O(n^2) time complexity.
void find_is_palindrome_for_all_substrings(vector<vector<bool>> &is_palindrome, int n, string &s)
{
	for (int len = 1; len <= n; len++)
	{
		for (int start = 0; start < n; start++)
		{
			int stop = start + len - 1;
			// We want to find if s[start, stop] is a palindrome or not.
			if (stop >= n)
			{
				break;
			}
			is_palindrome[start][stop] = false;
			if (len <= 2)
			{
				is_palindrome[start][stop] = (s[start] == s[stop]);
			}
			else if (s[start] == s[stop])
			{
				/*
				When first and last characters are same then whether string is a palindrome or 
				not, depends on the inner string.
				For example:
				1) In "abcba", 'a' = 'a' so string is a palindrome or not will depend on "bcb".
				1) In "abcca", 'a' = 'a' so string is a palindrome or not will depend on "bcc".
				*/
				is_palindrome[start][stop] = is_palindrome[start + 1][stop - 1];
			}
		}
	}
}

vector<string> generate_palindromic_decompositions(string s)
{
	int n = s.length();
	/*
	For all substrings of s, we will pre-calculate if it is a palindrome or not.
	is_palindrome[i][j] (where i <= j and 0 <= i, j < n) will contain whether s[i, j] is a 
	palindrome or not.
	*/
	vector<vector<bool>> is_palindrome (n, vector<bool> (n, false));
	find_is_palindrome_for_all_substrings(is_palindrome, n, s);
	/* 
	decompositions_container[i] will contain all possible palindromic decompositions of s[0, i]. 
	So our answer will be decompositions_container[0, n - 1].
	We will build our solution like: 
	decompositions_container[0, 0] -> decompositions_container[0, 1] ->  ... -> 
	decompositions_container[0, n - 1].
	Why we are storing these values? -> To avoid recalculation. 
	*/
	vector<vector<string>> decompositions_container(n, vector<string>(0));
	/*
	Loop to find decompositions_container[i] (i.e. all possible palindromic decompositions of 
	s[0, i].)
	*/
	for (int i = 0; i < n; i++)
	{
		// If s[0, i] is a palindrome then add it.
		if (is_palindrome[0][i])
		{
			decompositions_container[i].push_back(s.substr(0, i + 1));
		}
		/*
		Loop to find other palindromic decompositions of s[0, i] using already calculated 
		palindromic decompositions of s[0, 0], ..., s[0, n - 1]. 
		*/
		for (int j = 0; j < i; j++)
		{
			if (is_palindrome[j + 1][i])
			{
				/*
				If s[j + 1][i] is a palindromic substring, then we can join palindromic 
				decompositions (that we have already found) of s[0, j] with it to form the 
				palindromic decomposition of s[0, i].
				*/
				string cur_sub_str = '|' + s.substr(j + 1, i - j);
				int len = decompositions_container[j].size();
				for (int k = 0; k < len; k++)
				{
					/*
					Here we are directly using previously calculated values, but in recursion we 
					recalculate them. So that is why this solution is faster than recursive 
					solution. 
					*/
					decompositions_container[i].push_back(decompositions_container[j][k] + 
						cur_sub_str);
				}
			}
		}
	}
	return decompositions_container[n - 1];
}	

// ------------------------ STOP --------------------------


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
	string scan_new_line;
	getline(cin, scan_new_line);
	getline(cin, scan_new_line);
	while (test_cases--)
	{
		string s;
		getline(cin, s);
		int n = s.length();
		assert(1 <= n);
		assert(n <= MAX_N);
		for (int i = 0; i < n; i++)
		{
			assert('a' <= s[i]);
			assert(s[i] <= 'z');
		}
		vector<string> ans = generate_palindromic_decompositions(s);
		int len = ans.size();
		cout << len << " different palindromic decompositions possible." << endl;
		for (int i = 0; i < len; i++)
		{
			cout << ans[i] << endl;
		}
		cout << endl;
	}

	return 0;
}
'''
