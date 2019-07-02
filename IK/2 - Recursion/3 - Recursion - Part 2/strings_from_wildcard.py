'''
Strings From Wild Card
Problem Statement:
You are given string s of length n, having m wildcard characters '?', where each wildcard character represent
a single character. Write a program which returns list of all possible distinct strings that can be generated by
replacing each wildcard characters in s with either '0' or '1'.

Any string in returned list must not contain '?' character i.e. you have to replace all '?' with either '0' or '1'.
The purpose of this problem is to learn recursion and not DP. So, you must write at least one recursive solution.
After that, you can write a DP solution if you want.
Input Format:
There is only one argument s, denoting input string.

Output Format:
Return a result list of distinct strings (No fix order of strings in result list is required).

Constraints:
1 <= n <= 50, where n is length of s.
0 <= m <= 17, where m is number of ‘?’ (wildcard characters) in s.

Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
s = “1?10”

Sample Output 1:
result = ["1010", "1110"] or ["1110", "1010"].

Explanation 1:
‘?’ at index 1 (0 based indexing) can be replaced with either '0' or '1'. So, generated two strings replacing '?'
with ‘0’ and ‘1’.

Sample Test Case 2:
Sample Input 2:
s = “1?0?”

Sample Output 2:
result = ["1000", "1001", "1100", "1101"] or any other list having same strings but in different order.

Explanation 2:
Input string have two '?' characters. Each one can be replaced with either '0' or '1'. So, total 2*2 strings are
possible as ('?' at index 1, '?' at index 3) can be replaced with ('0','0'), ('0','1'), ('1', '0'), ('1', '1').
'''
#!/bin/python3

import os
import sys


def find_all_possibilities(s):
    pass


if __name__ == "__main__":
    fptr = sys.stdout

    s = input()

    res = find_all_possibilities(s)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()

'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
A naive approach would be generate all possible strings having '0's and '1's only, of length n, and filter out to 
select the ones which has mismatch with s only at all index i, where s[i] = '?', 0 <= i <= (n-1).

Time Complexity:
O(n*(2^n)) where n is length of s string.

As there are 2^n possible strings containing '0's and '1's only, and we are traversing through each generated string, 
to find out whether that generated string is equivalent to s or not if we ignore places where in s character is ‘?’.
As we are iterating over 2^n possible strings and to iterate over a single generated string it takes O(n) where n is 
length of generated string.
So, total time complexity will be O(n*(2^n)).

Auxiliary Space Used:
O(n) where n is length of given string.

As at any time we are just generating and storing single possible string to compare that whether generated string will 
be included in result or not. So, extra space will be equivalent to length of possible string.

Space Complexity:
O(n*(2^m)) where n is length of s string and m is number of ‘?’ (wild card) characters in s string.

To store input, it will take O(n) and result list will contains number of strings equal to 2^(number of ‘?’ 
characters in s i.e. m) so, space for result list will be O(n *(2^m)) and auxiliary space used is taking O(n).
Total space complexity will be
O(n*(2^m)) + O(n) → O(n*(2^m))

2) optimal_solution.java
Description:
Better approach would be only to generate valid possible strings matching with s instead of generating all 
possible strings.
For doing this we can replace every ‘?’ with ‘0’ and ‘1’. This approach would be a recursive approach. Because 
every time after replacing a single ‘?’ at index i ( 0 <= i <= n-1 where n is length of s ) we are trying to replace 
remaining ‘?’ in string having index j ( i < j < n-1 ).

Time Complexity:
O(n*(2^m)) where n is length of s string and m is number of ‘?’ (wild card) characters in s string.

As, two recursive calls will be made when s[i] == '?', and there are total m '?' and we are generating that possible 
string when we are reaching at the end of s to be added in final result list.
So, total time complexity will be O(n*(2^m)).

Auxiliary Space Used:
O(n) where n is length of given string.

As at any time we are maintaining current possible string generated in the solution and length of that string can be n.

Space Complexity:
O(n*(2^m)) where n is length of s string and m is number of ‘?’ (wild card) characters in s string.
To store input, it will take O(n) and result list will contains number of strings equal to 2^(number of ‘?’ 
characters in s i.e. m) so, space for result list will be O(n *(2^m)) and auxiliary space used is taking O(n).
Total space complexity will be
O(n*(2^m)) + O(n) → O(n*(2^m))
'''
'''
BRUTE FORCE
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * You are given string s of length n, having m WildCard characters '?', where each WildCard character represent
 * a single character. Write a program which returns all possible distinct strings valStr that can be generated by
 * replacing each WildCard characters in s with either a '0' or '1'.
 * Note that valStr doesn't contain any '?'
 */
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static String[] find_all_possibilities(String s) {
        int n = s.length();
        char[] input = s.toCharArray();
        List<String> allStrings = new ArrayList<>();
        char[] current;
        long end = (1L << n);
        // Generating all possible binary arrays and matching it with given s, if suitable
        // match found then add to result list allStrings else not.
        for (int i = 0; i < end; i++) {
            current = getBinaryArray(i, n);
            if (checkIfMismatchOnlyAtWildCard(input, current)) {
                allStrings.add(new String(current));
            }
        }
        int count = allStrings.size();
        String result[] = new String[count];
        for(int i = 0; i < count; i++){
            result[i] = allStrings.get(i);
        }
        return result;
    }

    static boolean checkIfMismatchOnlyAtWildCard(char[] input, char[] current) {
        /*
         * To check whether input char array and current char array are matching at all indices
         * other than indices where character in input char array is '?'
         */
        for (int i = 0; i < input.length; i++) {
            if (input[i] == '?') {
                continue;
            }
            if (input[i] != current[i]) {
                return false;
            }
        }
        return true;
    }

    static char[] getBinaryArray(int x, int n) {
        /*
         * To generate binary array representing x padded with 0
         */
        char[] res = new char[n];
        for (int i = 0; i < n; i++) {
            res[n - 1 - i] = (char) ((((1L << i) & x) >> i) + '0');
        }
        return res;
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

        String s = bufferedReader.readLine().trim();

        String result[] = Result.find_all_possibilities(s);
        for (String str: result) {
            bufferedWriter.write(str+"\n");
        }

        bufferedWriter.close();

        bufferedReader.close();
    }

}

/**
 * Time complexity: O(n*(2^n))
 * Space complexity: O(n*(2^m))
 */

'''
'''
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * You are given string s of length n, having m WildCard characters '?', where each WildCard character represent
 * a single character. Write a program which returns all possible distinct strings valStr that can be generated by
 * replacing each WildCard characters in s with either a '0' or '1'.
 * Note that valStr doesn't contain any '?'
 */
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static char possibleChars[] = {'0', '1'};

    static String[] find_all_possibilities(String s) {
        int n = s.length();
        char[] input = s.toCharArray();
        char[] current = new char[n];
        List<String> allStrings = new ArrayList<>();
        // Call recursive function to generate valid strings
        generate(allStrings, input, current, 0);
        int count = allStrings.size();
        String result[] = new String[count];
        for(int i = 0; i < count; i++){
            result[i] = allStrings.get(i);
        }
        return result;
    }

    public static void generate(List<String> allStrings, char[] input, char[] current, int start) {
        /*
         * Recursive function to generate all possible strings by replacing '?' with '1' and '0'.
         */
        if (start == input.length) {
            allStrings.add(new String(current));
            return;
        }
        // If found '?' then call recursive function by replacing '?' with '1' and then with '0'.
        if (input[start] == '?') {
            for (char c : possibleChars) {
                current[start] = c;
                generate(allStrings, input, current, start + 1);
            }
        } 
        else {
            // If found non '?' character then continue with setting current character as that character and continue
            current[start] = input[start];
            generate(allStrings, input, current, start + 1);
        }

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

        String s = bufferedReader.readLine().trim();

        String result[] = Result.find_all_possibilities(s);
        for (String str: result) {
            bufferedWriter.write(str+"\n");
        }

        bufferedWriter.close();

        bufferedReader.close();
    }

}

/**
 * Time complexity: O(n*(2^m))
 * Space complexity: O(n*(2^m))
 */

'''
