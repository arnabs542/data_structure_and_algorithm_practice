'''
Sum Zero
Problem Statement:
Given an array of integers arr of size n, find a non-empty subarray resSubArray such that sum of elements in resSubArray
 is zero.
Input/Output Format For The Function:
Input Format:
There is only one argument, arr denoting input array.
Output Format:
Return an array of integer res of size 2, where res[0] and res[1] denotes start index and end index(0 based indexing) (both
 inclusive) respectively for resSubArray in arr.
Note that:
    If there is no such subarray, then return array res of size one and res[0] = -1.
    If there are multiple such subarray, then return indices for any one of them.
    If a matching subarray is a subarray of a larger matching subarray, then return indices for either one.
    If there is a number '0' in the array arr, then it counts as a valid sum zero subarray.
Input/Output Format For The Custom Input:
Input Format:
The first line of the input should contain a single integer n, denoting the size of input array arr.
In the next n lines, ith line should contain an integer denoting arr[i].
If n = 6 and arr = [5, 1, 2, -3, 7, -4], then input should be:
6
5
1
2
-3
7
-4


If n = 5 and arr = [1, 2, 3, 5, -9], then input should be:
5
1
2
3
5
-9


Output Format:
There are two cases here:
1. If a valid sum zero subarray exists in arr, then there will be two lines for output. First line will have an integer
 res[0] and second line will have an integer res[1], denoting starting index and ending index of required subarray (0 based
 indexing, both inclusive).
2. Otherwise if there is no valid sum zero subarray, there will be only one line for output, having an integer -1.

For input n = 6 and arr = [5, 1, 2, -3, 7, -4], output will be:
1
3

For input n = 5 and arr = [1, 2, 3, 5, -9], output will be:
-1

Constraints:
1 <= n <= 5*10^5
-10^9 <= arr[i] <= 10^9, (i = 0,1,...,(n-1))
Sample Test Cases:
Sample Input 1:
6
5
1
2
-3
7
-4

Sample Output 1:
1
3

Explanation 1:
For given input array arr, arr[1]+arr[2]+arr[3] = 1+2+(-3) = 0. So, subarray starting from index 1 upto index 3 (0 based
 indexing) is sum zero subarray.
(3,5 and 1,5 are the other correct solutions)

Sample Input 2:
5
1
2
3
5
-9

Sample Output 2:
-1

Explanation 2:
For given input array arr, there is no subarray such that sum of integers in that subarray is 0.
So, -1 is printed as output.
'''
import math
import os
import random
import re
import sys

# Complete the sumZero function below.
def sumZero(arr):
    pass


if __name__ == "__main__":
    fptr = sys.stdout
    arr_count = int(input())
    arr = []
    for _ in range(arr_count):
        arr_item = int(input())
        arr.append(arr_item)
    res = sumZero(arr)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
A naive approach would be, to iterate over all possible subarrays of input array arr, such that while on subarray [i,j],
 i.e. subarray starting from ith index and ending at jth index, find sum of elements in it and if it's zero, return {i,j}.
 If no such subarray found, return {-1}.
Time Complexity:
O(n*n) where n is length of input arr.
As we are iterating over all possible subarrays of input array arr, time complexity will be O(n*n).
Auxiliary Space Used:
O(1).
We are not storing anything extra.
Space Complexity:
O(n) where n is length of input arr.
To store input it takes O(n) and as auxiliary space used is O(1).
Hence, O(n) + O(1) → O(n).
2) optimal_solution.java
Description:
An optimal approach would be as follows:
Notice that if there exists a zero sum subarray [i,j] in a given input array arr, then prefix sum (denote it as prefix where
 prefix[k] = arr[0] + arr[1] + arr[2] + ... + arr[k]) prefix[j] should be equal to prefix[i-1], as prefix[j] = prefix[i-1]
 + (arr[i] + arr[i+1] + ... + arr[j]), where the term in bracket is sum of subarray [i,j], which is 0.
Considering this fact, build prefix sum array prefix. If for some i, j, 0 <= i <= j < n, prefix[i-1] = prefix[j], then subarray
 [i,j] is the zero sum subarray.
Time Complexity:
O(n) where n is length of input arr.
To find out if any two sums of subarrays are equal or not we will store them in HashMap as prefix[k] (i.e. sum) as key and
 k as value. To maintain hashmap it will take O(n) time complexity in worst case to get and store n sums.
Auxiliary Space Used:
O(n) where n is length of input arr.
We are using hashmap to store sums. It will take O(n) of space.
Space Complexity:
O(n) where n is length of input arr.
To store input it takes O(n) and as auxiliary space used is O(n).
Hence, O(n) + O(n) → O(n).
'''
'''
BRUTE FORCE
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given an array of integers arr of size n, find a subarray whose sum is zero.
 */
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static int[] sumZero(int[] arr) {
        // To store interval (start, end) for which sum is zero
        int[] res = new int[2];
        // To store current sum
        long sum = 0;
        // We are trying to find sum of each subarray[i, n-1] where 0<=i<=n-1.
        for (int i = 0; i < arr.length; i++) {
            sum = 0;
            // To calculate sum of subarray starting from i and ending at n-1 
            for (int j = i; j < arr.length; j++) {
                sum += arr[j];
                // If sum == 0 means we found our subarray having sum as 0 with start index i 
                // and end index j
                if (sum == 0) {
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
            }
        }
        // If no subarray as sum equal to zero found then we will return [-1]
        return new int[]{-1};
    }
    // -------------------- END ----------------------
}

class Solution{
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(bufferedReader.readLine());

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(bufferedReader.readLine());
        }

        int[] resSubArray = Result.sumZero(arr);

        for (int i = 0; i < resSubArray.length; i++) {
            bufferedWriter.write(String.valueOf(resSubArray[i])+"\n");
        }
        bufferedWriter.newLine();
        
        bufferedWriter.close();

        bufferedReader.close();
    }

}
/**
 * Time complexity: O(n*n)
 * Space complexity: O(n)
 */

'''
'''
OPTIMAL SOLUTION
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given an array of integers arr of size n, find a subarray whose sum is zero.
 */
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static int[] sumZero(int[] arr) {
        // To store interval (start, end) for which sum is zero
        int[] res = new int[2];
        // To store prefix sum i.e. sum of subarray starting at index 0 and ending at index i
        // Key of hashmap will be sum and value will be index i for prefix sum
        HashMap<Long, Integer> map = new HashMap<>();
        // To check whether prefix sum it self is equal to zero
        map.put(0l, -1);
        // To store current sum
        long sum = 0;
        for (int i = 0; i < arr.length; i++) {
            // To check if we encountered with value which itself is zero
            if(arr[i]==0){
                res[0]=i;
                res[1]=i;
                return res;
            }
            // Adding current value in current sum
            sum += arr[i];
            // If we found value sum in our hashmap means we have encountered with this sum before
            // means arr[0, map.get(sum)] = sum and
            // arr[0, map.get(sum)] + arr[map.get(sum)+1, i] = sum
            // which implies arr[map.get(sum)+1, i] = 0 and hence interval we are looking for is
            // start = map.get(sum)+1 and end = i
            if (map.containsKey(sum)) {
                res[0] = map.get(sum) + 1;
                res[1] = i;
                return res;
            } else {
                map.put(sum, i);
            }
        }
        // If no subarray having sum = 0 found then we will return [-1]
        return new int[]{-1};
    }
    // -------------------- END ----------------------
}

class Solution{
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(bufferedReader.readLine());

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(bufferedReader.readLine());
        }

        int[] resSubArray = Result.sumZero(arr);

        for (int i = 0; i < resSubArray.length; i++) {
            bufferedWriter.write(String.valueOf(resSubArray[i])+"\n");
        }
        bufferedWriter.newLine();
        
        bufferedWriter.close();

        bufferedReader.close();
    }

}
/**
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
'''

