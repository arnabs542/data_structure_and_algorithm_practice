'''
Count Basins
Problem Statement:
You are given a matrix where each number represents altitude of that cell, such that, water flows towards lower altitudes.
 If a cell’s four neighboring cells all have higher altitudes, we call this cell a sink; water collects in sinks.
Otherwise, water will flow to the neighboring cell with the lowest altitude. If a cell is not a sink, you may assume it
 has a unique lowest neighbor and that this will be lower than the cell.
Cells that drain into the same sink – directly or indirectly – are said to be part of the same basin. Your challenge is
 to partition the map into basins. Your code should output the sizes of the basins, in non-decreasing order.
Input/Output Format For The Function:
Input Format:
There will be only one argument matrix denoting the matrix of size row_count * col_count, with the altitude represented
 as int in each cell.
Output Format:
Return an array of integers, denoting the sizes of basins, in non-decreasing order.
Input/Output Format For The Custom Input:
Input Format:
The first line of the input contains a number row_count, denoting the number of rows of the matrix. The second line of the
 input contains a number col_count, denoting the number of columns of the matrix. Next row_count lines, contains col_count
 numbers denoting matrix[i][j] where 0<=i<row_count and 0<=j<col_count.
For row_count=3, col_count=3 and matrix = [ [1, 5, 2], [2, 4, 7], [3, 6, 9]]
3
3
1 5 2
2 4 7
3 6 9
Output Format:
The output contains an array of numbers basin_sizes. Values of the basin_sizes array will be represented as one on a line.

For row_count=3, col_count=3 and matrix = [ [1, 5, 2], [2, 4, 7], [3, 6, 9]], output will be:
2
7
Constraints:
1 <= row_count * col_count <= 1000000.
0 <= matrix[i][j] <= 1000000 where 0<=i<row_count, 0<=j<col_count.
Sample Test Cases:
Sample Input:
3
3
1 5 2
2 4 7
3 6 9
Sample Output:
2
7
Explanation:
The basins, labeled with A’s and B’s, are:
A A B
A A B
A A A
Every cell labeled with A will sink at (0, 0), whereas B will sink at (0, 2).
Sample Input 2:
4
4
0 2 1 3
2 1 0 4
3 3 3 3
5 5 2 1
Sample Output 2:
4
5
7
Explanation:
The basins, labeled with A’s and B’s, are:
A A B B
A B B B
A B B C
A C C C
Every cell labeled with A will sink at (0, 0), B will sink at (1, 2) and C will sink at (3, 3).
'''
import math
import os
import random
import re
import sys


def find_basins(matrix):
    pass



def printMatrix(row_count, col_count, matrix):
    for i in range(row_count):
        for j in range(col_count):
            print(matrix[i][j], end=" ")
        print("")

if __name__ == '__main__':
    row_count = int(input())
    col_count = int(input())

    matrix = []

    for x in range(row_count):
        matrix.append(list(map(int, input().rstrip().split())))

    # printMatrix(row_count, col_count, matrix)

    basin_sizes = find_basins(matrix)

    fptr = sys.stdout

    fptr.write('\n'.join(map(str, basin_sizes)))
    fptr.write('\n')

    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
In this naive approach, we will simply assign each cell a unique id. Then iterate over the matrix and change each cell’s
 id to the id of the cell where it sinks.
For Example:
1 5 2
2 4 7
3 6 9
In this start by creating a new matrix to store ids and assign unique ids to each cell:
0 1 2
3 4 5
6 7 8
Then for each cell change its id as follows
(0, 0) is a sink so its id stays the same.
(0, 1) flows to (0, 0) (as it’s the minimum neighbour), so set its id to 0.
...
(1, 1) flows to (0, 1), then flows to (0,0) so set its id to 0.
...
And so on, to get a matrix like as follows:
0 0 1
0 0 1
0 0 0
Now, just count the total number of occurrences of remaining ids and return them in descending order. For a better understanding
 look at the code.
Time Complexity:
O((row_count*col_count)^2) where row_count is the number of rows in the given matrix and col_count is the number of columns
 in the given matrix.
As for each node in the worst case we will traverse complete matrix, the time complexity for this will be (row_count*col_count)
 * O(row_count*col_count) and as we are returning a sorted array and in worst case number of sinks can be equal to row_count*col_count
 so to sort it will take O(row_count*col_count) → O((row_count*col_count)^2).
Complexity to sort the resultant array is O(n) as we are using counting sort to sort the array.
To read about how counting sort works: https://www.geeksforgeeks.org/counting-sort/
Auxiliary Space Used:
O(row_count*col_count) where row_count is the number of rows in the given matrix and col_count is the number of columns
 in the given matrix.
As we are maintaining another matrix for the value of ids, it will take O(row_count*col_count) and recursion stack can also
 take O(row_count*col_count) space in the worst case. Also, we are sorting the resultant array using counting sort and in
 the worst case size of that array can be row_count*col_count hence it takes O(row_count*col_count) extra space. So, total
 complexity will be 3*O(row_count*col_count) → O(row_count*col_count).
Space Complexity:
O(row_count*col_count) where row_count is the number of rows in the given matrix and col_count is the number of columns
 in the given matrix.
For storing input it will take O(row_count*col_count) and as auxiliary space used is O(row_count*col_count). Hence total
 complexity will be 2*O(row_count*col_count) → O(row_count*col_count).
2) optimal_solution_1.java
Description:
This approach will be a greedy one. If we analyze the matrix closely we can easily see that the cell with the lowest altitude
 in the entire matrix will always be a sink, also, that all the neighbors of the cell with the lowest altitude, will flow
 into that cell.
We can use this fact to systematically map which cells belong to which basin.
Create a new matrix and initialize all cells with -1.
Now iterate over the cells from lowest to highest altitude.
If the current cell is unmarked, mark it with a new id.
Mark all its unmarked neighbor to be the same as the current cell. 
Finally, count all the total number of times each id occurs in the new matrix and return in descending order.
For example:
1 5 2
2 4 7
3 6 9
Create the id matrix as 
-1 -1 -1
-1 -1 -1
-1 -1 -1
Start with the lowest altitude that is 1 at (0, 0) and mark it with a new id, and change all it’s neighbors to its id.
0  0 -1
0 -1 -1
-1 -1 -1
Now the next lowest ids are at (0, 2) and (1, 0)
At (0, 2), as it is unmarked mark it with a new id, skip the neighbor already marked and change the remaining
0  0 1
0 -1  1
-1 -1 -1
Similarly for (1, 0), as it is already marked, change its neighbors to be the same as it.
0  0 1
0  0 1
0 -1 -1
Continue this until all cells have been processed. And the resultant matrix will be:
0 0 1
0 0 1
0 0 0
We can use the map to map heights to cells, and then sort the heights in ascending order to mark the cells. For a better
 understanding look at the code.
Time Complexity:
O(row_count*col_count*log(row_count*col_count)) where row_count is number of rows in given matrix and col_count is number
 of columns in given matrix.
To store height and list of pairs in the sorted map, it will take O(row_count*col_count*log(row_count*col_count)). For processing
 each cell afterward, it only takes constant operation per cell. So, the worst case complexity is O(row_count*col_count*log(row_count*col_count)).
 We are returning resultant array after sorting using counting_sort and in worst case number of sinks can be row_count*col_count
 so time complexity to sort sinks will be O(row_count*col_count) in the worst case. Hence total complexity will be O(row_count*col_count*log(row_count*col_count))
 + O(row_count*col_count) → O(row_count*col_count*log(row_count*col_count)).
Auxiliary Space Used:
O(row_count*col_count) where row_count is the number of rows in the given matrix and col_count is the number of columns
 in the given matrix.
As we are keeping track of ids of each element of the matrix. It will take O(row_count*col_count) extra space. We are using
 sorted map named heights which will take O(row_count*col_count) extra space. And using counting sort to sort row_count*col_count
 sinks in the worst case, it will use extra space of O(row_count*col_count). Hence total auxiliary space used will be 3*O(row_count*col_count)
 → O(row_count*col_count).
Space Complexity:
O(row_count*col_count) where row_count is the number of rows in the given matrix and col_count is the number of columns
 in the given matrix.
For storing input, it will take O(row_count*col_count) space and as auxiliary space used is O(row_count*col_count). Hence
 total complexity will be O(row_count*col_count).
3) optimal_solution_2.java
Description:
This approach will be an optimized version of brute_force approach. Same as the brute force, but this time we can mark all
 the cells we passed through while calculating the sink of a particular cell and ignoring any cell already processed.
Start by initializing the id matrix with -1. 
Iterate over each cell in the matrix, skip cells already marked. 
For each
 cell recursively call the cell it flows towards till we reach a sink or a cell which is already marked.
If the current
 cell is marked return it’s id.
If the current cell is a sink, set it’s id if not set otherwise return the id.
Set the returned
 id for each cell.
Continue until all cells are marked.
For example:
2 1 3
2 3 4
3 2 1
Initialize the id matrix:
-1 -1 -1
-1 -1 -1
-1 -1 -1
(0, 0) flows to (0, 1) which is a sink. So mark both them with 0.
Skip (0, 1) already marked.
0  0 -1
-1 -1 -1
-1 -1 -1
And continue like this till all cells are marked. And the resultant matrix will be:
0 0 1
0 0 1
0 0 0
Time Complexity:
O(row_count*col_count) where row_count is the number of rows in the given matrix and col_count is the number of columns
 in the given matrix.
As we are iterating over the matrix and each cell will be computed once. And we are sorting the resultant array using counting
 sort so it will take O(row_count*col_count) as in worst case size of the resultant array can be row_count*col_count. Hence
 total complexity will be 2*O(row_count*col_count) → O(row_count*col_count).
Auxiliary Space Used:
O(row_count*col_count) where row_count is the number of rows in the given matrix and col_count is the number of columns
 in the given matrix.
As we are keeping track of ids of each element of the matrix. It will take O(row_count*col_count) extra space. Recursion
 stack can also take O(row_count*col_count) space in the worst case. And as we are sorting the resultant array using counting
 sort which can have row_count*col_count number of elements in the worst case, it will take extra space of O(row_count*col_count).
 Hence total auxiliary space used will O(row_count*col_count).
Space Complexity:
O(row_count*col_count) where row_count is the number of rows in the given matrix and col_count is the number of columns
 in the given matrix.
For storing input, it will take O(row_count*col_count) space and as auxiliary space used is O(row_count*col_count). Hence
 total complexity will be O(row_count*col_count).
'''
'''
BRUTE FORCE
#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

//-------------------------------------START---------------------------------------
void count_sort(vector <int>& arr) {
    int max = *max_element(arr.begin(), arr.end());
    int min = *min_element(arr.begin(), arr.end());
    int range = max - min + 1;

    vector<int> count(range), output(arr.size());
    for(int i = 0; i < arr.size(); i++) {
        count[arr[i]-min]++;
    }

    for(int i = 1; i < count.size(); i++) {
        count[i] += count[i-1];
    }

    for(int i = arr.size()-1; i >= 0; i--) {
        output[ count[arr[i]-min] -1 ] = arr[i];
        count[arr[i]-min]--;
    }

    for(int i=0; i < arr.size(); i++) {
        arr[i] = output[i];
    }
}

int get_sink(vector< vector<int> > &matrix, vector< vector<int> > &basins, int row, int col) {
    int min_row = row, min_col = col;
    // Check element which is at left
    if (col > 0 && matrix[row][col - 1] < matrix[min_row][min_col]) {
        min_col = col - 1;
        min_row = row;
    }
    // Check element which is at down
    if (row > 0 && matrix[row - 1][col] < matrix[min_row][min_col]) {
        min_col = col;
        min_row = row - 1;
    }
    // Check element which is at up
    if (row < matrix.size() - 1 && matrix[row + 1][col] < matrix[min_row][min_col]) {
        min_col = col;
        min_row = row + 1;
    }
    // Check element which is at right
    if (col < matrix[0].size() - 1 && matrix[row][col + 1] < matrix[min_row][min_col]) {
        min_col = col + 1;
        min_row = row;
    }

    if (row == min_row && col == min_col){
        // If we reached at sink
        return basins[min_row][min_col];
    }

    // Recursively call to get sink for element matrix[min_row][min_col]
    return get_sink(matrix, basins, min_row, min_col);
}

vector<int> find_basins(vector< vector<int> > matrix) {
    int row_count = matrix.size();
    int col_count = matrix[0].size();

    // To maintain ids of each element of matrix
    vector< vector<int> > basins(row_count, vector<int>(col_count));

    int idx = 0;

    for (int i = 0; i < row_count; i++){
        for (int j = 0; j < col_count; j++){
            basins[i][j] = idx++;
        }
    }

    // To maintain id wise count of elements which will sink in that id
    unordered_map<int, int> basin_indexes;

    for (int i = 0; i < row_count; i++) {
        for (int j = 0; j < col_count; j++) {
            int sink = get_sink(matrix, basins, i, j);
            basin_indexes[sink] = basin_indexes[sink] + 1;
        }
    }

    vector<int> basin_sizes;

    for (auto pair : basin_indexes) {
        basin_sizes.push_back(pair.second);
    }

    // Sorting by size of sinks
    count_sort(basin_sizes);

    return basin_sizes;
}
//-------------------------------------END---------------------------------------

int main() {
    string row_count_temp;
    getline(cin, row_count_temp);

    int row_count = stoi(ltrim(rtrim(row_count_temp)));

    string col_count_temp;
    getline(cin, col_count_temp);

    int col_count = stoi(ltrim(rtrim(col_count_temp)));

    vector< vector<int> > matrix(row_count);
    for (int i = 0; i < row_count; i++) {
        matrix[i].resize(col_count);

        string row;
        getline(cin, row);

        vector<string> values = split(rtrim(row));

        for (int j = 0; j < col_count; j++) {
            matrix[i][j] = stoi(values[j]);
        }
    }

    ostream &fout = cout;

    vector<int> basin_sizes = find_basins(matrix);

    for (int i = 0; i < basin_sizes.size(); i++){
        fout << basin_sizes[i] << endl;
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
'''
'''
OPTIMIAL SOLUTION 1
#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

//-------------------------------------START---------------------------------------
void count_sort(vector <int>& arr) {
    int max = *max_element(arr.begin(), arr.end());
    int min = *min_element(arr.begin(), arr.end());
    int range = max - min + 1;

    vector<int> count(range), output(arr.size());
    for(int i = 0; i < arr.size(); i++) {
        count[arr[i]-min]++;
    }

    for(int i = 1; i < count.size(); i++) {
        count[i] += count[i-1];
    }

    for(int i = arr.size()-1; i >= 0; i--) {
        output[ count[arr[i]-min] -1 ] = arr[i];
        count[arr[i]-min]--;
    }

    for(int i=0; i < arr.size(); i++) {
        arr[i] = output[i];
    }
}

vector<int> find_basins(vector< vector<int> > matrix) {
    int row_count = matrix.size();
    int col_count = matrix[0].size();

    // To maintain ids of each element of matrix
    vector< vector<int> > basins(row_count, vector<int>(col_count, -1));

    // To store sorted entries with key as height and value as list of pair with that height
    map< int, vector< pair<int, int> > > heights;

    for (int i = 0; i < row_count; i++){
        for (int j = 0; j < col_count; j++){
            heights[matrix[i][j]].push_back(make_pair(i, j));
        }
    }

    int basin_index = 0;

    for (auto height_pair : heights) {
        for (pair<int, int> index : height_pair.second) {
            int row = index.first;
            int col = index.second;

            // If element is sink itself
            if (basins[row][col] == -1){
                basins[row][col] = basin_index++;
            }
            // Check element which is at left
            if (col > 0 && basins[row][col - 1] == -1){
                basins[row][col - 1] = basins[row][col];
            }
            // Check element which is at up
            if (row > 0 && basins[row - 1][col] == -1){
                basins[row - 1][col] = basins[row][col];
            }
            // Check element which is at down
            if (row < matrix.size() - 1 && basins[row + 1][col] == -1){
                basins[row + 1][col] = basins[row][col];
            }
            // Check element which is at right
            if (col < matrix[0].size() - 1 && basins[row][col + 1] == -1){
                basins[row][col + 1] = basins[row][col];
            }
        }
    }

    vector<int> basin_sizes(basin_index);

    for (int i = 0; i < row_count; i++){
        for (int j = 0; j < col_count; j++){
            basin_sizes[basins[i][j]]++;
        }
    }

    // Sorting by size of sinks
    count_sort(basin_sizes);

    return basin_sizes;
}
//-------------------------------------END---------------------------------------

int main() {
    string row_count_temp;
    getline(cin, row_count_temp);

    int row_count = stoi(ltrim(rtrim(row_count_temp)));

    string col_count_temp;
    getline(cin, col_count_temp);

    int col_count = stoi(ltrim(rtrim(col_count_temp)));

    vector< vector<int> > matrix(row_count);
    for (int i = 0; i < row_count; i++) {
        matrix[i].resize(col_count);

        string row;
        getline(cin, row);

        vector<string> values = split(rtrim(row));

        for (int j = 0; j < col_count; j++) {
            matrix[i][j] = stoi(values[j]);
        }
    }

    ostream &fout = cout;

    vector<int> basin_sizes = find_basins(matrix);

    for (int i = 0; i < basin_sizes.size(); i++){
        fout << basin_sizes[i] << endl;
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
'''
'''
OPTIMAL SOLUTION 2
#include <bits/stdc++.h>
#include <vector>
#include <algorithm>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

//-------------------------------------START---------------------------------------
void count_sort(vector <int>& arr) {
    int max = *max_element(arr.begin(), arr.end());
    int min = *min_element(arr.begin(), arr.end());
    int range = max - min + 1;

    vector<int> count(range), output(arr.size());
    for(int i = 0; i < arr.size(); i++) {
        count[arr[i]-min]++;
    }

    for(int i = 1; i < count.size(); i++) {
        count[i] += count[i-1];
    }

    for(int i = arr.size()-1; i >= 0; i--) {
        output[ count[arr[i]-min] -1 ] = arr[i];
        count[arr[i]-min]--;
    }

    for(int i=0; i < arr.size(); i++) {
        arr[i] = output[i];
    }
}

int get_sink(vector< vector<int> >& matrix, vector< vector<int> >& basins, int row, int col, int basin_idx) {
    if (basins[row][col] == -1) {
        int min_row = row, min_col = col;
        // Check element which is at left
        if (col > 0 && matrix[row][col - 1] < matrix[min_row][min_col]) {
            min_col = col - 1;
            min_row = row;
        }
        // Check element which is at up
        if (row > 0 && matrix[row - 1][col] < matrix[min_row][min_col]) {
            min_col = col;
            min_row = row - 1;
        }
        // Check element which is at down
        if (row < matrix.size() - 1 && matrix[row + 1][col] < matrix[min_row][min_col]) {
            min_col = col;
            min_row = row + 1;
        }
        // Check element which is at right
        if (col < matrix[0].size() - 1 && matrix[row][col + 1] < matrix[min_row][min_col]) {
            min_col = col + 1;
            min_row = row;
        }
        // If we found sink
        if (min_row == row && min_col == col) {
            basins[row][col] = basin_idx;
        }
        else {
            // Recursively call to find sink for element matrix[min_row][min_col]
            basins[row][col] = get_sink(matrix, basins, min_row, min_col, basin_idx);
        }
    }

    return basins[row][col];
}

vector<int> find_basins(vector< vector<int> > matrix) {
    int row_count = matrix.size();
    int col_count = matrix[0].size();

    // To maintain ids of each element of matrix
    vector< vector<int> > basins(row_count, vector<int>(col_count, -1));

    int basin_idx = 0;

    for (int i = 0; i < row_count; i++){
        for (int j = 0; j < col_count; j++){
            if (get_sink(matrix, basins, i, j, basin_idx) == basin_idx){
                basin_idx++;
            }
        }
    }
    // To store sink sizes
    vector<int> basin_sizes(basin_idx);

    for (int i = 0; i < row_count; i++){
        for (int j = 0; j < col_count; j++){
            basin_sizes[basins[i][j]]++;
        }
    }
    // Sorting on sink sizes
    count_sort(basin_sizes);

    return basin_sizes;
}
//-------------------------------------END---------------------------------------

int main() {
    string row_count_temp;
    getline(cin, row_count_temp);

    int row_count = stoi(ltrim(rtrim(row_count_temp)));

    string col_count_temp;
    getline(cin, col_count_temp);

    int col_count = stoi(ltrim(rtrim(col_count_temp)));

    vector< vector<int> > matrix(row_count);
    for (int i = 0; i < row_count; i++) {
        matrix[i].resize(col_count);

        string row;
        getline(cin, row);

        vector<string> values = split(rtrim(row));

        for (int j = 0; j < col_count; j++) {
            matrix[i][j] = stoi(values[j]);
        }
    }

    ostream &fout = cout;

    vector<int> basin_sizes = find_basins(matrix);

    for (int i = 0; i < basin_sizes.size(); i++){
        fout << basin_sizes[i] << endl;
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
'''

