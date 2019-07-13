'''
String Transformation Using Given Dictionary Of Words
Problem Statement:
You are given a dictionary of words named words, and two strings named start and stop. All given strings have equal length.
 Dictionary words are not in any particular order, there may be duplicates, too.
You need to transform string start to string stop using given dictionary words. In each transformation, you can only change
 one character of the current string. e.g. "abc" -> "abd" is a valid transformation, because only one character 'c' is changed
 to 'd', but, "abc" -> "axy" is not a valid transformation, because two characters are changed, character 'b' is changed
 to 'x' and character 'c' is changed to 'y'.
In other words, you need to find out the least amount of transformations between two words start and stop, given a specific
 set of allowed transformations words. In other words, you need to find the shortest possible sequence of strings (two or
 more strings) such that:
First string is start.
Last string is stop.
Every  string (except the first one) differs from the previous one by exactly
 one character.
Every string (except, possibly, first and last ones) are in the dictionary of words.
If two or more such sequences exist, any one of them is a correct answer.
If no such sequence is there to be found, [“-1”] (a sequence of one string, “-1”) is the correct answer.
Constraints:
All input strings consist of lowercase Latin characters only.
0 <=  total number of characters in all dictionary words combined
 <= 10^5.
Input/Output Format For The Function:
Input Format:
There are three arguments:
Array of strings words,
String start,
String stop.
Output Format:
Function must return an array of strings of length >= 2, where the first string is start and the last string is stop, if
 the transformation is possible. Else return an array of strings containing only one string "-1", i.e. return ["-1"].
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting size of input array words. In next n lines, ith line should
 contain a string words[i], denoting a value at index i of words.
In next line, there should be a string start, denoting the start string. In next line, there should be a string stop, denoting
 the stop string.
If n = 4, words = ["cat", "hat", "bad", "had"], start = “bat” and stop = “had”, then input should be:
4
cat
hat
bad
had
bat
had
Output Format:
Let’s denote the size of ans array as m, where ans is the output string array returned by solution function.
There will be m lines of output, where ith line contains a string ans[i], denoting a value at index i of ans.
For input n = 4, words = ["cat", "hat", "bad", "had"], start = “bat” and stop = “had”, output will be:
bat
hat
had
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
words = ["cat", "hat", "bad", "had"]
start = "bat"
stop = "had"
Sample Output 1:
["bat", "bad", "had"]
or
["bat", "hat", "had"]
Explanation 1:
From "bat" change character 't' to 'd', so new string will be "bad".
From "bad" change character 'b' to 'h', so new string will be "had".
or
From "bat" change character 'b' to 'h', so new string will be "hat".
From "hat" change character 't' to 'd', so new string will be "had".
Sample Test Case 2:
Sample Input 2:
words = []
start = bbb
stop = bbc
Sample Output 2:
["bbb", "bbc"]
Explanation 2:
From "bbb" change the last character 'b' to 'c', so new string will be "bbc".
Sample Test Case 3:
Sample Input 3:
words = []
start = "zzzzzz"
stop = "zzzzzz"
Sample Output 3:
[-1]
Explanation 3:
Function must return an array of strings of length >= 2, where the first string is start and the last string is stop, if
 the transformation is possible. Else return an array of strings containing only one string "-1", i.e. return ["-1"].
Here, the words dictionary is empty and ["zzzzzz", "zzzzzz"] is not a valid transformation hence return ["-1"].
'''
import os
import sys

# Complete the function below.

def string_transformation(words, start, stop):
    pass


if __name__ == "__main__":
    f = sys.stdout

    words_size = int(input())

    words = []
    for _ in range(words_size):
        words_item = input()
        words.append(words_item)


    start = input()

    stop = input()

    res = string_transformation(words, start, stop)

    f.write('\n'.join(res))
    f.write('\n')
    f.close()

'''
This problem can be solved using BFS.
From current string, when we want to update neighbor strings (strings having different character at exactly one position),
 there are two methods possible:
1) Visit every string in words array and check. 
There are no_of_words strings in words array and each having length len. So, for one string to find neighbor strings, time
 taken will be O(no_of_words * len). And we will find neighbors for O(no_of_words) strings, hence time complexity of this
 solution will be O(no_of_words ^ 2 * len). Now when value of no_of_words is high, this solution will timeout.
2) For current string we will generate all possible strings having different character at exactly one position, and we will
 update strings that are in words array i.e. they are neighbors. We can use hashmap to check if any string is in words array
 or not in O(len) time, instead of O(no_of_words * len) time using simple array search. 
Now there can be O(26 * len) different strings having different character at exactly one position. And for each string we
 will spend O(len) time to check if it is in words array or not. We will find neighbors for O(no_of_words) strings, hence
 time complexity of this solution will be O(no_of_words * len^2 * 26). Now when string length is high, this solution will
 timeout. 
So, we can combine both methods in one solution to bring down time complexity to O((no_of_words * len * min((no_of_words,
 26 * len)). When (no_of_words <= 26 * len) use first method and when (no_of_words > 26 * len) use second method!
Have a look at the solution provided by us, it contains necessary comments to understand the solution. 
Time Complexity:
O(no_of_words * len * min(no_of_words, 26 * len)).
Auxiliary Space Used:
O(no_of_words * len).
Space Complexity:
O(no_of_words * len).
As input is O(no_of_words * len) and auxiliary space used is also O(no_of_words * len). So, O(no_of_words * len) + O(no_of_words
 * len) -> O(no_of_words * len).
'''
'''
#include<bits/stdc++.h>

using namespace std;

const int MIN_NO_OF_CHARS = 2, MAX_NO_OF_CHARS = 100000;

// -------------------------- START --------------------------

// Each variable is explained in the code, where it is used first.
int len, no_of_words;
queue<int> bfs_q;
vector<bool> visited;
unordered_map<string, int> position;
unordered_map<int, int> parent;

// Check if str1 and str2 differs ar exactly one positon.
bool only_one_char_difference(int len, string &str1, string &str2)
{
	int difference = 0;
	for (int i = 0; i < len; i++)
	{
		if (str1[i] != str2[i])
		{
			// If there is already one miss match, and now we have found another. 
			if (difference == 1)
			{
				return false;
			}
			difference++;
		}
	}
	// If difference == 0, it means strings are same. So, difference == 1 is needed. 
	return difference == 1;
}

// Update neighbours using O(len * len * 26) method.
void add_neighbours_with_method2(string &cur_str, int idx)
{
	// For each position.
	for (int i = 0; i < len; i++)
	{	
		// For each possible character.
		for (char ch = 'a'; ch <= 'z'; ch++)
		{
			// We want to find string having one different character, so need to skip this. 
			if (ch == cur_str[i])
			{
				continue;
			}
			// Store the original character, this will help to backtrack the change.
			char original = cur_str[i];
			// Set new character.
			cur_str[i] = ch;
			// Check if new string is in words array or not.
			auto it = position.find(cur_str);
			// If new string is in words array.
			if (it != position.end())
			{
				int position_of_cur_str_in_words_array = it->second;
				// If neighbour string is not already visited.
				if (visited[position_of_cur_str_in_words_array] == false)
				{
					// Visit it.
					visited[position_of_cur_str_in_words_array] = true;
					/*
					This string is visited by idx th string. 
					So, remember it. This will help us to construct the answer later.
					*/ 
					parent[position_of_cur_str_in_words_array] = idx;
					/*
					If we have reached the stop string. 
					Do you remember we have pushed the stop string at the end of words array!
					*/
					if (position_of_cur_str_in_words_array == no_of_words - 1)
					{
						return;
					}
					bfs_q.push(position_of_cur_str_in_words_array);
				}
			}
			// Backtrack.
			cur_str[i] = original;
		}
	}
}

// Update neighbours using O(no_of_words * len) method.
void add_neighbours_with_method1(vector<string> &words, string &cur_str, int idx)
{
	// Iterate over all words.
	for (int i = 0; i < no_of_words; i++)
	{
		// If neighbour is not visited and has only one character different from current string.
		if (visited[i] == false && only_one_char_difference(len, cur_str, words[i]))
		{
			// Mark as visited.
			visited[i] = true;
			/*
			This string is visited by idx th string. 
			So, remember it. This will help us to construct the answer later.
			*/ 
			parent[i] = idx;
			/*
			If we have reached the stop string. 
			Do you remember we have pushed the stop string at the end of words array!
			*/
			if (i == no_of_words - 1)
			{
				return;
			}
			bfs_q.push(i);
		}
	}
}

void solution(vector<string> &words, string &start, string &stop)
{
	/*
	When no_of_words > len * 26, we are going to use method2. 
	So, we need to use hash map for faster search. 
	For search if string is present in words array or not in O(len) time.
	*/ 
	if (no_of_words > len * 26)
	{
		for (int i = 0; i < no_of_words; i++)
		{
			position[words[i]] = i;
		}
	}
	// -1 means start string.
	bfs_q.push(-1);
	/*
	Visited array to track if string is visited or not, during BFS.
	visited[i] = true -> words[i] is visited in BFS.
	visited[i] = false -> words[i] is not visited in BFS till now.
	*/
	visited.assign(no_of_words, false);
	while (bfs_q.empty() == false)
	{
		int idx = bfs_q.front();
		bfs_q.pop();
		// Stores string that is at the front of queue.
		string cur_str;
		if (idx == -1)
		{
			cur_str = start; 
		}
		else
		{
			cur_str = words[idx];
		}
		// Call appropriate method to update the neighbours.
		if (no_of_words <= len * 26)
		{
			add_neighbours_with_method1(words, cur_str, idx);
		}
		else
		{
			add_neighbours_with_method2(cur_str, idx);
		}
	}
}

vector<string> string_transformation(vector<string> words, string start, string stop)
{
	// Length of each string in input.
	len = start.length();
	/*
	Add stop string in words.
	This is not necessary, but this will help to simplify the code. 
	*/
	words.push_back(stop);
	// Total no of words. stop is also included.
	no_of_words = words.size();
	// Do BFS.
	solution(words, start, stop);
	// From parent information gathered from BFS, construct the actual string transformation.
	vector<string> ans;
	/*
	Start from stop string. Go to its parent, then its parent's parent... till we reach start 
	string. 
	*/
	int stop_idx = no_of_words - 1;
	// If stop string is not reached in BFS.
	if (parent.find(stop_idx) == parent.end())
	{
		ans.push_back("-1");
		return ans;
	}
	/*
	Start from stop string. Go to its parent, then its parent's parent... till we reach start 
	string.
	*/
	while (stop_idx != -1)
	{
		ans.push_back(words[stop_idx]);
		stop_idx = parent[stop_idx];
	}
	// Add the start string.
	ans.push_back(start);
	// ans array contains strings in reverse order so reverse it. 
	reverse(ans.begin(), ans.end());
	return ans;
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
		vector<string> words(n);
		for (int i = 0; i < n; i++)
		{
			cin >> words[i];
		}
		for (int i = 1; i < n; i++)
		{
			assert(words[i - 1].length() == words[i].length());
		}
		string start, stop;
		cin >> start;
		if (n != 0)
		{
			assert(start.length() == words[0].length());
		}
		cin >> stop;
		assert(start.length() == stop.length());
		assert(MIN_NO_OF_CHARS <= (n + 2LL) * start.length());
		assert((n + 2LL) * start.length() <= MAX_NO_OF_CHARS);
		while(bfs_q.empty() == false)
		{
			bfs_q.pop();
		}
		position.clear();
		parent.clear();
		vector<string> ans = string_transformation(words, start, stop);
		int ans_size = ans.size();
		if (ans_size != 1)
		{
			assert(ans[0] == start);
			assert(ans[ans_size - 1] == stop);
		}
		for (int i = 0; i < ans_size; i++)
		{
			if (i > 0)
			{
				assert(only_one_char_difference(len, ans[i - 1], ans[i]));
			}
			cout << ans[i] << endl;
		}
		cout << endl;
	}

	return 0;
}
'''




