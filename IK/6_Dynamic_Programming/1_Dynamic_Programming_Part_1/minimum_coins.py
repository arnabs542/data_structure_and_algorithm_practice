'''
Minimum Coins
Problem Statement:
Every currency system has a fixed denomination system such that a given amount of change can be expressed as the sum of
 these denominations.
Given coins for a currency system with positive integral values C1, C2, C3...........Cn with an infinite supply of each
 type of coin and a positive integer value. You have to make value using a minimal number of coins.
It is guaranteed that there will be always a coin with value 1 so a solution always exists.
Input/Output Format For The Function:
Input Format:
First is an integer array of values of coins and second is a positive integer value denoting the change you have to make.

Output Format:
Return an integer representing the minimum number of coins required.
Input/Output Format For The Custom Input:
Input Format:
The first line of the input contains an integer n, denoting no. of coins denominations. In the next n lines, the ith line
 contains an integer coin denoting coins[i]. The n+2 th line of the input contains an integer value, denoting value for
 which coins denominations to found.
If coins=[1, 3, 5], value=9, then input should be:
3
1
3
5
9
Output Format:
The one and only line of output will contain a single integer representing the minimum number of coins required to make
 value.
For input coins=[1, 3, 5], value=9, result will be:
3
Constraints:
1 <= length of array of coins <= 100.
1 <= value <= 10000.
1 <= coins[i] <= 100 for 0 <= i < length of array of coins.
Coins
 array will always have unique coin denomination values.
Sample Test Case:
Sample Input:
3
1
3
5
9
Sample Output:
3
Explanation:
For denominations of coins [1, 3, 5] and as we have every denomination in the infinite count. We want to make 9 using given
 denominations. So all possible unique ways to generate 9 are:
[1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 3]
[1, 1, 1, 1, 5]
[1, 1, 1, 3, 3]
[1, 3, 5]
[3, 3, 3]
And as [1, 3, 5] and [3, 3, 3] requires only 3 coins to make 9 and which is minimum from all other cases. Hence our answer
 is 3.
'''
import math
import os
import random
import re
import sys

#
# Complete the 'minimum_coins' function below.
#
# The function accepts INTEGER ARRAY and INTEGER as parameter.
# Return INTEGER ARRAY.
#
def minimum_coins(coins, value):
    pass


if __name__ == '__main__':
    n = int(input().strip())
    coins = []
    for _ in range(n):
        coins.append(int(input().strip()))
    value = int(input().strip())
    fptr = sys.stdout
    result = minimum_coins(coins, value)
    fptr.write(str(result))
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.cpp
Description:
To find out the number of minimum coins required to make value from given coins. We will follow:
Recursive definition:
If value == 0:
return 0 (then 0 coins are required to make the value (end of recursion or base case))
If value > 0:
	minimum_coins(value) = min {1 + minimum_coins(value-coins[i])} (where i belongs to [0,n-1] and coins[i] <= value)
Basically what we are doing here is exhaustively searching for all the possible combinations of denominations which can
 generate our desired value and maintain a minimum number of coins of required to generate that value and that will be our
 answer.
This method is not efficient as it computes subproblems again and again.
Time Complexity:
O(n^value) where n denotes the number of different denominations and value is value to make.
As we are recursively searching for all possible possibilities to make value. It will take O(n^value).
Auxiliary Space Used:
O(value) where value is value to make.
As the number of recursion calls in function stack can be O(value).
Space Complexity:
O(n + value) where n denotes the number of different denominations and value is value to make.
To store input, it will take O(n) as we are storing n number of coins, and as auxiliary space used is O(value) hence O(n)
 + O(value) → O(n + value).
2) optimal_solution.cpp
Description:
It’s fairly intuitive that the brute force method computes subproblems, again and again, so we need to cache the data.
It can be easily done using bottom-up DP approach. We will use a 1-D array as DP table which at ith index stores the minimum
 number of coins required to make the change i.
Base case: dp[0]=1 and initialize for all i in [1,change] dp[i]=INF
We use 2 loops:
Where 1st loop(i) iterates the values from [1-change] and 2nd loop(j) iterates the given coins.
For every value of i and coins[j] we check if that i (current change to be made) is greater than or equals to the coin value
 i.e. i>=coins[j]. If yes, then we update dp[i] = min(dp[i],1+dp[i-coins[j]]).
After the dp table has been constructed, dp[value] will
give us our answer.
Time Complexity:
O(n*value) where n denotes the number of different denominations and value is value to make.
To generating 1d dp values, it will take O(n*value), as it will take two loops of size value and size n.
Auxiliary Space Used:
O(value) where value denotes the value to make.
To store 1d dp array, it will take O(value).
Space Complexity:
O(n + value) where n denotes the number of different denominations and value denotes the value to make.
To store input, it will take O(n) as we are storing n number of coins, and as auxiliary space used is O(value) hence O(n)
 + O(value) → O(n + value).
'''
'''
BRUTE FORCE
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

//--------------------------------START-------------------------------

int minimum_coins(vector<int> &coins, int value) {
    // If value is zero return 0.
    if (value == 0) {
        return 0;
    }
    // Maximum value assigned initially
    int global_min=100005;
    for(int i=0; i < coins.size(); i++){
        if (coins[i] <= value) {
            // To find minimum coins required to make remaining value-coins[i]
            int local_min=minimum_coins(coins, value-coins[i]);
            // local_min number of coins required to make remaining value-coins[i] and 
            // 1 coin with value coins[i] used.
            if (local_min+1 < global_min) {
                global_min=local_min+1;
            }
        }
    }
    // Return maintained global minimum value
    return global_min; 
}

//--------------------------------END-------------------------------

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<int> coins(n);

    for (int i = 0; i < n; i++) {
        string coin;
        getline(cin, coin);

        coins[i] = stoi(ltrim(rtrim(coin)));
    }
    
    string value_temp;
    getline(cin, value_temp);

    int value = stoi(ltrim(rtrim(value_temp)));
    
    ostream &fout = cout;

    int result = minimum_coins(coins, value);
    fout << result;
    fout << "\n";
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
OPTIMAL SOLUTION
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

//--------------------------------START-------------------------------

const int MAX_VALUE=100005;

int minimum_coins(vector<int> coins, int value) {
    // Dp array of size (value+1) and pre filled value MAX_VALUE
    vector<int> dp(value+1, MAX_VALUE), ans;
    // As number of coins required to make 0 value is 0
    dp[0]=0;
    // Following nested loop calculates the minimum number of coins 
    // required to make the value i and stored in dp table
    int n=coins.size();
    for(int i=1; i <= value; i++) {
        for(int j=0; j < n; j++) {
            if (i >= coins[j] and 1+dp[i-coins[j]] < dp[i]) {
                // Condition that we have found a better minimal solution
                dp[i]=1+dp[i-coins[j]];
            }
        }
    }
    // Recursive function that calculates the distinct combinations of minimal size
    // that has the sum given to the input value
    return dp[value];
}
//--------------------------------END-------------------------------

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<int> coins(n);

    for (int i = 0; i < n; i++) {
        string coin;
        getline(cin, coin);

        coins[i] = stoi(ltrim(rtrim(coin)));
    }
    
    string value_temp;
    getline(cin, value_temp);

    int value = stoi(ltrim(rtrim(value_temp)));
    
    ostream &fout = cout;

    int result = minimum_coins(coins, value);
    fout << result;
    fout << "\n";
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
