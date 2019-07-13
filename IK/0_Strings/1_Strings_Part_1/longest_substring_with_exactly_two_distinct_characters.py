'''
Longest Substring With Exactly Two Distinct Characters
Problem Statement:
Given a string s of length n, find the length of the longest substring ss, that contains exactly two distinct characters.

There will be t test cases.
Input/Output Format For The Function:
Input Format:
There is only one argument s, denoting the input string.
Output Format:
Return an integer len, denoting length of ss.
(If there are no such substrings, then return 0)
Input/Output Format For The Custom Input:
Input Format:
The first line of the input should contain an integer t, denoting no. of test cases.
In the next t lines, ith line should contain a string si, denoting an input string s for ith test case.
If t = 3, s for 1st test case = “ababababa”, s for 2nd test case = “e” and s for 3rd test case = “baabcbab”, then input
 should be:
3
ababababa
e
baabcbab
Output Format:
There will be t lines for output, where ith line contains an integer leni, denoting resultant value len for ith test case.

For input t = 3, s for 1st test case = “ababababa”, s for 2nd test case = “e” and s for 3rd test case = “baabcbab”, output
 will be:
9
0
4
Constraints:
1 <= t <= 80
1 <= n <= 10^5
s may contain upper case alphabets, lower case alphabets and numerical values.
Sample Test Cases:
Sample Input 1:
2
eceba
abcdef
Sample Output 1:
3
2
Explanation 1:
In first case, 'ece' is the largest substring with exactly 2 distinct characters.
In second case, 'ab' is the largest substring with exactly 2 distinct characters. Also, 'bc', 'cd', 'de', 'ef' can be considered
 as substring with exactly 2 distinct characters.
Sample Input 2:
3
ababababa
e
baabcbab
Sample Output 2:
9
0
4
Explanation 2:
In first case, whole string 'ababababa' is the largest substring with exactly 2 distinct characters.
In second case, there is no substring with exactly 2 distinct characters.
In third case, 'baab' is the largest substring with exactly 2 distinct characters.
'''
import math
import os
import random
import re
import sys


# Complete the getLongestSubstringLengthExactly2DistinctChars function below.
def getLongestSubstringLengthExactly2DistinctChars(s):
    pass


if __name__ == "__main__":
    fptr = sys.stdout
    q = int(input())
    for _ in range(q):
        s = input()
        res = getLongestSubstringLengthExactly2DistinctChars(s)
        fptr.write(str(res) + '\n')
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
A naive approach would be to iterate over all possible substrings ss of input string s, check if it is a valid (i.e. contains
 exactly two distinct characters) substring or not. Maximum value of length out of all valid substrings is the required
 output.
While iterating over all substrings, we will iterate in such a manner that first all the substrings which starts from 0th
 index are covered, then the ones which starts from 1st index are covered, then ones from 2nd index, 3rd index and so on.
 And, while iterating over all substrings starting at ith index, we will break iteration while we hit on third distinct
 character found at index j>i.
Time Complexity:
O(n*n) where n is length of string s.
In the worst case, where we have only two distinct characters in the whole string, all substrings are valid. So, using this
 approach, code will iterate over all n^2 substrings.
Auxiliary Space Used:
O(1).
We are not storing anything extra.
Space Complexity:
O(n) where n is length of string s.
Input of function will take O(n) to store string s and as auxiliary space used is O(1).
O(n) + O(1) → O(n).
2) optimal_solution.java
Description:
An optimal approach would be as follows:
Let say, for current substring, starting point is i and j (for current value of i) is the index where there is first third
 distinct character, considering substring starting at i.
Now, using two pointer approach, move i forward (i.e i=i+1) until there is only two distinct characters in window [i,j]
 representing substring. Maintain a max variable 'res', which will be updated each time you find a valid substring while
 iterating string using two pointer approach. For maintaining frequency of characters in current window [i,j], we can use
 HashMap or similar data structure which allows O(1) amortized time complexities for lookup and add.
Time Complexity:
O(n) where n is length of string s.
As in this two pointer approach, none of the two pointers ever moves backward (i.e. to smaller value than its current value),
 complete string will be iterated twice only. Twice iteration of string will take O(n).
Auxiliary Space Used:
O(1).
We are just maintaining frequency map for at max three characters at any time hence O(1).
Space Complexity:
O(n) where n is length of string s.
Input of function will take O(n) to store string s and as auxiliary space used is O(1).
O(n) + O(1) → O(n).
'''
'''
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a string s of length n, find the length of the longest substring t that contains exactly two distinct
 * characters.
 */
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static int getLongestSubstringLengthExactly2DistinctChars(String s) {
        int max_len = 0;
        HashSet<Character> temp = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            temp.clear();
            // Considering substring starting from i and ending at j
            for (int j = i; j < s.length(); j++) {
                temp.add(s.charAt(j));
                // If size of temp set is more than 2 means substring s[i, j] 
                // have more than 2 distinct characters
                if (temp.size() > 2){
                    break;
                }
                // If size of temp set is equal to 2 means substring s[i, j] 
                // is composed of exactly 2 distinct characters hence we compare and store max_len
                if (temp.size() == 2){
                    max_len = Math.max(max_len, j - i + 1);
                }
            }
        }
        // Return maximum possible length of longest substring having exactly 2 distinct characters
        return max_len;
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

        int t = Integer.parseInt(bufferedReader.readLine().trim());
        while (t-- > 0) {
            String s = bufferedReader.readLine().trim();
            int l = Result.getLongestSubstringLengthExactly2DistinctChars(s);

            bufferedWriter.write(String.valueOf(l));
            bufferedWriter.newLine();
        }
        
        bufferedWriter.close();

        bufferedReader.close();
    }

}

/**
 * Time complexity: O(n^2)
 * Space complexity: O(n)
 */
'''
'''
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a string s of length n, find the length of the longest substring t that contains exactly two distinct
 * characters.
 */
import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static int getLongestSubstringLengthExactly2DistinctChars(String s) {
        int max_len = 0;
        HashMap<Character, Integer> countMap = new HashMap<>();
        int left = 0, right = 0;
        while (right < s.length()) {
            // We are maintaining character along with it's frequency
            if (countMap.containsKey(s.charAt(right))) {
                countMap.put(s.charAt(right), countMap.get(s.charAt(right))+1);
            }
            else{
                countMap.put(s.charAt(right), 1);
            }
            // If size of countMap is more than 2 means substring s[left, right] 
            // have more than 2 distinct characters so, we remove characters from left
            // while countMap size is more than 2
            while (countMap.size() > 2) {
                countMap.put(s.charAt(left), countMap.get(s.charAt(left)) - 1);
                if (countMap.get(s.charAt(left)) == 0){
                    countMap.remove(s.charAt(left));
                }
                left++;
            }
            // If size of countMap is equal to 2 means substring s[left, right] 
            // is composed of exactly 2 distinct characters hence we compare and store max_len
            if (countMap.size() == 2) {
                max_len = Math.max(max_len, right - left + 1);
            }
            right++;
        }
        // Return maximum possible length of longest substring having exactly 2 distinct characters
        return max_len;
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

        int t = Integer.parseInt(bufferedReader.readLine().trim());
        while (t-- > 0) {
            String s = bufferedReader.readLine().trim();
            int l = Result.getLongestSubstringLengthExactly2DistinctChars(s);
            bufferedWriter.write(String.valueOf(l));
            bufferedWriter.newLine();
        }
        
        bufferedWriter.close();

        bufferedReader.close();
    }

}
/**
 * Time complexity: O(n)
 * Space complexity: O(n)
*/
'''
