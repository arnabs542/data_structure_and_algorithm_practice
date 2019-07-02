'''
Power
Problem Statement:
The problem statement is straight forward. Given a base ‘a’ and an exponent ‘b’. Your task is to find a^b. The value
could be large enough. So, calculate a^b % 1000000007.
Input/Output Format For The Function:
Input Format:
First parameter of the function denotes base a and the second parameter of the function denotes the exponent b.
Output Format:
The function returns an integer variable denoting the calculated value of a^b % 1000000007.
Input/Output Format For The Custom Input:
Input Format:
First line of the input contains one single integer a, denoting the value of the base and the second line also contains
one single integer denoting the value of the exponent.
If a = 2 and b = 10, then custom input format will be:
2
10

Output Format:
Print one single line containing one integer denoting the calculated value of a^b % 1000000007.
For the above provided custom input, output would be:
1024

Constraints:
0 <= a <= 10^18
0 <= b <= 10^18
a and b together can’t be 0

Sample Test Case:
a = 2
b = 10

Sample Output:
1024

Explanation:
For the above sample input:
2^10 = 1024, and
1024 % 1000000007 = 1024
Hence, output is 1024.
'''

import math
import os
import random
import re
import sys
#
#  Complete the calculate_power function below.
#  @param a: base
#  @param b: exponent
#
def calculate_power(a,b):
    pass


if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    fptr = sys.stdout
    result = calculate_power(a,b)
    fptr.write(str(result) + "\n")
    fptr.close()

'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution:
Description:
In this approach, we simply keep multiplying the integer a, b number of times and after each multiplication if the 
product so far has increased the MOD value then we apply the mod (%) operator on it.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(b), where b is the exponent
To calculate a^b we are iterating from 1 to b, Hence the time complexity is O(b).
Time Complexity:
O(b), where b is the exponent
To calculate a^b we are iterating from 1 to b, Hence the time complexity is O(b).
Auxiliary Space Used:
O(1)

As we use just one variable to store the incremental product variable after each iterative multiplication.
Space Complexity:
O(1)

The function parameters are two integers that takes O(1) space. Hence, the total Space Complexity auxiliary space plus 
input space i.e. O(1) + O(1) ~ O(1).
2) other_solution:
Description:
In this approach we will try to solve this problem in a recursive manner. Let’s say we need to calculate a^b. Now, this
 can be reduced to a^b = a^(b/2) * a^(b/2) , if b is even and for the case when b is odd then we can say that 
 a^b = a^(b/2) * a^(b/2) * a.

Let’s say f(a,b) is the power function that denotes a^b. So, f(a,b) can be represented as:
f(a , b) = { f(a , b/2) * f(a , b/2) , when b is even;
      f(a , b/2) * f(a , b/2) * a , when b is odd;
      1, when b is zero }
We will use the above recursive relation to evaluate a^b.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(log(b)), where b is the exponent.
The recursive equation that we are using keeps reducing the exponent by half at each step till the exponent reduces to 
zero. Therefore, this takes O(log(b)) iterations to evaluate a^b.

Time Complexity:
O(log(b)), where b is the exponent.
The recursive equation that we are using keeps reducing the exponent by half at each step till the exponent reduces 
to zero. Therefore, this takes O(log(b)) iterations to evaluate a^b.
Auxiliary Space Used:
O(log(b)), where b is the exponent.

The recursive function calls consumes a recursive stack memory for each function call that is equal to O(log(b)).

Space Complexity:
O(log(b)), where b is the exponent.

The total space complexity is equal to the auxiliary space plus the input and output space. Here the input and output 
space complexity is constant O(1) as we are only taking two integers as input and returning one integer as output. 
Hence, the total space complexity becomes O(log(b)) + O(1) ~ O(log(b)).

2) optimal_solution:
Description:
In this approach we will use the same power doubling principal as used in the other_solution approach. In the above 
solution we used top down approach by spiting into half at each step. Here, in this approach we will solve it using 
bottom up approach by doubling at each step. Below is the mathematical illustration of the approach using an example :
So, this will be our approach in solving this problem in bottom-up fashion. We will start with the least significant 
bit of the exponent when represented in binary and for each set bit we keep on multiplying that power of the base into 
our final result. Kindly, refer to the implementation for better understanding.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(log(b)), where b is the exponent.

To evaluate the power we are iterating over all set-bits of the exponent which takes O(b) iterations.

Time Complexity:
O(log(b)), where b is the exponent.

To evaluate the power we are iterating over all set-bits of the exponent which takes O(b) iterations.
Auxiliary Space Used:
O(1)

This is a bottom up iterative approach. Hence, no stack memory is consumed in recursive function calls as compared to 
the other_solution.
Space Complexity:
O(1)

The total space complexity is equal to the auxiliary space plus the input and output space. Here the input and output 
space complexity is constant O(1) as we are only taking two integers as input and returning one integer as output. 
Hence, the total space complexity becomes O(1) + O(1) ~ O(1).
'''

'''
BRUTE FORCE
#include "bits/stdc++.h"
using namespace std;

// ------------------------------ START ---------------------
const int MOD = 1e9 + 7;

int calculate_power(long long a, long long b) {
    // stores final evaluated value of a^b % MOD
    long long result = 1LL;
    // iterate 1 to b
    for (int i = 0; i < b; i ++) {
        // keep multiplying a
        result = result * a % MOD;
    }
    return(int)result;
}
// ------------------------------ STOP ----------------------

int main(int argc, char const * argv[]) {
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
    long long a;
    long long b;
    cin >> a >> b;
    int ans = calculate_power(a, b);
    cout << ans << endl;
    // }
    return 0;
}
'''
'''
OPTIMAL
#include "bits/stdc++.h"
using namespace std;

// ------------------------------ START ---------------------------
const int MOD = 1e9 + 7;

int calculate_power(long long a, long long b) {
    // stores final evaluated power a^b
    long long result = 1;
    // stores a^(power of two)
    // initialixzed with a^(2^0)
    long long powerOfTwo = a % MOD;

    // iterate over all bits of b
    while (b != 0) {
        // if current bit is set
        if (b % 2 == 1) {
            // multiply the current power in result
            result = result * powerOfTwo % MOD;
        }
        // double the power of two
        // a^i * a^i = a^(2*i)
        powerOfTwo = powerOfTwo * powerOfTwo % MOD;
        // move to next bit of b
        b = b / 2;
    }
    return(int)result;
}

// ------------------------------ STOP ----------------------------

int main(int argc, char const * argv[]) {
    // freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
    // freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
    // freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
    // freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
    // int t;
    // cin >> t;
    // while (t --) {
    long long a;
    long long b;
    cin >> a >> b;
    int ans = calculate_power(a, b);
    cout << ans << endl;
    // }
    return 0;
}
'''
