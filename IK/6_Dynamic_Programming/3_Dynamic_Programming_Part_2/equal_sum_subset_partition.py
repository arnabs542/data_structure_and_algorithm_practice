'''
Equal Sum Subset Partition
Problem Statement:
Given an array s of n integers. Your task is to partition the given set s into two subsets, say s1 and s2 such that sum
 of all elements in s1 is equal to the sum of all elements in set s2. If it is not possible to partition the array s then
 returns a blank array else return a boolean array of size n where i (0<=i<n) element is true if it is part of s1 and false
 if it is part of s2.
Input/Output Format For The Function:
Input Format:
The first and only parameter of the function that is to be implemented is the array of integers s, that is to be partitioned.

Output Format:
If it is possible to partition the given array s in an above-said manner then return a boolean array of size n, where its
 i (0<=i<N) element is true if it is the part of s1 else false if it is the part of s2. In case it is not possible to partition
 the array s, then return an empty array.
Input/Output Format For The Custom Input:
Input Format:
The first line of the text file contains one single integer n, denoting number of elements in array s.
Next n lines of the input, each line contains single integer denoting the ith element in the array s.
If n = 3 and s = [1, 0, -1], then custom input format will be:
3
1
0
-1
Output Format:
If a valid partition exists, then the first line contains an integer s1, denoting the size of the first subset and next
 S1 line contains
ith elements in the set s1 in the order they appear in the input array s. Next line contains an integer s2, denoting the
 size of the second subset. Next s2 lines will contain integers denoting the ith element in the set s2 in the order they
 appear in the input array s.
In case a valid partition is not possible the output contains only one line having integer -1.
For the above-provided custom input, one possible custom output could be:
2
1
-1
1
0
Constraints:
1 <= n <= 100
-100 <= elements in s <= 100
Sample Test Case:
n = 6
s = [10, -3, 7, 2, 1, 3]
Sample Output:
[True, True, False, False, False, True]
Explanation:
For the above sample output.  There is only one possible partition to satisfy the equal subset sum condition. The two subsets
 are as follows:
For s1 we pick the 0, 1 and 5 indexed elements
s1 = [ 10 , -3 , 3 ]
Here, the sum elements of s1 is 10 + 3 – 3 = 10
For s2 we pick the 2, 3 and 4 indexed elements
s2 = [ 7 , 2 , 1 ]
Here, the sum elements of s1 is 7 + 2 + 1 = 10
Hence, the sum of both the subsets s1 and s2 is 10.
'''
import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000100)


#
#  Complete the equalSubSetSumPartition function below.
#
#  @param s: input array as parameter.
#
def equalSubSetSumPartition(s):
    pass



if __name__ == '__main__':
    n = int(input().strip())
    s = []
    for i in range(0, n):
        S_item = int(input().strip())
        s.append(S_item)
    fptr = sys.stdout
    result = equalSubSetSumPartition(s)
    if(len(result) == 0):
        fptr.write('-1\n')
        sys.exit()
    s1 = result.count(1)
    s2 = result.count(0)
    fptr.write(str(s1) + "\n")
    for i in range(0, len(result)):
        if(result[i] == True):
            fptr.write(str(s[i]) + "\n")
    fptr.write(str(s2) + "\n")
    for i in range(0, len(result)):
        if(result[i] == False):
            fptr.write(str(s[i]) + "\n")
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution:
Description:
This partition problem simply reduces to find a subset of the given array such that the sum of the given array is equal
 to sum/2, where the sum is the total sum of elements of the given array. Also, if the value of the sum is odd then we cannot
 partition it into two equal subsets. So, in case the value of the sum is odd we simply return an empty array.
Now, In this approach, we iterate on all possible combinations of subsets of the given array and check if the current subset
 sums to sum/2. If we are able to find once such subset then we declare this subset as s1 and rest of other remaining elements
 of the subset as s2 and return the denomination array as specified in the output section on the problem statement. Kindly,
 refer to the code for better understanding of the approach.
Time Complexity:
O(n*2^n) where n is the number of elements in the given input array.
As we are iterating on all possible subsets i.e. 2^n subsets for an array of size n. Hence, we are doing O(2^n) iterations
 and then for each subset, we are computing its sum. To do this we need to iterate on each element of the subset that takes
 O(n) time of each individual subset. Hence, the total time complexity becomes O(2^n) * O(n) ~ O(n*2^n).
Auxiliary Space Used:
O(n) where n is the number of elements in the given input array.
To generate all partitions we are recursively backtracking on all indexes of the array. So, at any point of time the recursion
 stack will occupy max O(n) stack size.
Apart this we are only traversing on the given subarray multiple times for different subsets without maintaining any state
 information, hence we do not allocate any space for processing. The only space we allocate is the final return array that
 is of size n and hence the total auxiliary space complexity is O(n) +  O(n) ~ O(n).
Space Complexity:
O(n) where n is the number of elements in the given input array.
Auxiliary space + the Input Space i.e. O(n) + O(n) →  O(n).
2) optimal_solution:
Description:
As discussed in the brute_force approach we have simply reduced this problem to a subset sum problem such that given an
 array s and we need to first check if a subset exists with the subset sum of sum/2. If it exists then we need to separate
 that subset from the rest of elements of the array. We will be using dynamic programming to solve this problem. Our first
 aim will be to check if a subset with sum sum/2 exists or not. To do so, we will be maintaining a 2D DP state as following
 :
Boolean state(idx, sum).
Here, state(idx, sum) tell us if it is possible to get a subset sum of the sum provided the elements from 0 to idx of the
 given array.
Now, our state transition will look like below:
state(idx, sum) = state(idx-1, sum) | state(idx, sum – s[idx])
So, using the above state transition we will populate all our DP states. Now, we simply check the value of state(n-1, sum/2)
 (assumed 0-based array index). If it is true then it is possible to partition the given array and if it is false then once
 again we return an empty array.
Now, to get the partition we start a top-down lookup on our DP states. We start from the state(n-1, sum/2). If this state
 is true and state(n-2, sum/2) is false this means s[n-1] contributed in the subset sum and if it is false we go to state(n-2,
 sum/2) to identify our contributors of the subset sum of sum/2. We repeat this reverse DP transition until the point we
 reach the first index of the array or till the point, the required sum becomes 0. While doing these reverse DP transitions
 we also mark the contributed elements as s1 subset elements and rest of the array as s2 elements.
Because the elements in our array can also be negative and hence we use a hash-based container like unordered_map in C++
 to overcome this problem of negative indexing.
Kindly, refer to the solution for implementation details.
Time Complexity:
O(n*range_sum) since this is a pseudo-polynomial time problem where n is the number of elements in the given input array
 and range_sum is the absolute difference between the maximum sum and the minimum sum possible in the given input array
 s.
As we are visiting all the DP states i.e. n*range_sum, hence we will be doing n*range_sum iterations and for each state,
 we are doing O(1) amount of work and also because of memorization each state is being visited once. Hence, the total time
 complexity of this solution is O(n*range_sum).
Auxiliary Space Used:
O(n*range_sum) where n is the number of elements in the given input array and range_sum is the absolute difference between
 the maximum sum and the minimum sum possible in the given input array s.
Since we are using an auxiliary container of size n*range_sum to store the DP states. So, the auxiliary space complexity
 is O(n*range_sum).
Space Complexity:
O(n*range_sum) where n is the number of elements in the given input array and range_sum is the absolute difference between
 the maximum sum and the minimum sum possible in the given input array s.
Auxiliary space + the Input space i.e. O(n*range_sum) + O(n) →  O(n*range_sum).
'''
'''
BRUTE FORCE
#include "bits/stdc++.h"
using namespace std;

// ------------------------------ START ------------------------------

// returns true if the result array subsets gives
// a valid partition for the array v
bool validator(vector<int> &v, vector<bool> &subsets)
{
    // stores sum of subset s1
    int sum1 = 0;
    // stores sum of subset s2
    int sum2 = 0;
    // counts number of elements in s2
    int sz = count(subsets.begin(), subsets.end(), true);
    int n = v.size();
    // basic sanity check
    if (sz == 0 or sz == n or subsets.size() != n)
    {
        return false;
    }
    // loop into array v and calculate s1 and s2 sum
    for (int i = 0; i < n; i++)
    {
        // if 0 belongs to s1
        if (subsets[i] == 0)
            sum1 += v[i];
        // if 1 belongs to s1
        else if (subsets[i] == 1)
            sum2 += v[i];
        else
        { // invalid output
            return false;
        }
    }
    // check if subset sum s1 equals subset sum s2
    if (sum1 != sum2)
    {
        return false;
    }
    return true;
}

// resursive backtracking to generate all subset partition
void solver(vector<bool> &vis, vector<int> &s, int idx, bool &solutionFound)
{
    if (idx == s.size())
    {
        // check if current partition is valid or not
        solutionFound = validator(s, vis);
        return;
    }

    if (!solutionFound)
    {
        solver(vis, s, idx + 1, solutionFound);
    }

    if (!solutionFound)
    {
        // add current idx element in subset 1
        vis[idx] = 1;
        solver(vis, s, idx + 1, solutionFound);
        // remove current element forom subset 1
        vis[idx] = solutionFound;
    }
}

vector<bool> equalSubSetSumPartition(vector<int> &s)
{
    // flag to indicate if solution is found in
    // recursion
    bool solutionFound = false;
    vector<bool> resultSubset(s.size(), 0);
    // recursively generates all possible partitions
    // and checks for solution
    solver(resultSubset, s, 0, solutionFound);
    if (!solutionFound)
    {
        // empty the array if no result found
        resultSubset.clear();
    }
    // return the resultant subset partition
    return resultSubset;
}
// ------------------------------ STOP ------------------------------

int main(int argc, char const *argv[])
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output.txt", "w",
    //     stdout);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output.txt", "w",
    //     stdout);

    // int t;
    // cin >> t;
    // while (t--)
    // {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    vector<bool> result = equalSubSetSumPartition(v);
    if (result.size() == 0)
    {
        cout << -1 << endl;
        return 0;
    }
    // assert(result.size() == n);
    int sz = 0;
    for (int i = 0; i < n; i++)
    {
        if (result[i])
            sz++;
    }
    cout << sz << endl;
    for (int i = 0; i < n; i++)
    {
        if (result[i])
            cout << v[i] << endl;
    }
    cout << n - sz << endl;
    for (int i = 0; i < n; i++)
    {
        if (!result[i])
            cout << v[i] << endl;
    }
    //     assert(validator(v, result) == true);
    // }
    return 0;
}
'''
'''
#include "bits/stdc++.h"
using namespace std;

// returns true if the result array subsets gives
// a valid partition for the array v
bool validator(vector<int> &v, vector<bool> &subsets)
{
    // stores sum of subset s1
    int sum1 = 0;
    // stores sum of subset s2
    int sum2 = 0;
    // counts number of elements in s2
    int sz = count(subsets.begin(), subsets.end(), true);
    int n = v.size();
    // basic sanity check
    if (sz == 0 or sz == n or subsets.size() != n)
    {
        return false;
    }
    // loop into array v and calculate s1 and s2 sum
    for (int i = 0; i < n; i++)
    {
        // if 0 belongs to s1
        if (subsets[i] == 0)
            sum1 += v[i];
        // if 1 belongs to s1
        else if (subsets[i] == 1)
            sum2 += v[i];
        else
        { // invalid output
            return false;
        }
    }
    // check if subset sum s1 equals subset sum s2
    if (sum1 != sum2)
    {
        return false;
    }
    return true;
}

// ------------------------------ START ------------------------------

vector<bool> equalSubSetSumPartition(vector<int> &s)
{
    // store min and max sum possible for given array
    int sum_neg = 0, sum_pos = 0;
    // calculate min and max subset sums
    for (auto val : s)
    {
        if (val < 0)
            sum_neg += val;
        else
            sum_pos += val;
    }

    // total sum of the array
    int sum = sum_pos + sum_neg;
    // Partition not possible
    if (sum & 1)
    {
        vector<bool> ret;
        // return empty array
        return ret;
    }

    int n = s.size();

    // dp state
    unordered_map<int, bool> dp[n];

    // base state
    // for idx 0 only one sum s[0] is possible
    dp[0][s[0]] = true;

    // iterate on all idx
    for (int i = 1; i < n; i++)
    {
        // iterate on all possible subset sum
        for (int val = sum_neg; val <= sum_pos; val++)
        {
            // dp state-transition

            // 1) state(i,val) = state(i-1,val) without taking current element
            dp[i][val] = dp[i - 1][val];

            // 2) if val == s[i], just taking ith element is sufficient
            if (val == s[i])
                dp[i][val] = true;
            else if (val - s[i] >= sum_neg)
            {
                // 3) state(i,val) = state(i-1,val-s[i]) when taking current element
                dp[i][val] |= dp[i - 1][val - s[i]];
            }
        }
    }

    int required = sum / 2;
    int idx = n - 1;

    // parition not possible
    if (!dp[idx][required])
    {
        vector<bool> ret;
        return ret;
    }

    // tracks partition elements
    vector<bool> resultSubset(s.size(), 0);
    // tracks count of elements included in S1
    int cnt = 0;
    while (idx >= 0)
    {
        if (idx != 0)
        {
            // reverse dp transition
            if (dp[idx][required] and !dp[idx - 1][required])
            {
                resultSubset[idx] = 1;
                cnt++;
                required -= s[idx];
                if (required == 0)
                    break;
            }
        }
        else
        {
            resultSubset[idx] = 1;
            cnt++;
        }
        idx--;
    }

    // if all elements are included in S1
    // All elements will be in S1 if total_sum = 0
    // case when s = [-2,2]
    // partition is not possible in this case
    if (cnt == n)
    {
        resultSubset.clear();
    }
    return resultSubset;
}

// ------------------------------ STOP ------------------------------

int main(int argc, char const *argv[])
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output.txt", "w",
    //     stdout);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output.txt", "w",
    //     stdout);

    // int t;
    // cin >> t;
    // while (t--)
    // {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    vector<bool> result = equalSubSetSumPartition(v);
    if (result.size() == 0)
    {
        cout << -1 << endl;
        return 0;
    }
    // assert(result.size() == n);
    int sz = 0;
    for (int i = 0; i < n; i++)
    {
        if (result[i])
            sz++;
    }
    cout << sz << endl;
    for (int i = 0; i < n; i++)
    {
        if (result[i])
            cout << v[i] << endl;
    }
    cout << n - sz << endl;
    for (int i = 0; i < n; i++)
    {
        if (!result[i])
            cout << v[i] << endl;
    }
    // assert(validator(v, result) == true);
    // }
    return 0;
}
'''



