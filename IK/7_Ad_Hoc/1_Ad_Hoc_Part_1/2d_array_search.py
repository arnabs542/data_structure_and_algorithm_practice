'''
2D Array Search
Problem Statement:
You are given a sorted 2D array arr of size r * c, where all the numbers (integers) in the array are in non decreasing order
 from left to right and top to bottom. ( i.e. arr[i][j] <= arr[i+1][j] and arr[i][j] <= arr[i][j+1] for all i = 0,1,...,(r
 - 2) and j = 0,1,...,(c - 2) )
Check if a given number x exists in arr or not.
Given an arr, you have to answer q such queries.
Input/Output Format For The Function:
Input Format:
There are two arguments, arr and x, denoting input 2D array and a number to be searched as mentioned in problem statement
 respectively
Output Format:
Return string "present" if x is present in arr, string "not present" otherwise.
Input/Output Format For The Custom Input:
Input Format:
The first line of the input should contain a single integer r, denoting the no. of rows of input array arr. Second line
 should contain a single integer c, denoting the no. of columns of arr.
In the next r lines, each line should contain c space separated numbers. jth number in ith line of these r lines is arr[i][j],
 denoting the number at ith row of the jth column of arr.
Next line should contain q, denoting no of queries to be answered. In next q lines, each line should contain xi, denoting
 x for ith query
If r = 3, c = 4, arr = [[1, 2, 3, 12], [4, 5, 6, 45], [7, 8, 9, 78]], q = 3, x for 1st query = 6, x for 2nd query = 7 and
 x for 3rd query = 23, then input should be:
3
4
1 2 3 12
4 5 6 45
7 8 9 78
3
6
7
23
Output Format:
There will be q lines, ith line of which contains the result for ith query as "present" or "not present"
For input r = 3, c = 4, arr = [[1, 2, 3, 12], [4, 5, 6, 45], [7, 8, 9, 78]], q = 3, x for 1st query = 6, x for 2nd query
 = 7 and x for 3rd query = 23, output will be:
present
present
not present
Constraints:
1 <= r <= 10^3
1 <= c <= 10^3
1 <= q <= 10^4
-10^9 <= arr[i][j] <= 10^9, (i = 0,1,...,(r - 1) and j = 0,1,...,(c - 1))
-10^9
 <= x <= 10^9
Sample Test Cases:
Sample Input 1:
arr = [[1, 2, 3, 12], [4, 5, 6, 45], [7, 8, 9, 78]]
queries = [6, 7, 23]
Sample Output 1:
result = [“present”, “present”, “not present”]
Explanation 1:
Given number x=6 is present at arr[1][2] and x=7 is present at arr[2][0]. Hence, "present" returned for them, while
x=23 is not present in arr, hence "not present" returned
Sample Input 2:
arr = [[3, 4], [5, 10]]
queries = [12, 32]
Sample Output 2:
result = [“not present”, “not present”]
Explanation 2:
Given number x=12 and x=32 are not present in arr. Hence, "not present" returned for both of the queries
'''
import os
import sys


#
# Complete the isPresent function below.
#
def isPresent(arr, x):
    pass



if __name__ == "__main__":
    fptr = sys.stdout
    arr_rows = int(input())
    arr_columns = int(input())
    arr = []
    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))
    q = int(input())
    for _ in range(q):
        x = int(input())
        res = isPresent(arr, x)
        fptr.write(res + '\n')
    fptr.close()

'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
A naive approach would be, to iterate over entire input array arr to check if x is present or not.
Time Complexity:
O(r*c*q) where r denotes number of rows of arr, c denotes number of columns of arr and q denotes number of queries.
As we are iterating over entire array for each query, time complexity will be O(r*c) (for each query) and as there are q
 queries so total time complexity will be O(r*c*q).
Auxiliary Space Used:
O(1).
As we are not storing anything extra.
Space Complexity:
O(r*c) where r denotes number of rows of arr and c denotes number of columns of arr.
To store input, it would take O(r*c), auxiliary space used is O(1).
So, total space complexity will be O(r*c).
2) optimal_solution.java
Description:
An optimal approach would be as follows:
Steps:
1) Start with top right element arr[0][c-1]
2) Loop: compare this element arr[i][j] with x
-> If arr[i][j] == x, then return "present"
-> If arr[i][j] < x then move to next row (i.e. arr[i+1][j])
-> If arr[i][j] > x then move to column to its left (i.e. arr[i][j-1])
3) repeat the steps in #2 till you find element and return "present" OR if out of bound of matrix then break and return
 "not present"
Let say x is not present in first (i-1) rows.
Let's say in ith row, arr[i][j] is largest number smaller than or equal to x.
-> If it is equal to x, then problem solved, directly return “present”.
-> If arr[i][j] < x, it can be implied that x cannot be present at arr[l][m], i < l and j < m as array is row wise and column
 wise sorted (ascending). So, moving on to next row, (i+1)th row, we can start checking from jth column (i.e. arr[i+1][j]).

-> If arr[i][j] > x, means element x can be present in left side of column jth as row and column are sorted in ascending
 order. So, we start checking it with arr[i][j-1].
Time Complexity:
O((r+c)*q) where r denotes number of rows of arr, c denotes number of columns of arr and q denotes number of queries.
As for each query maximum iteration over array can be of O(r+c) and as there can be q queries so, total complexity will
 be O((r+c)*q).
Auxiliary Space Used:
O(1).
As we are not storing anything extra.
Space Complexity:
O(r*c) where r denotes number of rows of arr and c denotes number of columns of arr.
To store input, it would take O(r*c), auxiliary space used is O(1).
So, total space complexity will be O(r*c).
'''
'''
BRUTE FORCE
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * You are given a sorted 2D array arr of size r*c, where all the numbers (integers) in the array are in increasing
 * order from left to right and top to bottom i.e. arr[i][j]<=arr[i+1][j] and arr[i][j]<=arr[i][j+1].
 * Check if a given number x exists in it or not.
 */
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static String isPresent(int[][] arr, int x) {
        int r = arr.length;
        int c = arr[0].length;
        // Iterate over entire input array to check if x is present or not
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (arr[i][j] == x) {
                    return "present";
                }
            }
        }
        return "not present";
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
        int arrRows = Integer.parseInt(bufferedReader.readLine().trim());
        int arrColumns = Integer.parseInt(bufferedReader.readLine().trim());
        
        int[][] arr = new int[arrRows][arrColumns];

        for (int arrRowItr = 0; arrRowItr < arrRows; arrRowItr++) {
            String[] arrRowItems = bufferedReader.readLine().split(" ");

            for (int arrColumnItr = 0; arrColumnItr < arrColumns; arrColumnItr++) {
                int arrItem = Integer.parseInt(arrRowItems[arrColumnItr].trim());
                arr[arrRowItr][arrColumnItr] = arrItem;
            }
        }
        
        int q = Integer.parseInt(bufferedReader.readLine().trim());
        int x;
        String res;
        for (int i=0 ; i<q ; i++){
            x = Integer.parseInt(bufferedReader.readLine().trim());
            res = Result.isPresent(arr, x);
            bufferedWriter.write(res+"\n");
        }
        bufferedReader.close();
        bufferedWriter.close();
    }
}


/**
 * Time complexity: O((r*c)*q)
 * Space complexity: O(1)
 */
'''
'''
OPTIMAL SOLUTION
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * You are given a sorted 2D array arr of size r*c, where all the numbers (integers) in the array are in increasing
 * order from left to right and top to bottom i.e. arr[i][j]<=arr[i+1][j] and arr[i][j]<=arr[i][j+1].
 * Check if a given number x exists in it or not.
 */
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static String isPresent(int arr[][], int x) {
        int r = arr.length;
        int c = arr[0].length;
        int rowIndex = 0;
        int colIndex = c - 1;
        // Starting from 0th row, find first element from right in current row, let say a[l][m], such
        // that a[l][m] <= x.
        while(rowIndex <= (r-1) && colIndex >= 0){
            // arr[rowIndex][colIndex] is the first element from right in current row rowIndex. 
            if (arr[rowIndex][colIndex] == x){
                return "present";
            }
            
            // As arr is sorted row wise and column wise in increasing order, 
            // we can say that x can't be present at arr[l][m], rowIndex<l and colIndex<m
            // Also, in current row rowIndex, x can't be present as arr[rowIndex][colIndex] < x and 
            // all elements to its left are even smaller than arr[rowIndex][colIndex] and 
            // we have already checked all elements to its right. So moving on to next row.
            // Notice that you can start to check at current column j (stored in colIndex) in next row as x can't
            // be present at arr[l][m], l>rowIndex and m>colIndex
            if (arr[rowIndex][colIndex] < x){
                rowIndex++;
            }
            // As arr is sorted row wise and column wise in increasing order, 
            // we can say that if x < arr[rowIndex][colIndex] means x can be present 
            // on left side of colIndex in same row rowIndex.
            else if(arr[rowIndex][colIndex] > x){
                colIndex--;
            }
        }
        return "not present";
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
        int arrRows = Integer.parseInt(bufferedReader.readLine().trim());
        int arrColumns = Integer.parseInt(bufferedReader.readLine().trim());
        
        int[][] arr = new int[arrRows][arrColumns];

        for (int arrRowItr = 0; arrRowItr < arrRows; arrRowItr++) {
            String[] arrRowItems = bufferedReader.readLine().split(" ");

            for (int arrColumnItr = 0; arrColumnItr < arrColumns; arrColumnItr++) {
                int arrItem = Integer.parseInt(arrRowItems[arrColumnItr].trim());
                arr[arrRowItr][arrColumnItr] = arrItem;
            }
        }
        
        int q = Integer.parseInt(bufferedReader.readLine().trim());
        int x;
        String res;
        for (int i=0 ; i<q ; i++){
            x = Integer.parseInt(bufferedReader.readLine().trim());
            res = Result.isPresent(arr, x);
            bufferedWriter.write(res+"\n");
        }
        bufferedReader.close();
        bufferedWriter.close();
    }
}


/**
 * Time complexity: O((r+c)*q)
 * Space complexity: O(1)
 */
'''
