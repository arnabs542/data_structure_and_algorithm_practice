'''
Regex Matcher
Problem Statement:
Given a text string containing characters only from lowercase alphabetic characters and a pattern string containing characters
 only from lowercase alphabetic characters and two other special characters '.' and '*'.
Your task is to implement pattern matching algorithm that returns true if pattern is matched with text otherwise returns
 false. The matching must be exact, not partial.
Explanation of the special characters:
1) '.' - Matches a single character from lowercase alphabetic characters.
2) '*' - Matches zero or more preceding character. It is guaranteed that '*' will have one preceding character which can
 be any lowercase alphabetic character or special character '.'. But '*' will never be the preceding character of '*'. (That
 means "**" will never occur in the pattern string.)
'.' = "a", "b", "c", ... , "z".
a* = "a","aa","aaa","aaaa",... or empty string("").
ab* = "a", "ab", "abb", "abbb", "abbbb",...
Input Format:
There are two arguments, first one is string denoting text and second one is string denoting pattern.
Output Format:
Return boolean, true if text and pattern matches exactly, otherwise return false.
Constraints:
0 <= text length, pattern length <= 1000
Text string containing characters only from lowercase alphabetic characters.
Pattern string containing characters only from lowercase alphabetic characters and two other special characters '.' and
 '*'
In pattern string, It is guaranteed that '*' will have one preceding character which can be any lowercase alphabetic character
 or special character '.'. But '*' will never be the preceding character of '*'.
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
text = "abbbc" and pattern = "ab*c"
Sample Output 1:
true
Explanation 1:
Given pattern string can match:
"ac", "abc", "abbc", "abbbc", "abbbbc", ...
Sample Test Case 2:
Sample Input 2:
text = "abcdefg" and pattern = "a.c.*.*gg*"
Sample Output 2:
true
Explanation 2:
".*" in pattern can match  "", ".", "..", "...", "....", ...
"g*" in pattern can match "", "g", "gg", "ggg", "gggg", ...
Now, consider:
'.' at position 2 as 'b',
'.*'  at position {4,5} as "...",
'.*' at position {6,7} as "" and
[g*] at position {8,9} as "".
So, "a.c.*gg*" = "abc...g" where we can write "..." as "def". Hence, both matches.
Sample Test Case 3:
Sample Input 3:
text = "abc" and pattern = ".ab*.."
Sample Output 3:
false
Explanation 3:
If we take 'b*' as "" then also, length of the pattern will be 4 (".a.."). But, given text's length is only 3. Hence, they
 can not match.
'''
import math
import os
import re
import sys


#
# Complete the 'pattern_matcher' function below.
#
# The function accepts STRING text and pattern as parameter and returns BOOLEAN.
#

def pattern_matcher(text, pattern):
    pass


if __name__ == '__main__':
    text = input()
    pattern = input()

    fptr = sys.stdout

    result = pattern_matcher(text, pattern)

    fptr.write(str(int(result)) + '\n')

    fptr.close()

'''
We have provided two solutions and both solutions contain necessary comments to understand the approach used:
In both the solution we are making simplified pattern string from pattern string (explained below with examples). Basically,
 We are removing duplicate '*' character from pattern string and '*' itself also. We are also maintaining isStarChar boolean
 array to store whether simplified pattern character was followed by '*' in pattern string or not.
e.g. If pattern = [abc*c*c*dd*] then simplified pattern string = "abcdd" and isStarChar = [false, false, true, false, true].

Here, in this example we have removed [c*c*c*] and keep only one [c]. [c]'s position in simplified pattern string is 3.
 So, we have stored true at position 3 of isStarChar and also removed '*' from pattern string. Same for character 'd*'.

1) brute_solution.java
Time Complexity:
O(2^(len_simpl_pat + len_text))
Auxiliary Space Used:
O(len_pat + len_text).
We are using one extra character array and one boolean array to make simplified pattern string. Also, O(len_pat + len_text)
 space will be used by recursion stack.
Space Complexity:
O(len_pat + len_text).
As input is O(len_pat + len_text) and auxiliary space used is also O(len_pat + len_text). So, O(len_pat + len_text) + O(len_pat
 + len_text) -> O(len_pat + len_text).
2) optimal_solution.java
Time Complexity:
O(len_simpl_pat * len_text + (len_simpl_pat + len_text)).
O(len_simpl_pat + len_text) for reading input and simplifying pattern string.
This solution is using Dynamic Programming. In this method, We build a dp[][] 2D boolean array from top to bottom such that
 dp[i][j] indicates first i character of text string matches to first j character of pattern string or not.
Here, 3 cases will arise,
Case 1:
dp[i][j-1] is true.
It means first i character of text string matches with first j-1 character of simplified pattern string. So, dp[i][j] will
 be true if jth character of simplified pattern string is '*', it means isStarChar[j] should be true.
Case 2:
dp[i-1][j-1] is true.
It means first i-1 character of text string matches with first j-1 character of simplified pattern string. So, dp[i][j]
 will be true if jth character of simplified pattern string matches with ith character of text string. It can only be match
 if jth character of pattern string is '.' or same as ith character of text string.
Case 3:
dp[i-1][j] is true.
It means first i-1 character of text string matches with first j character of simplified pattern string. So, dp[i][j] will
 be true if jth character of simplified pattern string is '*' and can be match with ith character of text string. It can
 only be match if jth character of pattern string is '.' or same as ith character of text string.
Auxiliary Space Used:
O(len_simpl_pat * len_text + (len_pat + len_text)).
As we are using boolean array of size (len_simpl_pat * len_text) to store dp values, Char array of size len_pat to get simplified
 pattern string, boolean array of size len_pat to store is that toStarChar or not.
Space Compelxity:
O(len_simpl_pat * len_text + (len_pat + len_text)).
As input is O(len_pat + len_text) and auxiliary space used is O(len_simpl_pat * len_text + (len_pat + len_text)). So, O(len_pat
 + len_text) + O(len_simpl_pat * len_text + (len_pat + len_text)) -> O(len_simpl_pat * len_text + (len_pat + len_text)).
'''
'''
BRUTE FORCE
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        // TODO Auto-generated method stub

        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine(), pattern = sc.nextLine();
        System.out.println(pattern_matcher(text, pattern));
        sc.close();
    }

    // --------------------- START ------------------------------------

    public static boolean pattern_matcher(String text,String pattern) {

        int pLen = pattern.length();

        //This will store true at location i, if simplifiedPattern has "*" character at location i.

        boolean isStarChar[] = new boolean[pLen];
        String simplifiedPattern = simplifyPattern(pattern, isStarChar, pLen);
        return matcherBrute(simplifiedPattern, text, 0, 0,isStarChar);
        
    }

    /* 
    * Below function will remove duplicate '*' characters and '*' itself from pattern String, and will
    * return that string.
    * e.g. pattern = [a*a*bcd*] returns [abcd] and make true to isStarChar at position {0,3}. 
    */

    public static String simplifyPattern(String pattern, boolean isStarChar[], int pLen) {

            int ind = 0;
            char simplifiedChars[] = new char[pattern.length()];

            for(int i = 0 ; i < pLen ; ) {

                simplifiedChars[ind] = pattern.charAt(i);

                // If i'th character is followed by '*', then mark isStartChar[i] true.
                if(i + 1 < pLen && pattern.charAt(i+1) == '*') {

                    // Below 'if' condition is to handle Duplicate character.
                    // e.g. [a*a*bc*dd*] = [a*bc*dd*] because, 
                    //      you can write [a*a*] = [a*] which meaning is same.

                    if(ind - 1 >= 0 && isStarChar[ind-1] && simplifiedChars[ind-1] == simplifiedChars[ind]) {
                        ind--;
                    } else {
                        isStarChar[ind] = true;
                    }

                    // i+1'th character is "*". So, i increases by 2.

                    i = i + 2;
                } else {
                    i++;
                }
                ind++;
            }

            // Converting character array to string for simplicity.
            
            return new String(simplifiedChars , 0 , ind);
    }

    public static boolean matcherBrute(
                            String pattern, String text, int pInd, int tInd, boolean isStarChar[] 
                                         ){

        // If both the pointer reaches at the end, then it matches.

        if(pInd == pattern.length() && tInd == text.length()) {
            return true;
        }

        // If only pattern pointer reaches at the end, then there is no match.

        if(pInd == pattern.length()) {
            return false;
        }

        /*  If only text pointer reaches at the end,
        *  then there should be only star characters ("*") in pattern for match.
        */

        if(tInd == text.length()) {
            
            while(pInd < pattern.length()) {
                if( !isStarChar[pInd] ) {
                    return false;
                }
                pInd++;
            }

            return true;
        }

        /* When pattern character is not followed by '*', 
        *  but If it is a '.' or matches with the text character,
        *  then increases both the pointer and check.
        */

        if( 
           !isStarChar[pInd] && (pattern.charAt(pInd) == '.' 
               || pattern.charAt(pInd) == text.charAt(tInd))
                    ) {
                        
            return matcherBrute(pattern, text, pInd + 1, tInd + 1, isStarChar);
            
        }

        /* If pattern character has '*', then there can be two cases,
        *      1) It's a '.' (2 cases)
        .* 	        a) Match with the text character
        *           b) Ignore the '.'
        *       
        *       2) It's an alphabet
        *           if it matches with text character (2 cases)
        *               a) consider the pattern character
        *               b) ignore the pattern character
        *           else
        *               a) ignore the pattern character
        */

        if(isStarChar[pInd]) {

            if(pattern.charAt(pInd) == '.') {
                return matcherBrute(pattern, text, pInd, tInd + 1, isStarChar) 
                        || matcherBrute(pattern, text, pInd + 1 , tInd, isStarChar);
                
            } else {
                if(pattern.charAt(pInd) == text.charAt(tInd)) {
                    return matcherBrute(pattern, text, pInd, tInd + 1, isStarChar) 
                    || matcherBrute(pattern, text, pInd + 1 , tInd, isStarChar);

                } else {
                    return matcherBrute(pattern, text, pInd + 1, tInd, isStarChar);

                }
            }
        }

        return false;
    }

    // ----------------------------- STOP -------------------------
}
'''
'''
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        // TODO Auto-generated method stub

        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine(), pattern = sc.nextLine();
        System.out.println(pattern_matcher(text, pattern));	
        sc.close();
    }



    // -------------------------- START ---------------------------------

    public static boolean pattern_matcher(String text,String pattern) {

        int pLen = pattern.length();

        //This will store true at location i, if simplifiedPattern has "*" character at location i
        boolean isStarChar[] = new boolean[pLen];
        String simplifiedPattern = simplifyPattern(pattern, isStarChar, pLen);
        return matcher(simplifiedPattern, text, isStarChar);

    }

    /* 
    * Below function will remove duplicate '*' characters and '*' itself from pattern String, and will
    * return that string.
    * e.g. pattern = [a*a*bcd*] returns [abcd] and make true to isStarChar at position {0,3}. 
    */

    public static String simplifyPattern(String pattern, boolean isStarChar[], int pLen) {

            int ind = 0;
            char simplifiedChars[] = new char[pattern.length()];

            for(int i = 0 ; i < pLen ; ) {

                simplifiedChars[ind] = pattern.charAt(i);

                // If i'th character is followed by '*', then mark isStartChar[i] true.
                if(i + 1 < pLen && pattern.charAt(i+1) == '*') {

                    /* Below 'if' condition is to handle Duplicate character.
                     * e.g. [a*a*bc*dd*] = [a*bc*dd*], 
                     *      because you can write [a*a*] = [a*] which meaning is same.
                     */
                     
                    if(ind - 1 >= 0 && isStarChar[ind-1] && simplifiedChars[ind-1] == simplifiedChars[ind]) {
                        ind--;
                    } else {
                        isStarChar[ind] = true;
                    }

                    // i+1'th character is "*". So, i increases by 2.

                    i = i + 2;
                } else {
                    i++;
                }
                ind++;
            }

            // Converting character array to string for simplicity.

            return new String(simplifiedChars , 0 , ind);
        }

    public static boolean matcher(String pattern, String text, boolean isStarChar[]) {

        int pLen = pattern.length(), tLen = text.length();

        // If both strings are null, then return true.

        if(pLen == 0 && tLen == 0) {
            return true;
        }

        // If pattern is null but text is not, then return false.

        if(pLen == 0) {
            return false;
        }

        // dp[i][j] is true, if first i characters in given string matches the first j characters of pattern.

        boolean dp[][] = new boolean[tLen + 1][pLen + 1];
        dp[0][0] = true;
        if(isStarChar[0]) {
            dp[0][1] = true;
        }

        // If the given text is null, 
        // then it will be true till the all the characters in simplified string have "*".

        for(int pInd = 1 ; pInd < pLen ; pInd++) {

            if(dp[0][pInd] && isStarChar[pInd]) {
                dp[0][pInd+1] = true;
                continue;
            }

            break;
        }

        for(int tInd = 0 ; tInd < tLen ; tInd++) {

            for(int pInd = 0 ; pInd < pLen ; pInd++) {

                /* Note : First i character of text string means substring of text string 
                 *        with [0,i-1] positions.
                 *        same for pattern string.
                 */
                 
                // Case 1, explained in editorial

                if(dp[tInd + 1][pInd] && isStarChar[pInd]) {
                    dp[tInd + 1][pInd + 1] = true;
                    continue;
                }

                // Case 2, explained in editorial

                if(
                   dp[tInd][pInd] 
                       && (pattern.charAt(pInd) == '.' || pattern.charAt(pInd) == text.charAt(tInd))
                           ) {
                    dp[tInd + 1][pInd + 1] = true;
                    continue;
                }

                // Case 3, explained in editorial

                if(dp[tInd][pInd + 1] && isStarChar[pInd] && 
                        (pattern.charAt(pInd) == '.' || pattern.charAt(pInd) == text.charAt(tInd))) {					
                    dp[tInd + 1][pInd + 1] = true;
                    continue;
                }
            }
        }

        return dp[tLen][pLen];

    }

    // ------------------------------ STOP ----------------------------
}
'''
