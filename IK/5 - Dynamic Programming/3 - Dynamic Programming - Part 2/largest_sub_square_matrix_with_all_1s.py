'''
Largest sub-square matrix with all 1s
Problem Statement:
Given a 2D matrix mat of integers with n rows and m columns. All the elements in the matrix mat are either 0 or 1. Your
 task is to determine the largest sub-square size of the matrix that contains only 1s.
Input/Output Format For The Function:
Input Format:
There are three arguments, n, m, mat denoting the number of rows of matrix, number of columns of matrix and 2D matrix respectively.

Output Format:
Return an integer denoting the largest size of sub-square matrix that contains only 1s in the input 2D matrix mat.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain a single number n, denoting the number of rows of input matrix mat. Second line should
 contain a single integer m, denoting the number of columns of input matrix mat. In the next n lines, each line should contain
 m space separated numbers. jth number in ith line of these n lines is mat[i][j], denoting the number at ith row and jth
 column of matrix.
If n=3, m=3 and mat=[ [1,0,0], [0,1,1], [0,1,1]], then input should be:
3
3
1 0 0
0 1 1
0 1 1
Output Format:
There should be a single number representing result.
If n=3, m=3 and mat=[ [1,0,0], [0,1,1], [0,1,1]], then output should be:
2
Constraints:
1 <= n, m <= 1000
mat[i][j] can be 0 or 1 where 0<=i<n and 0<=j<m.
Sample Test Case:
Sample Input:
n = 3
m = 3
mat = [ [1,0,0] , [0,1,1] , [0,1,1] ]
Sample Output:
2
Explanation:
The given matrix is represented below:
1 0 0
0 1 1
0 1 1
Here, we can easily infer that the 1s in bold form a sub-square matrix and is of the largest size(2*2) in the matrix such
 that all the elements in the sub-matrix are 1. Hence, the answer is 2.
'''
import math
import os
import random
import re
import sys



#
# Complete the 'largest_sub_square_matrix' function below.
#
# @param n: number of rows in mat
# @param m: number of columns in mat
# @param mat: 2D matrix of zeros and ones
#
def largest_sub_square_matrix(n, m, mat):
    pass


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    mat = []
    for _ in range(n):
        mat.append(
            list(map(int, input().rstrip().split())))
    fptr = sys.stdout
    result = largest_sub_square_matrix(n, m, mat)
    fptr.write(str(result) + "\n")
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution:
Description:
In this approach we assume every cell in the matrix as the top-left. We iterate over matrix and try to see what is the maximum
 size of sub-square matrix we can obtain satisfying that all elements in the sub-square matrix are 1.
Time Complexity:
O( (n*m)^2) where n is number of rows of matrix and m is number of columns of matrix.
To visit each cell and choose it as top-left cell of the sub-square matrix take O(n*m) time. Now to calculate the maximum
 size of sub-square matrix we start looking if it is feasible for a size 1 matrix, then for size 2 and so on. Next is to
 check if the corresponding size is possible or not. Since it feasible to have a sub-square matrix of all 1s for (size-1).
 So, for sub-matrix of size, it can done by two linear traversal one row wise and another column wise for the last row and
 last column of the sub-matrix.
The time complexity for this step is O(min(m,n)) * (2*O(min(m,n)) → O(n*m). Therefore, the total time complexity becomes
 O(n*m)*O(n*m) → O((m*n)^2).
Auxiliary Space Used:
O(1).
Since we are only traversing on the original matrix without storing anything extra.
Space Complexity:
O(n*m) where n is number of rows of matrix and m is number of columns of matrix.
For storing input it will take space of O(n*m) and auxiliary space used is O(1).
So, O(n*m) + O(1) → O(n*m).
2) other_solution:
Description:
In this solution, we approach the problem dynamically.
Let’s first decide a state for our DP solution. Here we choose state(i, j), which will tell us the maximum size of sub-square
 matrix with all 1s considering the cell (i, j) as the bottom-right most cell of the sub matrix. Now, we see that for a
 state(i, j), its value can be computed using the below state relation:
state(i, j) = min(state(i, j-1) ,state(i-1, j) ,state(i-1, j-1)) + 1 if mat[i][j] = 1
state(i, j) = 0 otherwise.
Now we, just add memorization to the above states, So that we do not calculate same state more than once. As discussed till
 now, our DP state will look something like dp[n][m]. But here is one catch, If you observe carefully then to calculate
 a particular state we only look to its neighbouring 3 states. So, there is no requirement cache all the state. Will simply
 cache the corresponding 3 states and it solves our problem. As, described in the above state relation, two lookup states
 belong to the row just above the current state and one state lies in the same row and just in the previous column of the
 current state. Hence, we will now only maintain a linear memorization table that caches the state solutions of the previous
 row. The same memorization table is updated every time we calculate a state so that it can be used for the states that
 belong to the next row. Kindly, refer to the solution for better understanding.
Time Complexity:
O(n*m) where n is number of rows of matrix and m is number of columns of matrix.
As there are a total of m*n states and each state is being calculated only once and to calculate each state me make three
 lookups. Hence, the time complexity of the dp solution is (number of states) * (number of state lookups) → O(n*m) * 3 →
 O(m*n).
Auxiliary Space Used:
O(m) where m is number of columns of matrix.
As we are storing dp array of size equal to column of matrix while iterating over matrix.
Space Complexity:
O(n*m) where n is number of rows of matrix and m is number of columns of matrix.
To store input matrix, it will take O(n*m), the size of the given matrix mat and auxiliary space used id O(m).
So, O(n*m) + O(m) → O(n*m).
3) optimal_solution:
Description:
The approach in this solution is same as the other_solution that uses the same dynamic programming state relation. Here,
 instead of taking an auxiliary memory we use the provided input matrix to store the DP state and once when all the DP states
 are computed and we have our answer.
Time Complexity:
O(n*m)
Same as other_solution O(n*m) as the algorithm remains the same.
Auxiliary Space Used:
O(1).
Since we are using the original input matrix to store DP states.
Space Complexity:
O(n*m) where n is number of rows of matrix and m is number of columns of matrix.
For storing input it will take space of O(n*m) and auxiliary space used is O(1).
So, O(n*m) + O(1) → O(n*m).
'''
'''
BRUTE FORCE SOLUTION
#include <bits/stdc++.h>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

// -------------------------- START --------------------------
// @param n: integer n, denoting number of rows of matrix
// @param m: integer m, denoting number of columns of matrix
// @param mat: denoting 2D integer array (matrix) of size n*m
int largest_sub_square_matrix(int n, int m, vector<vector<int>> &mat)
{   
    // stores max size of sub square matrix
    int maxi = 0;

    // iterating on all cells of mat 
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            if(!mat[i][j])
                continue;
            // Assuming mat[i][j] as top left corner
            // and checking for all sizes of sub-squre matrix
            int flag = 1;
            for(int sz = 0;(i+sz) < n && (j+sz) < m; sz++) {
                if(!flag)
                    break;
                for(int col = j;col <= (j+sz);col++) {
                    if(!mat[i+sz][col]) {
                        flag = 0;
                        break;
                    }
                }
                for(int row = i;flag && row <= (i+sz); row++) {
                    if(!mat[row][j+sz]) {
                        flag = 0;
                        break;
                    }
                }
                // updating maximum size encountered so far
                if(flag)
                    maxi = max(maxi,sz+1);
            }
        }
    }
    return maxi;
}
// -------------------------- STOP --------------------------

int main()
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output1.txt", "w",
    //     stdout);
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output.txt", "w",
    //     stdout);
    // string testcases;
    // getline(cin,testcases);
    // int t = stoi(testcases);
    // while(t--) {
    string mat_rows_temp;
    getline(cin, mat_rows_temp);
    int n = stoi(ltrim(rtrim(mat_rows_temp)));

    string mat_columns_temp;
    getline(cin, mat_columns_temp);

    int m = stoi(ltrim(rtrim(mat_columns_temp)));

    vector < vector < int > > mat(n);

    for (int i = 0; i < n; i++)
    {
        mat[i].resize(m);
        string mat_row_temp_temp;
        getline(cin, mat_row_temp_temp);
        vector<string> mat_row_temp = split(rtrim(mat_row_temp_temp));
        for (int j = 0; j < m; j++)
        {
            int mat_row_item = stoi(mat_row_temp[j]);
            mat[i][j] = mat_row_item;
        }
    }
    int ans = largest_sub_square_matrix(n, m, mat);
    cout << ans << endl;
    // }
    return 0;
}

string ltrim(const string &str)
{
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str)
{
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}

vector<string> split(const string &str)
{
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos)
    {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
'''
'''
OPTMIAL SOLUTION
#include <bits/stdc++.h>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

// -------------------------- START --------------------------
// @param n: integer n, denoting number of rows of matrix
// @param m: integer m, denoting number of columns of matrix
// @param mat: denoting 2D integer array (matrix) of size n*m
int largest_sub_square_matrix(int n, int m, vector<vector<int>> &mat)
{   
    // stores the size of largest square sub matrix
    int maxi = 0;

    // initializing max sub square size "maxi"
    // by checking first row and first column of mat
    for (int i = 0; i < n; i++)
        maxi |= mat[i][0];
    for (int j = 0; j < m; j++)
        maxi |= mat[0][j];

    // populating dp
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (mat[i][j] == 1) {
                // getting minimum from the below states
                // state (i-1, j-1) 
                // state (i, j-1) 
                // state (i-1, j)
                int value = min(mat[i - 1][j - 1],min(mat[i - 1][j], mat[i][j - 1])) + 1;
                // using current matrix state as dp state
                mat[i][j] = value;
                // updating maximum size encountered so far
                maxi = max(mat[i][j], maxi);
            }
        }
    }

    return maxi;
}
// -------------------------- STOP --------------------------

int main()
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output.txt", "w",
    //     stdout);
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output.txt", "w",
    //     stdout);
    // string testcases;
    // getline(cin,testcases);
    // int t = stoi(testcases);
    // while(t--) {
    string mat_rows_temp;
   getline(cin, mat_rows_temp);
    int n = stoi(ltrim(rtrim(mat_rows_temp)));

    string mat_columns_temp;
   getline(cin, mat_columns_temp);

    int m = stoi(ltrim(rtrim(mat_columns_temp)));

    vector<vector<int>> mat(n);

    for (int i = 0; i < n; i++)
    {
        mat[i].resize(m);
        string mat_row_temp_temp;
       getline(cin, mat_row_temp_temp);
        vector<string> mat_row_temp = split(rtrim(mat_row_temp_temp));
        for (int j = 0; j < m; j++)
        {
            int mat_row_item = stoi(mat_row_temp[j]);
            mat[i][j] = mat_row_item;
            assert(mat[i][j] <= 1000000000);
        }
    }
    int ans = largest_sub_square_matrix(n, m, mat);
    cout << ans << endl;
    // }
    return 0;
}

string ltrim(const string &str)
{
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str)
{
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}

vector<string> split(const string &str)
{
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos)
    {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
'''
'''
OTHER SOLUTION
#include <bits/stdc++.h>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

// -------------------------- START --------------------------
// @param n: integer n, denoting number of rows of matrix
// @param m: integer m, denoting number of columns of matrix
// @param mat: denoting 2D integer array (matrix) of size n*m
int largest_sub_square_matrix(int n, int m, vector<vector<int>> &mat)
{   
    // memoization vector
    vector<int> dp;
    // initializing maximum size of sub square matrix
    int maxi = 0;
    // initializing dp array with first row of matrix mat
    for (int i = 0; i < m; i++) {
        dp.push_back(mat[0][i]);
        maxi = max(maxi, dp[i]);
    }
    int prev = 0;
    int diagonal = 0;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // caching calculated answer for state (i-1, j)
            int tmp = dp[j];

            // if current cell can be a bottom corner
            if (mat[i][j]) {
                if(j != 0)
                    prev = dp[j-1];
                else
                    prev = 0;
                // getting minimum from the below states
                // state (i-1, j-1) ~ diagonal
                // state (i, j-1) ~ prev
                // state (i-1, j) ~ tmp 
                dp[j] = min(min(prev, tmp),diagonal) + 1;
            }
            else {
                dp[j] = 0;
            }
            // caching (i,j-1) ~ tmp state as diagonal for next state
            diagonal = tmp;
            // updating the maximum sub-matrix encounted so far
            maxi = max(maxi, dp[j]);
        }
    }
    return maxi;
}
// -------------------------- STOP --------------------------

int main()
{
    // freopen(
    //     "..//test_cases//handmade_test_cases_expected_output.txt", "w",
    //     stdout);
    // freopen(
    //     "..//test_cases//handmade_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_input.txt", "r",
    //     stdin);
    // freopen(
    //     "..//test_cases//generated_big_test_cases_expected_output.txt", "w",
    //     stdout);
    // string testcases;
    // getline(cin,testcases);
    // int t = stoi(testcases);
    // while(t--) {
    string mat_rows_temp;
    getline(cin, mat_rows_temp);
    int n = stoi(ltrim(rtrim(mat_rows_temp)));

    string mat_columns_temp;
    getline(cin, mat_columns_temp);

    int m = stoi(ltrim(rtrim(mat_columns_temp)));

    vector<vector<int>> mat(n);

    for (int i = 0; i < n; i++)
    {
        mat[i].resize(m);
        string mat_row_temp_temp;
        getline(cin, mat_row_temp_temp);
        vector<string> mat_row_temp = split(rtrim(mat_row_temp_temp));
        for (int j = 0; j < m; j++)
        {
            int mat_row_item = stoi(mat_row_temp[j]);
            mat[i][j] = mat_row_item;
            assert(mat[i][j] <= 1000000000);
        }
    }
    int ans = largest_sub_square_matrix(n, m, mat);
    cout << ans << endl;
    // }
    return 0;
}

string ltrim(const string &str)
{
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str)
{
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}

vector<string> split(const string &str)
{
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos)
    {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
'''
