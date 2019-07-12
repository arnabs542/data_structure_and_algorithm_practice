'''
Levenshtein Distance
Problem Statement:
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is
 counted as 1 step.)
You have the following 3 operations permitted on a word:
a) Insert a character
b) Delete a character
c) Replace a character
The minimum no of steps required to convert word1 to word2 with the given set of allowed operations is called edit distance.

e.g. Minimum edit distance between the words 'kitten' and 'sitting', is 3.
kitten → sitten (substitution of "s" for "k")
sitten → sittin (substitution of "i" for "e")
sittin → sitting (insertion of "g" at the end)
Read more about edit distance here:
https://en.wikipedia.org/wiki/Edit_distance
Input/Output Format For The Function:
Input Format:
You will be given two strings word1 and word2.
Output Format:
Return an integer editDist, denoting the edit distance between given two input strings.
Input/Output Format For The Custom Input:
Input Format:
The first line should contain a string denoting word1.
The second line should contain a string denoting word2.
If word1 = “cat” and word2 = “bat”, then input should be:
cat
bat
Output Format:
There will be one line, containing an integer editDist, denoting the result returned by solution function.
For input word1 = “cat” and word2 = “bat”, output will be:
1
Constraints:
1 <= length(word1), length(word2) <= 1000
word1 and word2 contains lower case alphabets from a to z.
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
cat
bat
Sample Output 1:
1
Explanation 1:
1: Replace c with b.
Sample Test Case 2:
Sample Input 2:
qwe
q
Sample Output 2:
2
Explanation 2:
1: Add w
2: Add e
'''
import sys
import os


# Complete the function below.
def  levenshteinDistance(strWord1, strWord2):
    pass


f = sys.stdout
_strWord1 = str(input())
_strWord2 = str(input())
res = levenshteinDistance(_strWord1, _strWord2);
f.write(str(res) + "\n")
f.close()


'''
Recursive solution
The idea is process all characters one by one staring from either from left or right sides of both strings.
Let us traverse from right corner, there are two possibilities for every pair of character being traversed.
m: Length of strWord1 (first string)
n: Length of strWord2 (second string)
If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings.
 So we recur for lengths m-1 and n-1.
Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character
 of first string, recursively compute minimum cost for all three operations and take minimum of three values.
a)Insert: Recur for m and n-1
b)Remove: Recur for m-1 and n
c)Replace: Recur for m-1 and n-1
Optimal solution
We can memoize the recurrence relationship mentioned above or build an iterative version for the same problem.
If last characters match, then
dp[i][j] = dp[i-1][j-1];
Else
dp[i][j] = 1 + min(dp[i][j-1], // Insert
dp[i-1][j], // Remove
dp[i-1][j-1]); // Replace
Space Complexity: O(length(strWord1)*length(strWord2)) 
Time Complexity: O(length(strWord1)*length(strWord2))
'''
'''
import java.util.TreeSet;

public class OptimalSolution {
    /*
     * Space Complexity: O(length(strWord1)*length(strWord2)) 
     * Time Complexity: O(length(strWord1)*length(strWord2))
     */
    static int levenshteinDistance(String strWord1, String strWord2) {
        char a[] = strWord1.toCharArray();
        char b[] = strWord2.toCharArray();
        int n = a.length;
        int m = b.length;

        // Fill all values in table with a maximum value
        int dp[][] = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], n + m);
        }
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            // If second string is empty, only option is to
            // remove all characters of second string
            dp[i][0] = i;
        }
        for (int i = 1; i <= m; i++) {
            // If first string is empty, only option is to
            // isnert all characters of second string
            dp[0][i] = i;
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (a[i - 1] == b[j - 1]) {
                    // If last characters are same, ignore last char
                    // and recur for remaining string
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][j - 1]);
                } else {
                    // If the last character is different, consider all
                    // possibilities and find the minimum
                    dp[i][j] = Math.min(dp[i][j],
                            1 + Math.min(dp[i - 1][j - 1], // Replace
                                Math.min(dp[i - 1][j], // Remove
                                         dp[i][j - 1] // Insert
                                    )));
                }
            }
        }
        return dp[n][m];
    }
}
'''
