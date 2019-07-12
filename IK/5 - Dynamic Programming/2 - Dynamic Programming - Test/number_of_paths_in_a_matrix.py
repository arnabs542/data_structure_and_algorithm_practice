'''
Number Of Paths In A Matrix
Problem Statement:
Consider a maze mapped to a matrix with an upper left corner at coordinates (row, column) = (0, 0). You can only move either
 towards right or down from a cell. You must determine the number of distinct paths through the maze. You will always start
 at a position (0, 0), the top left, and end up at (n-1, m-1), the bottom right.
As an example, consider the following diagram where '1' indicates an open cell and '0' indicates blocked. You can only travel
 through open cells, so no path can go through the cell at (0, 2). There are two distinct paths to the goal.

 https://i.imgur.com/1uOgaIO.png

There are two possible paths from the cell (0, 0) to cell (1, 3) in this matrix.
Complete the function numberOfPaths. The function must return the number of paths through the matrix, modulo (10^9 + 7).

Input/Output Format For The Function:
Input Format:
The function contains a single argument, a 2d integer array matrix.
Output Format:
Return an integer, the number of paths to reach from (0, 0) to (n-1, m-1).
Input/Output Format For The Custom Input:
Input Format:
The first line contains integer n, the number of rows. The next line contains integer m, number of columns. Next n lines
 contain m integers each.
For example:
3
3
1 1 0
1 1 1
0 1 1
Output Format:
Output the number of paths in a single line.
For the above input, the output would be
4
Constraints:
1 <= n*m <= 2*10^6
Each cell, matrix[i][j], contains 1, indicating it is accessible or 0, indicating it is not accessible,
 where 0<=i<n and 0<=j<m.
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
3
4
1 1 1 1
1 1 1 1
1 1 1 1
Sample Output 1:
10
Explanation 1:
There are 10 possible paths from cell (0, 0) to cell (2, 3).﻿﻿

https://i.imgur.com/YxeHc1n.png


Sample Test Case 2:
Sample Input 2:
2
2
1 1
0 1
Sample Output 2:
1

Explanation 2:
https://i.imgur.com/b4JfKBX.png

There is 1 possible path from the cell (0, 0) to cell (1, 1).
'''
import math
import os
import random
import re
import sys


#
#Complete the fumction numberOfPaths
#The fumction takes integers 2D integer array, matrix, as parameter.
#
def numberOfPaths(matrix):
    pass



if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    m = int(input().strip())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
    result = numberOfPaths(matrix)
    fptr.write(str(result) + '\n')
    fptr.close()


'''
We have provided 2 solutions and the solutions contains necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
We have a matrix having n rows and m columns where each cell, matrix[A][B], denotes whether it is accessible or not.
We
 will use recursion to solve this problem.
We know that the number of ways to reach a cell is the sum of the number of ways
 to reach cell just to the left of it and the number of ways to reach cell just above it, that is for cell matrix[i][j],
 the number of ways to reach that cell is the number of ways to reach cell matrix[i-1][j] + number of ways to reach cell
 matrix[i][j-1].
This is because we can only go in the right or downward direction from any cell.
Now, we start from cell
 and perform recursion that is number of ways to reach cell (n-1, m-1) which is recur(matrix, n-1, m-1) = recur(matrix,
 n-2, m-1) + recur(matrix, n-1, m-2).
For each cell we will check if it is accessible or not. If it is not we simply return
 0, as there is no way to reach it.
The base condition would be that for cell (0,0), that is the starting cell, if it is
 accessible then the number of ways to reach it is 1.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(2^(n*m)) considering the number of rows are n and columns are m.
We start recursion from the end cell. We keep on recurring until we reach either the stopping condition or the base condition.
 There are total n*m possibilities and so in the worst case, the time complexity turns out to be O(2^(n*m)).
Time Complexity:
O(2^(n*m)) considering the number of rows are n and columns are m.
As time complexity assuming that input arguments are already given and excluding time used in declaration of output is O(2^(n*m)),
 to read input it will take O(n^2) and to store output it will take O(1) hence total complexity will be O(2^(n*m)) + O(n^2)
 + O(1) → O(2^(n*m)).
Auxiliary Space Used:
O(n+m) considering the number of rows are n and columns are m.
We do not create any auxiliary array for the solution. We use recursion which uses O(n+m) stack space as the maximum steps
 can be n+m at a time. So overall auxiliary space used is O(n+m).
Space Complexity:
O(n*m) considering the number of rows are n and columns are m.
Input complexity is O(n*m), auxiliary space used is O(n+m), and output space complexity is O(1), hence total complexity
 will be O(n*m).
2) optimal_solution.java

Description:
* We have a matrix having n rows and m columns where each cell, matrix[A][B], denotes whether it is accessible or not.
* As we can see from the above recursive solutions (brute_force_solution) is exponential. We are visiting multiple states again
 and again and then recursing for them, which we can surely avoid.
* With the same idea of avoiding recursion again and again for states that have already been visited, we store them in 
a dp array so that they can be accessed as and when needed.
* This approach is known as Dynamic Programming which we will use to solve this problem.
* We know that, for any cell (i, j) the number of paths to reach it would be number of paths to reach 
cell(i-1, j) + number of paths to reach cell (i, j-1).
* This means, for any accessible cell matrix[i][j], we maintain the count of number of paths to reach this cell in a separate
 2D array dp[i][j], where dp[i][j] = dp[i-1][j] + dp[i][j-1], given that cell (i, j) is accessible.
* We return the value of dp[i][j] as the answer.


Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*m) considering the number of rows are n and columns are m.
We traverse the entire array matrix once and simultaneously traverse the dp array to keep the count of number of ways to
 reach that cell from cell (0,0). So we travel both the arrays at most 1 time and hence the time complexity is O(n*m).
Time Complexity:
O(n*m) considering the number of rows are n and columns are m.
As time complexity assuming that input arguments are already given and excluding time used in declaration of output is O(n*m),
 to read input it will take O(n*m) and to store output it will take O(1) hence total complexity will be O(n*m) + O(n*m)
 + O(1) → O(n*m).
Auxiliary Space Used:
O(n*m) considering the number of rows are n and columns are m.
We create a 2D array dp of size n*m to store the count of number of paths from cell (0,0) to the current cell. Hence, auxiliary
 space used is O(n*m).
Space Complexity:
O(n*m) considering the number of rows are n and columns are m.
Input complexity is O(n*m), auxiliary space used is O(n*m), and output space complexity is O(1), hence total complexity
 will be O(n*m).
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
    /*============================== START =========================================*/
    public static int numberOfPaths(List<List<Integer>> matrix){
        int n = matrix.size(), m = matrix.get(0).size(), MOD = 1000000007;
        int ans = recur(matrix, n-1, m-1, MOD);
        return ans;
    }
    
    public static int recur(List<List<Integer>> matrix, int n, int m, int MOD) {
        int ans = 0;
        //stopping condition
        if(n<0 || m<0) {
            return 0;
        }
        //if a cell is restricted, there are 0 ways to reach there.
        if(matrix.get(n).get(m)==0) {
            return 0;
        }
        //base condition: if cell (0,0) is accessible, we have 1 way to reach it.
        if(n==0 && m==0) {
            return 1;
        }
        /*number of ways to reach cell 
        a[i][j] = number of ways to reach cell a[i-1][j] + number of ways to reach cell a[i][j-1]*/
        ans += (recur(matrix, n-1, m, MOD) + recur(matrix, n, m-1, MOD))%MOD;
        return ans;
    }
    /*============================== END =========================================*/
    
}

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        int m = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> matrix = new ArrayList<>();

        IntStream.range(0, n).forEach(i -> {
            try {
                matrix.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.numberOfPaths(matrix);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        bufferedReader.close();
    }
}
'''
'''
OPTMIAL SOLUTION
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
    /*============================== START =========================================*/
    public static int numberOfPaths(List<List<Integer>> matrix){
        int n = matrix.size(), m = matrix.get(0).size(), MOD = 1000000007;
        if(matrix.get(0).get(0)== 0 || matrix.get(n-1).get(m-1)==0) {
            return 0;
        }
        int[][] dp = new int[n][m];
        //if cell (0,0) is accessible, number of ways to reach it is 1
        dp[0][0] = 1;
        //filling for the cells in first row.
        for(int i = 1; i < m ;i++){
            if(matrix.get(0).get(i)==1 && dp[0][i-1] == 1){
                dp[0][i] = 1;
            }
        }
        //filling for the cells in the first column
        for(int i = 1; i < n ;i++){
            if(matrix.get(i).get(0)==1 && dp[i-1][0] == 1){
                dp[i][0] = 1;
            }
        }
        /*number of ways to reach 
        cell(i,j) = number of ways to reach cell(i-1,j) + number of ways to reach cell (i,j-1)*/
        for(int i = 1; i < n; i++){
            for(int j = 1; j<m; j++){
                if(matrix.get(i).get(j)==1){
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1])%MOD;
                }
            }
        }
        return dp[n-1][m-1];
    }
    /*============================== END =========================================*/
}

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        int m = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> matrix = new ArrayList<>();

        IntStream.range(0, n).forEach(i -> {
            try {
                matrix.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.numberOfPaths(matrix);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        bufferedReader.close();
    }
}
'''
