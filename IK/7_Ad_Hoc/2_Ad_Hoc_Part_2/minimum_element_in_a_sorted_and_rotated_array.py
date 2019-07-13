'''
Minimum Element In A Sorted And Rotated Array
Problem Statement:
You are given a sorted array arr which is rotated by unknown pivot k. You need to find minimum element from given array
using fastest possible way which uses only constant space.

Input Format:
Only argument for function, integer array named arr.

Output Format:
Return integer which is minimum element in given array.

Constraints:
1 <= n <= 10^5 where n is number elements in given array.
Every element of array will be unique.

For every element arr[i],
-10^9 <= arr[i] <= 10^9 where 0 <= i <= (n-1)

Sample Test Case:
Sample Input:
arr = [ 4, 5, 6, 7, 8, 1, 2, 3]
Sample Output:
1

Explanation:
For given arr = [ 4, 5, 6, 7, 8, 1, 2, 3] which is sorted in ascending order and right rotated by pivot 5 has minimum value as 1 at index 5.
'''
import math
import os
import random
import re
import sys

#
# Complete the 'find_minimum' function below.
#
# The function accepts INTEGER ARRAY as parameter.
# Return INTEGER.
#
def find_minimum(arr):
    pass


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(int(input().strip()))
    fptr = sys.stdout
    result = find_minimum(arr)
    fptr.write(str(result)+"\n")
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Time Complexity:
O(n) where n is number of elements in array.
This approach is very simple, We just need to iterate over the given array and maintain the minimum value found and return
 that minimum value which will be our answer.
 
Auxiliary Space Used:
O(1).
As we are not storing anything.

Space Complexity:
O(n).

Input is O(n) because we are storing n elements of array and auxiliary space used is O(1). So, O(n) + O(1) -> O(n).




2) suboptimal_solution.java
Time Complexity:
Time complexity for the function find_minimum: O(log n) where n is number of elements in array.
Time complexity for the complete program: O(n) where n is number of elements in array, because size of input is n.
In this approach we used recursive binary search.
If we take some examples and look closely, we would observe some patterns:
If array was previously sorted in ascending order:
    The minimum element is the only element whose previous element is greater than it.
    If we found any subarray ( from low to high ) which is ascending sorted then minimum element will be element at low.
    Else minimum element lies in either left half or right half.
    If middle element is greater than element at low, then the minimum element lies in right half.
    Else minimum element lies in left half.
If array was previously sorted in descending order:
We use these patterns to make solution:
    The minimum element is the only element whose next element is greater than it.
    If we found any subarray ( from low to high) which is descending sorted then minimum element will be element at high.
    Else minimum element lies in either left half or right half.
    If middle element is less than element at low, then the minimum element lies in right half.
    Else minimum element lies in left half.
As the time complexity of binary search will be
T(n) = T(n/2) + c ( Each iteration reducing array in half ).
The above function can be solved either using recurrence Tree method or Master method. It falls in case II of Master Method
 and solution of the function is O(log n) hence, complexity of our solution (find_minimum function) is O(log n).
Auxiliary Space Used:
O(log n) where n is number of elements in array.
Similarly by above logic for time complexity, number of recursive calls will be O(log n) and hence size of function stack
 used will be O(log n).
Space Complexity:
O(n) where n is number of elements in array.
Input is O(n) because we are storing n elements of array and auxiliary space used is O(1). So, O(n) + O(1) -> O(n).
3) optimal_solution.java
Time Complexity:
Time complexity for the function find_minimum: O(log n) where n is number of elements in array.
Time complexity for the complete program: O(n) where n is number of elements in array, because size of input is n.
Here we are using iterative approach of binary search. Explanation will same as mentioned above for suboptimal_solution.

Auxiliary Space Used:
O(1).
As we are using only constant extra space.
Space Complexity:
O(n) where n is number of elements in array.
Input is O(n) because we are storing n elements of array and auxiliary space used is O(1). So, O(n) + O(1) -> O(n).
'''
'''
BRUTE FORCE
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


class Result {

    /*
    * Complete the 'find_minimum' function below.
    *
    * The function accepts INTEGER ARRAY as parameter.
    * Return INTEGER.
    */
    // ============================ Start ============================
    public static int find_minimum(List<Integer> arr) {
        int minimum = Integer.MAX_VALUE;
        // Iterating over all the values of arr to find minimum value
        for(int num: arr){
            minimum = Math.min(minimum, num);
        }
        return minimum;
    }
    // ============================= End ==============================
}


class Solution {
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

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        List<Integer> arr = new ArrayList<Integer>();
        
        for(int i=0;i<n;i++){
            arr.add(Integer.parseInt(bufferedReader.readLine().trim()));
        }
        
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        int result = Result.find_minimum(arr);
        bufferedWriter.write(result+"\n");
        bufferedWriter.close();
    }
}
'''
'''
SUBOPTIMAL SOLUTION
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


class Result {

    /*
    * Complete the 'find_minimum' function below.
    *
    * The function accepts INTEGER ARRAY as parameter.
    * Return INTEGER.
    */
    // ============================ Start ============================
    public static int find_minimum(List<Integer> arr) {
        int n = arr.size();
        if(n==1) {
            return arr.get(0);
        }
        if(n==2) {
            return Math.min(arr.get(0), arr.get(1));
        }
        if(n==3) {
            return Math.min(arr.get(0), Math.min(arr.get(1), arr.get(2)));
        }
        /*
         * All numbers of array are unique as given in question so don't consider the cases when 
         * numbers are equal and get confuse.
         */
        /*
         * consider example [4, 7, 8, 10, 15].
         * for this given array was [4, 7, 8, 10, 15] which was sorted in ascending order
         * and rotated right by 0
         */
        if(arr.get(0)-arr.get(n-1)<0&&arr.get(0)-arr.get(1)<0&&arr.get(n-2)-arr.get(n-1)<0) {
            return arr.get(0);
        }
        /*
         * consider example [15, 10, 8, 7, 4].
         * for this given array was [15, 10, 8, 7, 4] which was sorted in ascending order
         * and rotated right by 0
         */
        if(arr.get(0)-arr.get(n-1)>0&&arr.get(0)-arr.get(1)>0&&arr.get(n-2)-arr.get(n-1)>0) {
            return arr.get(n-1);
        }
        if(arr.get(0)-arr.get(n-1) > 0) {
            /*
             * consider example [10, 13, 15, 4, 6, 8].
             * for this given array was [4, 6, 8, 10, 13, 15] which was sorted in ascending order
             * and rotated right by 3
             */
            return find_minimum_in_increasing(arr, 0, n-1);
        }
        else {
            /*
             * consider example [8, 6, 4, 15, 13, 10].
             * for this given array was [15, 13, 10, 8, 6, 4] which was sorted in descending order
             * and rotated right by 3
             */
            return find_minimum_in_decreasing(arr, 0, n-1);
            
        }
    }
    public static int find_minimum_in_increasing(List<Integer> arr, int low, int high) {
        if(low>high){
            return -1;
        }
        if(arr.get(low)-arr.get(high)<=0){
            return arr.get(low);
        }
        int mid = (low+high)/2;
        if(arr.get(mid)-arr.get(low)>=0){
            return find_minimum_in_increasing(arr, mid+1, high);
        }
        return find_minimum_in_increasing(arr, low, mid);
    }
    public static int find_minimum_in_decreasing(List<Integer> arr, int low, int high) {
        if(low>high){
            return -1;
        }
        if(arr.get(low)-arr.get(high)>=0) {
            return arr.get(high);
        }
        int mid = (low+high)/2;
        if(arr.get(mid)-arr.get(low)<0){
            return find_minimum_in_decreasing(arr, mid, high);
        }
        return find_minimum_in_decreasing(arr, low, mid);
    }
    // ============================= End ==============================
}


class Solution {
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

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        List<Integer> arr = new ArrayList<Integer>();
        
        for(int i=0;i<n;i++){
            arr.add(Integer.parseInt(bufferedReader.readLine().trim()));
        }
        
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        int result = Result.find_minimum(arr);
        bufferedWriter.write(result+"\n");
        bufferedWriter.close();
    }
}
'''
'''
OPTIMAL SOLUTION

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;


class Result {

    /*
    * Complete the 'find_minimum' function below.
    *
    * The function accepts INTEGER ARRAY as parameter.
    * Return INTEGER.
    */
    // ============================ Start ============================
    public static int find_minimum(List<Integer> arr) {
        int n = arr.size();
        if(n==1) {
            return arr.get(0);
        }
        if(n==2) {
            return Math.min(arr.get(0), arr.get(1));
        }
        if(n==3) {
            return Math.min(arr.get(0), Math.min(arr.get(1), arr.get(2)));
        }
        /*
         * All numbers of array are unique as given in question so don't consider the cases when 
         * numbers are equal and get confuse.
         */
        /*
         * consider example [4, 7, 8, 10, 15].
         * for this given array was [4, 7, 8, 10, 15] which was sorted in ascending order
         * and rotated right by 0
         */
        if(arr.get(0)-arr.get(n-1)<0&&arr.get(0)-arr.get(1)<0&&arr.get(n-2)-arr.get(n-1)<0) {
            return arr.get(0);
        }
        /*
         * consider example [15, 10, 8, 7, 4].
         * for this given array was [15, 10, 8, 7, 4] which was sorted in ascending order
         * and rotated right by 0
         */
        if(arr.get(0)-arr.get(n-1)>0&&arr.get(0)-arr.get(1)>0&&arr.get(n-2)-arr.get(n-1)>0) {
            return arr.get(n-1);
        }
        if(arr.get(0)-arr.get(n-1) > 0) {
            /*
             * consider example [10, 13, 15, 4, 6, 8].
             * for this given array was [4, 6, 8, 10, 13, 15] which was sorted in ascending order
             * and rotated right by 3
             */
            return find_minimum_in_increasing(arr);
        }
        else {
            /*
             * consider example [8, 6, 4, 15, 13, 10].
             * for this given array was [15, 13, 10, 8, 6, 4] which was sorted in descending order
             * and rotated right by 3
             */
            return find_minimum_in_decreasing(arr);
            
        }
    }
    public static int find_minimum_in_increasing(List<Integer> arr) {
        int low = 0;
        int high = arr.size()-1;
        while(low<=high) {
            if(arr.get(low)-arr.get(high)<=0) {
                return arr.get(low);
            }
            int mid = (low+high)/2;
            if(arr.get(mid)-arr.get(low)>=0) {
                //Minimum is in right subarray
                low = mid + 1;
            }else {
                //Minimum is in left subarray 
                high = mid;
            }
        }
        return -1;
    }
    public static int find_minimum_in_decreasing(List<Integer> arr) {
        int low = 0;
        int high = arr.size()-1;
        while(low<=high) {
            if(arr.get(low)-arr.get(high)>=0) {
                return arr.get(high);
            }
            int mid = (low + high)/2;
            if(arr.get(mid)-arr.get(low)<0) {
                //Minimum is in right subarray
                low = mid;
            }else {
                //Minimum is in left subarray
                high = mid;
            }
        }
        return -1;
    }
    // ============================= End ==============================
}


class Solution {
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

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        List<Integer> arr = new ArrayList<Integer>();
        
        for(int i=0;i<n;i++){
            arr.add(Integer.parseInt(bufferedReader.readLine().trim()));
        }
        
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        int result = Result.find_minimum(arr);
        bufferedWriter.write(result+"\n");
        bufferedWriter.close();
    }
}
'''
