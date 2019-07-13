'''
Pascal's Triangle
Problem Statement:
Pascal’s triangle is a triangular array of the binomial coefficients. Write a function that takes an integer value n as

input and returns 2d Array representing pascal’s triangle.
pascalTriangleArray is a 2D array of size n*n, where
pascalTriangleArray[i][j] = BinomialCoefficient(i, j); if j<=i,
pascalTriangleArray[i][j] = 0; if j>i
Following are the first 6 rows of Pascal’s Triangle:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
Input/Output Format For The Function:
Input Format:
There is only one argument n, denoting the number of lines of Pascal's triangle to be considered.
Output Format:
Return an 2d integer array result, denoting pascal’s triangle where each value of result 2d array must be modulo with (10^9
 + 7).
Size of result[i] for 0 <= i < n should be (i + 1) i.e. 0s for pascalTriangleArray[i][j] = 0; if j>i, should be ignored.

Input/Output Format For The Custom Input:
Input Format:
There should be one line for input, containing a single integer n, denoting the number of lines of Pascal's triangle to
 be considered.
If n = 6, then input should be:
6
Output Format:
There will be 2d array of integers, where each row of result 2d array will denotes row of pascal’s triangle in same order.

For input n = 6, output will be:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
Constraints:
1 <= n <= 1700
Sample Test Cases:
Sample Input 1:
4
Sample Output 1:
1
1 1
1 2 1
1 3 3 1
Explanation 1:
Pascal's Triangle for given n=4:
Using equation,
pascalTriangleArray[i][j] = BinomialCoefficient(i, j); if j<=i,
pascalTriangleArray[i][j] = 0; if j>i
Generated pascal’s triangle will be:
1
1 1
1 2 1
1 3 3 1
Sample Input 2:
6
Sample Output 2:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
Explanation 2:
Pascal's Triangle for given n=6:
Using equation,
pascalTriangleArray[i][j] = BinomialCoefficient(i, j); if j<=i,
pascalTriangleArray[i][j] = 0; if j>i
Generated pascal’s triangle will be:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
'''
import math
import os
import random
import re
import sys

#
# Complete the 'findPascalTriangle' function below.
#
# The function accepts INTEGER as parameter.
# Return 2D INTEGER ARRAY.
#
def findPascalTriangle(n):
    pass


if __name__ == '__main__':
    n = int(input().strip())
    fptr = sys.stdout
    result = findPascalTriangle(n)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
A naive approach would be to calculate each (binomial coefficient % mod) separately. Binomial coefficient nCr = n!/((n-r)!
 * r!). So, calculate numerator = (n! % mod) , denominator = (((n-r)! * r!) % mod). Finally nCr can be found as ((numerator
 * moduloInverse(denominator)) % mod).
Time Complexity:
O(n^3) where n is given number.
As there are n rows and each row can have n element in worst  cases. For calculating nCr for each element it will take O(n).
 Hence for n*n elements it will take O(n^3).
Auxiliary Space Used:
O(1).
As we are not storing anything extra. (Here we are ignoring space used to store output 2d array result which will be O(n*n))

Space Complexity:
O(n * n).
As input is O(1), auxiliary space used is O(1) and output space is O(n * n).
2) optimal_solution.java
Description:
An optimal approach would be as follows:
As we know that for pascals triangle pascalsTriangle[i][j] = pascalsTriangle[i-1][j] + pascalsTriangle[i-1][j-1] and pascalsTrianlge[i][0]
 = 1 and pascalsTriangle[i][i]=1. For 0<=i<n and 0<=j<=i.
We use these facts and iterate each row and find out the pascalsTriangle.
Time Complexity:
O(n^2) where n is given number.
As there are n rows and each row can have n element in worst  cases so, to iterate over n*n elements it will take O(n^2).

Auxiliary Space Used:
O(1).
As we are not storing anything extra. (Here we are ignoring space used to store output 2d array result which will be O(n*n))

Space Complexity:
O(n * n).
As input is O(1), auxiliary space used is O(1) and output space is O(n * n).
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
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    // -------------------- START ----------------------
    /*
    * Complete the 'findPascalTriangle' function below.
    *
    * The function accepts INTEGER as parameter.
    * Return 2D INTEGER ARRAY.
    */
    static List<List<Integer>> findPascalTriangle(int n) {
        long res = 0;
        int mod = 1000000007;
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            ArrayList<Integer> row = new ArrayList<Integer>();
            for (int j = 0; j <= i; j++) {
                // nCr(i,j) is nothing but jth value in ith line of Pascal's Triangle (0-based indexing)
                row.add((int)(nCr(i, j, mod)%mod));
            }
            result.add(row);
        }
        return result;
    }

    private static long nCr(int n, int r, int mod) {
        long num = 1;
        long den = 1;
        for (long i = 1; i <= n; i++) {
            num *= i;
            num %= mod;
        }

        for (long i = 1; i <= (n - r); i++) {
            den *= i;
            den %= mod;
        }

        for (long i = 1; i <= r; i++) {
            den *= i;
            den %= mod;
        }

        long nCr = (num * modInverse((int) den, mod)) % mod;
        return nCr;
    }

    // Works only for prime value of modulo
    static long modInverse(int a, int mod) {
        return modPower(a, mod - 2, mod);
    }

    // To compute x^y under modulo m
    static long modPower(int x, int y, int m) {
        if (y == 0)
            return 1;

        long p = modPower(x, y / 2, m) % m;
        p = (p * p) % m;

        if (y % 2 == 0)
            return p;
        else
            return (p * x) % m;
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

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        List<List<Integer>> result = Result.findPascalTriangle(n);

        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            });

        bufferedWriter.close();
        bufferedReader.close();
    }

}
/**
 * Time complexity: O(n^3)
 * Space complexity: O(n^2)
 */
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
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    // -------------------- START ----------------------
    /*
    * Complete the 'findPascalTriangle' function below.
    *
    * The function accepts INTEGER as parameter.
    * Return 2D INTEGER ARRAY.
    */
    static List<List<Integer>> findPascalTriangle(int n) {
        int mod = 1000000007;
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < n; i++){ 
            // Every ith row has number of integers  
            // equal to row number
            ArrayList<Integer> row = new ArrayList<Integer>();
            for (int j = 0; j <= i; j++){
                // First and last values in every row are 1 
                if (i == j || j == 0){ 
                    row.add(1); 
                }
                // Other values are sum of values just  
                // above and left of above 
                else{
                    row.add((result.get(i-1).get(j-1) + result.get(i-1).get(j))%mod); 
                }
            }
            result.add(row);
        }
        return result;
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

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        List<List<Integer>> result = Result.findPascalTriangle(n);

        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            });

        bufferedWriter.close();
        bufferedReader.close();
    }

}
/**
 * Time complexity: O(n^2)
 * Space complexity: O(n^2)
 */
'''

