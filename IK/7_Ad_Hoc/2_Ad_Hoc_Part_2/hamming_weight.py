'''
Hamming Weight
Problem Statement:
Hamming Weight of an integer x is defined as the total number of set bits in the binary representation of the integer x.
 Now, given an array s of n integers. We need to calculate the total hamming weight of the array s i.e. to sum-up the individual
 hamming weight of each integer in the array S.
Input/Output Format For The Function:
Input Format:
First and only parameter of the function that is to be implemented the array of 64-bit integers s.
Output Format:
The function returns an integer variable storing the value of the total hamming weight of the given input array s.
Input/Output Format For The Custom Input:
Input Format:
First line of the input contains one single integer n, denoting number of elements in array s.
Next n lines of the input, each line contains single integer denoting the ith element in the array s.
If n = 3 and s = [ 1, 2, 3 ], then custom input format will be:
3
1
2
3

Output Format:
Print one single line containing one integer denoting the total hamming weight of the input array s.
For the above provided custom input, output would be:
4

Constraints:
1 <= n <= 10^5
0 <= s[i] < 2^32 where 0 <= i < n.

Sample Test Case:
n = 3
s = [ 1, 2, 3 ]

Sample Output:
4

Explanation:
For the array s = [1, 2, 3], number of set bits for each element of the array is mentioned below:
Binary representation of 1 is “1” so set bits in 1 is 1.
Binary representation of 2 is “10” so set bits in 2 is 1.
Binary representation of 3 is “11” so set bits in 3 are 2.
So, total set bits in 1 + set bits in 2 + set bits in 3 are 1 + 1 + 2 = 4. Hence Summing hamming weight of given array [1, 2, 3] is 4.
'''
import math
import os
import random
import re
import sys

#
#  Complete the calculateHammingWeight function below.
#  @param s: input array as parameter.
#
#
def calculateHammingWeight(s):
    pass




if __name__ == '__main__':
    n = int(input().strip())
    s = []
    for i in range(0, n):
        s_item = int(input().strip())
        s.append(s_item)
    fptr = sys.stdout
    result = calculateHammingWeight(s)
    fptr.write(str(result) + "\n")
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution:
Description:
As per the constraints, all the elements in the array can be stored in a 32-bit integer and hence, to calculate the number
 of set bits in an integer x, we can iterate on all these 32 bits of the corresponding integer and keep a count of the number
 of set bits.
We repeat the same process for all integers in the given input array s and keep the count of total set bits in all integers.
 To optimize the solution we can break traversal over the bits once we encounter the MSB(Most Significant Bit / Leftmost
 set bit) in the integer x.
Time Complexity:
O(n*32) where n is number elements in the given input array.
For every integer in the array, we are iterating over 32 bits in its binary representation. So, for n integers, time complexity
 becomes O(n*32).
Auxiliary Space Used:
O(1).
Since we are only traversing on the bits of the integers in array s without storing any data regarding set bits and hence,
 the Auxiliary Space complexity is O(1).
Space Complexity:
O(n) where n is number of elements in the given array s.
For storing input, it will take O(n) and as auxiliary space used is O(1) hence total complexity will be O(n) + O(1) → O(n).

2) optimal_solution:
Description:
Our main aim of the solution is to calculate the hamming distance of an integer x in constant time with some precomputation.

As the integer size is 32 bit as per the input constraints. So, we can divide the 32-bit integer x, into two 16-bits integers.

[31th , 30th , ……. , 17th, 16th] [ 15th , 14th, ………. , 1th , 0th]
A	B
Let’s call the first part i.e. from [31th bit to 16th bit] as A and second part from [15th bit to 0th] bit as B. Also, note
 that both these integers A and B are 16-bit integers. Now, the total set bits in the integer x is equal to number of set
 bits in integer A + number of set bits in integer B and this is the key idea for this solution. Now let Sz be the number
 of all possible 16-bit integers. So, we precompute the number of set bits for all Sz integers and store it in memory. We
 can compute the set bits for all Sz integers in linear time. Let’s say dp[i] denotes the number of set bits in integer
 i. So, we can compute dp[i] using the below state relation :
dp[i] = dp[i >> 1] + (i&1)
In the above relation (i&1) tells if the 0th bit is set in the binary representation of the integer i. To illustrate the
 above relation, consider the calculation of dp[5].
Now, (5)base10 = (101)base2
So, dp[5] = dp[5 >> 1] + 5&1
Here 5&1 is 1 as the 0th bit is set in binary representation of 5.
As now, we have taken 0th bit of 5 under consideration and hence, now we can right shift the binary representation of 5
 by 1 to omit the 0th bit and then calculate the number of set bits in the resulting integer. Also, as right shifting 5
 by 1 will result in an integer which is less than 5 and as we are iteratively computing dp states the resultant state dp[5>>1]
 would have already been computed.
Hence, dp[5] = dp[2] + 1 i.e. last bit in 5 plus the number of set bits in 2.
Once, we have precomputed set bits individually for all 16-bit integers. We can answer calculate the number of set bits
 in a 32-bit integer by two lookups in the precomputed state values.
So, for an integer x we first divide it into A and B as explained above and then we do a lookup in our dp[A] and dp[B] to
 get the set bits in the integer x.
We repeat the same process for all integers in the array s and keep count of the total number of set bits and hence, the
 hamming weight of the array.
Also, instead of dividing the array into 2 parts, we can divide it into 4 integers each of size 8 bits and proceed the same
 way as we did in the above explanation. This will reduce the space complexity significantly, but will require 4 lookups
 and hence will double the previous time complexity. Though, the asymptotics remain the same.
Bonus take away – this is called as the Space-Time trade off.
Kindly, refer to the solution for implementation details.
Time Complexity:
O(n + Sz) where n is number of elements in the given array s and Sz be the number of all possible 16-bit integers i.e. 2^16.

Precomputing dp state for all 16 bit integers take a linear time O(2^16) as explained above. To calculate the set bits in
 an integer x we are performing 2 iterations. Hence, for all n integers the time complexity become O(2*n). Summing up the
 overall time complexity becomes O( 2*n + Sz ) →  O(n + Sz).
Auxiliary Space Used:
O(Sz) where Sz be the number of all possible 16-bit integers i.e. 2^16.
As, we are pre-computing set bits for all 16 bit integers and storing it. Hence the space complexity is O(Sz).
Space Complexity:
O(n + Sz) where n is number of elements in the given array s and Sz be the number of all possible 16-bit integers i.e. 2^16.

For storing input, it will take O(n) and as auxiliary space used is O(Sz) hence total complexity will be O(n) + O(Sz) →
 O(n + Sz).
'''
'''
BRUTE FORCE
#include "bits/stdc++.h"
using namespace std;

// ------------------------------ START ------------------------------

int calculateHammingWeight(vector<long long> &s)
{
    // stores total number of set bits in all elements
    int totalSetBits = 0;
    // max number of bits in an integer (input constraint)
    int maxNumberOfBits = 32;
    int N = s.size();
    for (int i = 0; i < N; i++)
    {
        // iterate over all bits of s[i]
        for (int j = 0; j < maxNumberOfBits; j++)
        {
            // if jth bit is set increment totalSetBits
            if (s[i] & (1LL << j))
                totalSetBits++;
        }
    }
    // return final count of set bits
    return totalSetBits;
}
// ------------------------------ STOP ------------------------------

int main(int argc, char const *argv[])
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output1.txt", "w",
    //     stdout);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);

    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output1.txt", "w",
    //     stdout);

    // string testcases;
    // getline(cin, testcases);
    // int t = stoi(testcases);
    // while (t--)
    // {
    int n;
    cin >> n;
    vector<long long> s(n);
    for (int i = 0; i < n; i++)
    {
        cin >> s[i];
    }
    int ans = calculateHammingWeight(s);
    cout << ans << endl;
    // }
    return 0;
}
'''
'''
OPTIMAL SOLUTION
#include "bits/stdc++.h"
using namespace std;

// ------------------------------ START ------------------------------

int calculateHammingWeight(vector<long long> &s)
{
    // size of mem dp table
    int sz = 1 << 16;
    // number of elements in s
    int N = s.size();
    // stores set bits in integers
    int memo[sz];
    // 0 set bits in integer 0
    memo[0] = 0;
    // using dp-state relation to populate
    // all dp states
    for (int i = 1; i < sz; i++)
    {
        memo[i] = memo[i >> 1] + (i & 1);
    }
    // total set bits in all N elements of s
    int totalSetBits = 0;
    // bit mask = (1<<16) - 1 = (1111111111111111) in binary
    int bitMask = sz - 1;
    // iterate over all elements in array
    for (int i = 0; i < N; i++)
    {
        // add set bits from (0th to 15th) bits position
        totalSetBits += memo[s[i] & bitMask];
        // shift s[i] 16 positions to right
        s[i] = s[i] >> 16;
        // again add set bits from (0th to 15th) bits position
        totalSetBits += memo[s[i] & bitMask];
    }
    return totalSetBits;
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

    // string testcases;
    // getline(cin, testcases);
    // int t = stoi(testcases);
    // while (t--)
    // {
    int n;
    cin >> n;
    vector<long long> s(n);
    for (int i = 0; i < n; i++)
    {
        cin >> s[i];
    }
    int ans = calculateHammingWeight(s);
    cout << ans << endl;
    // }
    return 0;
}
'''



