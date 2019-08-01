'''
Maximum In Sliding Window
Problem Statement:
An integer array named arr is given to you. Size of arr is n and assume that it is very large.
There is a sliding window of size w, which is moving from the very left of the array to the very right. You can only see
 the w numbers in the window. Each time the sliding window moves rightwards by one position. You have to find maximum number
 in the window each time.
Input/Output Format For The Function:
Input Format:
There are two arguments in input. First is an integer array arr. Second is the window width w.
Output Format:
Return an array res, of size (n-w+1), where i-th number of the returned array contains the maximum number in window from
 arr[i] to arr[i+w-1].
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting the length of input array arr. In next n lines, ith line should
 contain an integer arr[i], denoting value at index i of arr. In the next line, there should be an integer w, denoting size
 of window.
If n = 8, arr = [1, 3, -1, -3, 5, 3, 6, 7] and w = 3, then input should be:
8
1
3
-1
-3
5
3
6
7
3
Output Format:
There will be (n-w+1) lines, where ith line contains an integer res[i], denoting the value at index i of res. res is the
 result returned by the solution function.
For input n = 8, arr = [1, 3, -1, -3, 5, 3, 6, 7] and w = 3, output will be:
3
3
5
5
6
7
Constraints:
    * 1 <= n <= 10^5
    * -2 * 10^9 <= arr[i] <= 2 * 10^9
    * 1 <= w <= n
Sample Test Case:
Sample Input:
arr = [1 3 -1 -3 5 3 6 7]
w = 3
Sample Output:
[3, 3, 5, 5, 6, 7]
Explanation:
Window Position -> Max
1) [1 3 -1] -3 5 3 6 7 -> 3
2) 1 [3 -1 -3] 5 3 6 7 -> 3
3) 1 3 [-1 -3 5] 3 6 7 -> 5
4) 1 3 -1 [-3 5 3] 6 7 -> 5
5) 1 3 -1 -3 [5 3 6] 7 -> 6
6) 1 3 -1 -3 5 [3 6 7] -> 7
Notes:
Suggested time in interview: 20 minutes.
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework i.e.
 For the first attempt of a given homework problem, the focus should be to understand what the problem is asking, what approach
 you are using, coding it, as well as identifying any gaps that you can discuss during a TC session. Take your time, but
 limit yourself to 2 one hour sessions for most problems.
'''
#!/bin/python3

import sys
import os

# Complete the function below.

def max_in_sliding_window(arr, w):
    pass


if __name__ == "__main__":
    f = sys.stdout

    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input())
        arr.append(arr_item)
        arr_i += 1


    w = int(input())

    res = max_in_sliding_window(arr, w);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()

'''
Input:
arr = [1 3 -1 -3 5 3 6 7] (n = 8)
w = 3
Output:
ans = [3, 3, 5, 5, 6, 7] (size = 6)
Size of the ans = (n - w + 1) = 8 - 3 + 1 = 6.
We can go through window of size w, (n - w + 1) times. So this brute force solution will be of time complexity O((n - w + 1) * w).
First time we will find maximum number in arr[0, w - 1].
Second time we will find maximum number in arr[1, w] and so on. 
Here we can clearly see that finding maximum number of arr[1, w - 1] is common in first and second time.
So we can remove this recomputation and speedup! 
We can use data structures like heap, priority queue or balanced BST, and speedup to O(n * log(w)).
Now still it can be improved to O(n). 
Trick is to find a way such that the largest element in the window would always appear in the front of the queue.
Have a look at the solution provided by us for O(n) solution. 
Time Complexity:
O(n).
As we are adding each element in deque once and removing each element at most once.
Auxiliary Space Used:
O(k).
As we are using deque and it can be maximum of size k.
Space Complexity: 
O(n).
Input is of size O(n) and auxiliary space used is O(k) hence O(k) + O(n) -> O(k + n) -> given that k <= n -> O(n + n) -> O(n). 
'''
'''
#include<bits/stdc++.h>

using namespace std;

const int MAX_N = 100000, MIN_NO = -2000000000, MAX_NO = 2000000000;  

// -------------------------- START --------------------------

vector<int> max_in_sliding_window(vector<int> arr, int w)
{
	int n = arr.size();
	/*
	Input:
	arr = [1 3 -1 -3 5 3 6 7] (n = 8)
	w = 3

	Output:
	ans = [3, 3, 5, 5, 6, 7] (size = 6)
	
	Size of the ans = n - w + 1 = 8 - 3 + 1 = 6.
	*/
	vector<int> ans(n - w + 1);
	// Note that we are storing indices not values, in deque.
	deque<int> indices;
	/*
	Input:
	arr = [1 3 -1 -3 5 3 6 7] (n = 8)
	w = 3

	For each step we can uniquely define the window by its right most element index. 

	All possible windows:
	[1 3 -1] -3 5 3 6 7 -> 2 (and this index is w - 1)
	1 [3 -1 -3] 5 3 6 7 -> 3
	1 3 [-1 -3 5] 3 6 7 -> 4
	1 3 -1 [-3 5 3] 6 7 -> 5
	1 3 -1 -3 [5 3 6] 7 -> 6
	1 3 -1 -3 5 [3 6 7] -> 7 (and this index is n - 1)

	So for i = 0 to w - 2, we will just setup the deque and for i = w - 1 to n - 1, we will add 
	the answer. 
	*/
	for (int i = 0; i < n; i++)
	{
		/*
		Suppose arr[j] <= arr[i] where j < i, then arr[j] is not needed, it can be removed. 
		ith number is on the right side of jth number and jth number is <= ith number, so jth 
		number can never be the answer for further calculations! 
		Try some examples to understand this clearly!
		*/
		while (!indices.empty() && arr[indices.back()] <= arr[i])
		{
			indices.pop_back();
		}
		// Add current index.
		indices.push_back(i);
		// If i >= w - 1 then add the answer for window arr[i - w + 1, i].
		if (i >= w - 1)
		{
			/*
			Current window should only see elements in arr[i - w + 1, i], so remove previous 
			elements if any.
			When i >= w then only this while loop can be executed, so we have placed this inside 
			if statement.
			*/
			while (indices.front() <= i - w)
			{
				indices.pop_front();
			}
			/*
			Observe that deque contains numbers in decreasing order, so first number is the 
			maximum number! 
			*/
			ans[i - w + 1] = arr[indices.front()];
		}
	}
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
	while (test_cases--)
	{
		int n;
		cin >> n;
		assert(1 <= n);
		assert(n <= MAX_N);
		vector<int> arr(n);
		for (int i = 0; i < n; i++)
		{
			cin >> arr[i];
			assert(MIN_NO <= arr[i]);
			assert(arr[i] <= MAX_NO);
		}
		int w;
		cin >> w;
		assert(1 <= w);
		assert(w <= n);

		vector<int> ans = max_in_sliding_window(arr, w);
		
		int len = ans.size();
		assert(len == n - w + 1);
		// cout << len << endl;
		for (int i = 0; i < len; i++)
		{
			//set<int> vals(arr.begin() + i, arr.begin() + i + w);
			//assert(ans[i] == *vals.rbegin());
			cout << ans[i] << endl;
		}
		cout << endl;
	}

	return 0;
}
'''
